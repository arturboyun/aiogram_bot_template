from aiogram import Dispatcher

# from . import errors
from . import admin
from . import user


async def setup(dp: Dispatcher):
    # await errors.setup(dp)
    # todo: await admin.setup(dp)
    await user.setup(dp)
