## Build and start
```bash
$ docker-compose build && docker-compose up
```

## Migrations

```bash
Create migration: $ docker exec -it $(api_container_name) alembic revision --autogenerate -m 'message'
Make migartion:   $ docker exec -it $(api_container_name) alembic upgrade head
```
