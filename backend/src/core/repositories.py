from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.core.db.session import get_async_db
from src.shared.exceptions import DuplicateException
from src.shared.exceptions import NotFoundException


def filter_by_gen(id: int = None, **filters) -> dict:
    filter_by = dict(id=id)
    if id is None:
        filter_by = {**filters}
    return filter_by


class BaseMixin:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    @property
    def model(self):
        raise NotImplementedError

    async def _fetch_instance(self, id: int = None, db_item=None, **filters):
        filter_by = filter_by_gen(id, **filters)
        query = select(self.model).filter_by(**filter_by)

        if db_item is None:
            db_item = await self.db.execute(query)
            db_item = db_item.scalars().first()

        if db_item is None:
            raise NotFoundException
        return db_item


class CreateMixin(BaseMixin):
    async def create(self, data: BaseModel):
        db_item = self.model(**data.dict())
        try:
            self.db.add(db_item)
            await self.db.commit()
            await self.db.refresh(db_item)
        except IntegrityError:
            raise DuplicateException
        return db_item


class ReceiveMixin(BaseMixin):
    async def all(self, skip: int = 0, limit: int = 100, **filters):
        count_query = select(func.count(self.model.id))
        query = select(self.model).limit(limit).offset(skip)

        if len(filters):
            query = query.filter_by(**filters)
            count_query = count_query.filter_by(**filters)

        res = await self.db.execute(query)
        count = await self.db.execute(count_query)

        return {"count": count.scalar(), "results": res.scalars().all()}

    async def get(self, id: int = None, **filters):
        filter_by = filter_by_gen(id, **filters)

        query = select(self.model).filter_by(**filter_by)
        res = await self.db.execute(query)
        db_item = res.scalar()

        if db_item is None:
            raise NotFoundException
        return db_item


class UpdateMixin(BaseMixin):
    async def _update_fields(self, instance, data: dict):
        for var, value in data.items():
            setattr(instance, var, value)
        return instance

    async def update(
            self, id: int = None, data: dict = None, db_item=None, **filters
    ):
        instance = await self._fetch_instance(id, db_item, **filters)
        instance = await self._update_fields(instance, data)

        self.db.add(instance)

        await self.db.commit()
        await self.db.refresh(instance)
        return instance


class DeleteMixin(BaseMixin):
    async def delete(self, id: int = None, db_item=None, **filters):
        instance = await self._fetch_instance(id, db_item, **filters)
        await self.db.delete(instance)
        await self.db.commit()


class CRUDRepository(CreateMixin, UpdateMixin, DeleteMixin, ReceiveMixin):
    pass
