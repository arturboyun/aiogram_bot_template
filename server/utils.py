import asyncio
from decimal import Decimal
from typing import Union

from aiogram.utils import exceptions
from loguru import logger

from bot.controllers.user import user_mention
from bot.misc import bot, config
from bot.models import User


async def send_message_to_payments_chat(amount: Decimal, worker: Union[User, None]):
    if worker:
        worker_mention = await user_mention(worker.uid, worker.full_name, worker.username)
    else:
        worker_mention = "Нету..."
    worker_percent = config.WORKER_PERCENT
    worker_money = float(amount) * float(worker_percent) / 100
    text = [
        f'🎄 <b>Новый залет</b> ✌️',
        f'💰 Сумма: {round(amount, 2)} руб.💰',
        f'❄️ Доля воркера: {worker_money} руб. {worker_percent}%',
        f'👨‍💻 Воркер: {worker_mention}',
    ]
    try:
        await bot.send_message(config.PAYMENTS_CHAT_ID, '\n'.join(text))
    except exceptions.ChatNotFound:
        logger.exception(f'Reports group ({config.PAYMENTS_CHAT_ID}) not found!')
        return
    except exceptions.ChatAdminRequired:
        bot_user = await bot.get_me()
        logger.exception(f'Bot ({bot_user.username}) is not admin in reports group ({config.PAYMENTS_CHAT_ID})!')
        return
    except exceptions.RetryAfter as e:
        logger.error(f"Target [ID:{config.PAYMENTS_CHAT_ID}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message_to_payments_chat(amount, worker)
    else:
        logger.info(f"Payment successful sent.")
