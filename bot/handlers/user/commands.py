from aiogram import types
from aiogram.dispatcher import FSMContext


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f'Привет {message.from_user.full_name}')
