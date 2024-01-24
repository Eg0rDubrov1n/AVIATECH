import archive
import os

import pymysql
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from core.TheTaskBook.keyboards.inline import TasksKeyboardIn
from core.setings import settings
from core.unit.SignalState import Form, Specialist, FormMesegeInlineKeyboard, Tasks

import aspose.zip as az
from openpyxl import Workbook

from core.keyboards.inline import generatorWorkerKeyBoard, generatorMainKeyBoard, FORMPRINT

async def NewTasks(message: Message, state: FSMContext) -> None:

    # await message.answer(text="Проекты", reply_markup = KeyWorkWithDocument)
    await state.set_state(Tasks.chosenUser)
    await message.answer(text="Users-->", reply_markup=await TasksKeyboardIn())
    # print(settings.server.host,
    #     settings.server.port,
    #        settings.server.user,
    #         settings.server.password,
    #         settings.server.db_name,sep='\n')
    # # try:
    # connect = pymysql.connect(
    #         host="127.0.0.1",
    #         port=3306,
    #         user="root",
    #         password="root",
    #         database="test12",
    #         cursorclass=pymysql.cursors.DictCursor
    #         # host=settings.server.host,
    #         # port=settings.server.port,
    #         # user=settings.server.user,
    #         # password=settings.server.password,
    #         # database=settings.server.db_name,
    #         # cursorclass=pymysql.cursors.DictCursor
    #     )
    # with connect.cursor() as cursor:
    #     x = "SELECT ID, Name FROM `group`"
    #     cursor.execute(x)
    #     for i in cursor.fetchall() :
    #         print(i.get("Name"),i.get("ID"))
    # # except Exception:
    #     print(Exception.args, "\nERROR")

async def chosenUser(call: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(chosenUser=call.data)
    print("name_of_the_specialist")
    await call.message.edit_message_text(text="Вывод Информации  о пользователе",
        reply_markup=await generatorWorkerKeyBoard()
    )