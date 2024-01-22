# Надо
#     обработать все ошибки
#     поработать над стилистикой
#     *Добавить редактирование уже существующих проектов
#     *Добавит расширяемый список специалистов
#     Вывод карточки проекта




import logging
import sys
from pydoc import html
from typing import Optional
import os
from aiofiles import os
from aiogram.dispatcher import router
from aiogram.enums import ContentType
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from datetime import datetime
from aiogram.filters import CommandStart, StateFilter, Command

from aiogram.handlers import callback_query
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.callback_query import CallbackQuery

from core.hendlers.SetingsHendler import new_the_specialist, process_new_the_specialist_name, \
    process_new_the_specialist_tag, Setings
from core.hendlers.action import process_name, process_Description, download_zipAction, process_nameError
from core.hendlers.baseAr import Archive, SendFileArchive, ActionWithProject
from core.hendlers.baseNew import *
from core.keyboards.reply import KeyGlobal
from core.setings import settings
from core.unit.SignalState import ArchiveState


# from core.unit.SignalState import FileSend


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.a

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,"12312321312312231123")
    await message.reply(f"Ваш Chat ID: {message.chat.id}")
    await message.answer("What Project?",reply_markup=KeyGlobal)
async def start():
    dp = Dispatcher()
    bot = Bot(settings.bots.bot_token)
    dp.message.register(get_start,Command(commands=["start","exit"]))
    dp.message.register(SendFileArchive,F.text.lower() == "скачать")

    dp.message.register(newProject,F.text.lower() == "новый проект")
    dp.message.register(Archive, F.text.lower() == "архив")
    dp.message.register(Setings, F.text.lower() == "настройки")

    dp.callback_query.register(exit, F.data.lower() == 'exit')

    dp.callback_query.register(name_pjoject, F.data.lower() == 'name_pjoject')
    dp.callback_query.register(name_of_the_specialist, F.data.lower() == 'name_of_the_specialist')
    dp.callback_query.register(description,F.data.lower() == 'description')
    dp.callback_query.register(download_zip,F.data.lower() == 'download_zip')
    dp.callback_query.register(send, F.data.lower() == 'send')
    # print(f"F Chek -- > {F.data.lower().find('NameProjectExistsYet') > 0}")
    dp.callback_query.register(process_nameError, F.data[3:] == 'NameProjectExistsYet')



    dp.callback_query.register(new_the_specialist, F.data.lower() == 'specialist')
    dp.message.register(process_new_the_specialist_name, Specialist.specialistName)
    dp.message.register(process_new_the_specialist_tag, Specialist.specialisttag)

    dp.message.register(process_name, Form.namePjoject)
    dp.message.register(process_Description, Form.Description)
    dp.message.register(download_zipAction, Form.download_zip,F.document)

    dp.callback_query.register(ActionWithProject,ArchiveState.NameProject)

    dp.callback_query.register(name_of_the_specialistPoint2, Form.nameOfTheSpecialist)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(start())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
