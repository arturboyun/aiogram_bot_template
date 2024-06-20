# Aiogram bot template
This is a template for easy start of bot async development for Telegram

### Setup
```shell
docker-compose up
```

##### Migrations
```shell
docker-compose run --rm bot aerich migrate
docker-compose run --rm bot aerich upgrade
docker-compose run --rm bot aerich downgrade
```

## TODO
- [X] Upload template
- [X] Change SQLAlchemy to TortoiseORM
- [X] Migrations for TortoiseORM
- [X] Add example for work with TortoiseORM
- [ ] Add FastAPI for webhook and other stuff
- [X] Add Docker Compose
- [ ] CI/CD example
- [ ] Migration to aiogram 3
- [ ] Migration to sqlalchemy v2 
