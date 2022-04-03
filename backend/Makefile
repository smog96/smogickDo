api_container_name = smogickdo.api

build:
	docker-compose build

run:
	docker-compose up

run_detached:
	docker-compose up -d

kill:
	docker-compose down

status:
	docker ps -a

log:
	docker logs $(api_container_name)

inspect:
	docker exec -it $(api_container_name) bash

generate_migrations:
	docker exec -it $(api_container_name) alembic revision --autogenerate -m '$(message)'

migrate:
	docker exec -it $(api_container_name) alembic upgrade head

restart:
	make kill && make build && make run

test:
	docker exec -it drf pytest -v -s --code-highlight=yes

attach:
	docker attach $(api_container_name)

drop_volumes:
	docker-compose down -v
