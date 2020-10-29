from tortoise import Tortoise

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    },
    "apps": {
        "models": {
            "models": ["bot.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def setup():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()
