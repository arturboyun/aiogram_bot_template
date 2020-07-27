from aiogram.types import ChatMemberStatus

from bot import database
import config
from bot.database import get_conn_and_cursor
from loguru import logger

from bot.misc import bot


async def create_user(user_id: int, username: str = None) -> str:
    if not await user_exists(user_id):
        if not username:
            username = 'none'
        conn, cursor = await get_conn_and_cursor()
        await cursor.execute(
            f"INSERT INTO users "
            f"(user_id, username) "
            f"VALUES (%s, %s)",
            (user_id, username,))
        await conn.commit()
        logger.info(f'Новый пользователь {user_id}')
        return '✅Вы успешно зарегистрированы'
    return '✅Кнопки бота были обновлены'


async def user_exists(user_id: int):
    res = await database.fetchone('users', ['user_id'], {'user_id': str(user_id)})
    if res:
        return True
    return False


async def check_chat_member(user_id: int) -> bool:
    chat = await bot.get_chat(config.CHAT_ID)
    chat_url = chat.invite_link
    chat_link = f'<a href="{chat_url}">ЧАТ</a>'
    try:
        member = await bot.get_chat_member(config.CHAT_ID, user_id)
        if member.status == ChatMemberStatus.LEFT:
            await bot.send_message(user_id, f'Нельзя пользоваться ботом не вступив в наш {chat_link}')
            return False
    except Exception:
        await bot.send_message(user_id, f'Нельзя пользоваться ботом не вступив в наш {chat_link}')
        return False
    return True
