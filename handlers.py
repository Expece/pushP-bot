from aiogram import types

import utils
from dispatcher import dp


@dp.message_handler(commands=['start'])
async def print_start(message: types.Message):
    await message.answer("Hello! Here you can save your passwords.\n"
                         "Commands:\n"
                         "/push [service_name] : [password]\n")


@dp.message_handler(commands=['push'])
async def print_start(message: types.Message):
    mess = utils.push_password([s.strip() for s in message.text[5:].split(":")])
    await message.answer(mess)