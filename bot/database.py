from tortoise import Tortoise

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE

DB_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"


async def setup():
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['bot.models']}
    )
    await Tortoise.generate_schemas()
