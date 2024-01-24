import os

import pymysql
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json
from core.setings import settings
from core.unit.SignalState import Form
async def TasksKeyboardIn():
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
    with connect.cursor() as cursor:
        TasksKeyboardIn = InlineKeyboardBuilder()
        sqlCommand = "SELECT  ID, Name FROM `group`"
        cursor.execute(sqlCommand)
        for nameProject in cursor.fetchall():
            print(nameProject.get("Name"),nameProject.get("ID"))
            TasksKeyboardIn.button(text=nameProject.get('Name'), callback_data=str(nameProject.get("ID")))
        TasksKeyboardIn.adjust(1)
        TasksKeyboardIn.button(text="Send", callback_data=str(nameProject.get("ID")))
        TasksKeyboardIn.button(text="exit", callback_data="exit")

        return TasksKeyboardIn.as_markup()