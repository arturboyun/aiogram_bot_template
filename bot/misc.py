import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.utils.executor import Executor
from loguru import logger

import config

ROOT_DIR: Path = Path(__file__).parent.parent

loop = asyncio.get_event_loop()
storage = RedisStorage(host=config.REDIS_HOST, port=config.REDIS_PORT)

bot = Bot(token=config.TELEGRAM_BOT_TOKEN, loop=loop, parse_mode='HTML')
dp = Dispatcher(bot=bot, loop=loop, storage=storage)

executor = Executor(dp, skip_updates=True)


async def setup():
    user = await bot.me
    logger.info(f"Bot: {user.full_name} [@{user.username}]")
    logger.debug(f'{ROOT_DIR=}')
