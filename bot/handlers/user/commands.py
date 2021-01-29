from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.controllers import user


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f'Привет {message.from_user.full_name}')
    await user.create_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username
    )
