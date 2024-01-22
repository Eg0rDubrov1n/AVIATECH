import os

import pymysql
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json
from core.setings import settings
from core.unit.SignalState import Form

async def FORMPRINT(state: FSMContext):
    data = await state.get_data()
    name = data.get("namePjoject")
    print(f"-----------------{Form.__states__}---------------")
    print(f"-----------------{Form.namePjoject}---------------")
    print(f"-----------------{state}---------------")
    print(f"-----------------{name}---------------")

async def generatorMainKeyBoard(state: FSMContext):
    data = await state.get_data()
    # state:FSMContext = Form.namePjoject
    MainKeyBoard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Название проекта {["🔴","🟢"][data.get("namePjoject") != None]}', url=None, callback_data='name_pjoject')],
                         [InlineKeyboardButton(text=f'Назначте специалиста {["🔴","🟢"][data.get("nameOfTheSpecialist") != None]}', url=None, callback_data='name_of_the_specialist')],
                         [InlineKeyboardButton(text=f'Описание {["🔴","🟢"][data.get("Description") != None]}', url=None, callback_data='description')],
                         [InlineKeyboardButton(text=f'Загрузить ZIP файл {["🔴","🟢"][data.get("download_zip") != None]}', url=None, callback_data='download_zip')],
                         [InlineKeyboardButton(text='Send', url=None, callback_data='send'), InlineKeyboardButton(text='Exit', url=None, callback_data='exit')]])
    return MainKeyBoard

# async def generatorWorkerKeyBoard():
#     workload = '' #  Потом реализовать отметку загруженности специалиста
#     MainKeyBoard = InlineKeyboardMarkup(
#         inline_keyboard=[[InlineKeyboardButton(text=f'Egor {workload}', url=None, callback_data='egor')],
#                          [InlineKeyboardButton(text=f'NoName {workload}', url=None, callback_data='noname')],
#                          [InlineKeyboardButton(text='All', url=None, callback_data='all'), InlineKeyboardButton(text='Exit', url=None, callback_data='exit_worker')]])
#     return MainKeyBoard

async def generatorWorkerKeyBoard(state: FSMContext):
    connect = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="test12",
        cursorclass=pymysql.cursors.DictCursor
        # host=settings.server.host,
        # port=settings.server.port,
        # user=settings.server.user,
        # password=settings.server.password,
        # database=settings.server.db_name,
        # cursorclass=pymysql.cursors.DictCursor
    )
    data = await state.get_data()
    with connect.cursor() as cursor:
        TasksKeyboardIn = InlineKeyboardBuilder()
        sqlCommand = "SELECT  ID, Name FROM `group`"
        cursor.execute(sqlCommand)
        for nameProject in cursor.fetchall():
            print(nameProject.get("Name"), nameProject.get("ID"))
            if data.get("nameOfTheSpecialist") != None:
                print("affasm--->",str(nameProject.get("ID")) in data.get("nameOfTheSpecialist"))
                print("affasm--->",nameProject.get("ID") , data.get("nameOfTheSpecialist"))

            TasksKeyboardIn.button(text=f'Name:{nameProject.get("Name")}{["🔴","🟢"][data.get("nameOfTheSpecialist") != None and str(nameProject.get("ID")) in data.get("nameOfTheSpecialist")]}', callback_data=str(nameProject.get("ID")))


        TasksKeyboardIn.button(text="exit", callback_data="exitMainKey")
        TasksKeyboardIn.adjust(1)
        return TasksKeyboardIn.as_markup()


async def generatorArchiveKeyBoard():
    archiveKeyBoard = InlineKeyboardBuilder()
    print(settings.bots.path_save)
    for nameProject in os.listdir(settings.bots.path_save):
        archiveKeyBoard.button(text=nameProject, callback_data=nameProject)
    archiveKeyBoard.adjust(1)
    return archiveKeyBoard.as_markup()


async def generatorSetingsrKeyBoard():
    workload = '' #  Потом реализовать отметку загруженности специалиста
    MainKeyBoard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Новый специалист {workload}', url=None, callback_data='specialist')],
                         # [InlineKeyboardButton(text=f'NoName {workload}', url=None, callback_data='noname')],
                         [InlineKeyboardButton(text='Exit', url=None, callback_data='exit')]])
    return MainKeyBoard

async def simpleQuestion(nameDef):
    simpleQuestionKeyBoard = InlineKeyboardMarkup(
        inline_keyboard=[
                         [InlineKeyboardButton(text='YES', url=None, callback_data=f'YES{nameDef}'),
                          InlineKeyboardButton(text='NO', url=None, callback_data=f'NO_{nameDef}')]])
    return simpleQuestionKeyBoard