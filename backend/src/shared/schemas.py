from fastapi_camelcase import CamelModel


class ListResponse(CamelModel):
    count: int
