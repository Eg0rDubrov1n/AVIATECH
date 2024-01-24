import os

import pymysql
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from core.keyboards.reply import KeyGlobal
from core.setings import settings, Connect
from core.unit.SignalState import Form, Specialist, FormMesegeInlineKeyboard, SpeciaParametrsWite

from core.keyboards.inline import generatorWorkerKeyBoard, generatorMainKeyBoard, FORMPRINT

async  def Chose_Myself(call: CallbackQuery, state: FSMContext):
    print("-->",call.data)
    if call.data == "none_In_List":
        await call.message.answer(text="Введите имя")
        await state.set_state(SpeciaParametrsWite.Name)
    else:
        await state.update_data(specialistName=call.data)
        await state.set_state(Specialist.chaeckSpecialistPassword)
        await call.message.answer(text="Введите пароль")



async def CheakPasswordAndWrite(message: Message, state: FSMContext):
    connect = Connect()
    data = await state.get_data()
    with connect.cursor() as cursor:
        sqlCommand = f"SELECT Password FROM `group` WHERE ID={data.get('specialistName')}"
        print(f"sqlCommand------------------------------------------{sqlCommand}")
        cursor.execute(sqlCommand)
        if cursor.fetchall()[0]['Password']==message.text:
            sqlCommand = f"UPDATE `group` SET ChatID = {message.chat.id} WHERE ID={data.get('specialistName')};"
            cursor.execute(sqlCommand)
            connect.commit()
            await state.clear()
        else:
            await message.answer(text="Неверный пароль")

async def RegistrationName(message: Message, state: FSMContext):
    await state.update_data(Name=message.text)
    await state.set_state(SpeciaParametrsWite.Password)
    await message.answer(text="Введите пароль(до 15 символов)")

async def RegistrationPassword(message: Message, state: FSMContext):
    if len(message.text)<15:
        await state.update_data(Password=message.text)
        await WriteInSQL(state,message)
    else:
        await message.answer(text="Превышена максимальная длина пароля")

async def WriteInSQL(state: FSMContext,message: Message):
    connect = Connect()
    data = await state.get_data()
    isstr_queryKey = list()
    isstr_queryValues = list()
    for key, item in data.items():
        isstr_queryKey.append(f"'{key}'")
        isstr_queryValues.append(f"'{item}'")

    isstr_queryKey = ','.join(isstr_queryKey).replace('\'', '`')
    isstr_queryValues = ','.join(isstr_queryValues)

    with connect.cursor() as cursor:
        isstr_query = (f"INSERT INTO `group` ({isstr_queryKey},ChatID) VALUES ({isstr_queryValues},{message.chat.id});")
        print(isstr_query)
        cursor.execute(isstr_query)
        connect.commit()
    await state.clear()