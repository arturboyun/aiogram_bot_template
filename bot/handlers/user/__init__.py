from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text

from bot.handlers.user.commands import cmd_start


async def setup(dp: Dispatcher):
    # Commands
    dp.register_message_handler(cmd_start, CommandStart(''), state='*')
