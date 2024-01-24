import os

import pymysql
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json
from core.setings import settings, Connect
from core.unit.SignalState import Form

async def FORMPRINT(state: FSMContext):
    data = await state.get_data()
    name = data.get("name_Tasks")
    print(f"-----------------{Form.__states__}---------------")
    print(f"-----------------{Form.name_Tasks}---------------")
    print(f"-----------------{state}---------------")
    print(f"-----------------{name}---------------")

async def generatorMainKeyBoard(state: FSMContext):
    data = await state.get_data()
    # state:FSMContext = Form.name_Tasks
    MainKeyBoard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Название проекта {["🔴","🟢"][data.get("name_Tasks") != None]}', url=None, callback_data='name_tasks')],
                         [InlineKeyboardButton(text=f'Назначте специалиста {["🔴","🟢"][data.get("designated_People") != None]}', url=None, callback_data='designated_people')],
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


def List_of_Employees():
    connect = Connect()
    with connect.cursor() as cursor:
        sqlCommand = "SELECT  ID, Name FROM `group`"
        cursor.execute(sqlCommand)
        return cursor.fetchall()
async def generatorWorkerKeyBoard(state: FSMContext):
    data = await state.get_data()
    TasksKeyboardIn = InlineKeyboardBuilder()
    for nameProject in List_of_Employees():
        print(nameProject.get("Name"), nameProject.get("ID"))
        TasksKeyboardIn.button(text=f'Name:{nameProject.get("Name")}{["🔴","🟢"][(data.get("designated_People") != None and str(nameProject.get("ID")) in data.get("designated_People"))]}', callback_data=str(nameProject.get("ID")))

    TasksKeyboardIn.button(text="exit", callback_data="exitMainKey")
    TasksKeyboardIn.adjust(1)
    return TasksKeyboardIn.as_markup()


async def EmployeeSelection():
    TasksKeyboardIn = InlineKeyboardBuilder()
    for nameProject in List_of_Employees():
        print(nameProject.get("Name"), nameProject.get("ID"))
        TasksKeyboardIn.button(
            text=f'Name:{nameProject.get("Name")}',
            callback_data=str(nameProject.get("ID")))

    TasksKeyboardIn.button(text="Нет в спске ", callback_data="none_In_List")
    # TasksKeyboardIn.adjust(2)
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


async def Calender():
    archiveKeyBoard = InlineKeyboardBuilder()
    print(settings.bots.path_save)
    for nameProject in os.listdir(settings.bots.path_save):
        archiveKeyBoard.button(text=nameProject, callback_data=nameProject)
    archiveKeyBoard.adjust(1)
    return archiveKeyBoard.as_markup()