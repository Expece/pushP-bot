from aiogram import types

import src.utils as utils
from src.dispatcher import dp


@dp.message_handler(commands=['start'])
async def print_start(message: types.Message):
    await message.answer("Hello! Here you can save your passwords.\n"
                         "Commands:\n"
                         "/push [service_name] : [password]\n"
                         "/pmake\n")


@dp.message_handler(commands=['push'])
async def print_start(message: types.Message):
    ans = "Success"
    formated_message = utils.parse_message(message.text.strip(), "/push")
    if formated_message:
        service, password = formated_message
        utils.push_password(service, password, "passwords")
    else : ans = "Error"

    await message.answer(ans)


@dp.message_handler(commands=['pmake'])
async def print_start(message: types.Message):
    random_string = utils.generate_random_string()
    password = utils.encrypt_string(random_string)
    password = utils.format_password(password)
    await message.answer(password)


@dp.message_handler(commands=['pget'])
async def print_start(message: types.Message):
    output = utils.get_passwords("passwords")
    await message.answer(output)