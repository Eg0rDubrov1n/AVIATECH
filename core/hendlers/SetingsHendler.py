from aiofiles import os
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
import aspose.zip as az
import tempfile
from core.setings import settings
from core.unit.SignalState import Specialist
from aiogram.types.input_file import FSInputFile
import json

from core.keyboards.inline import generatorWorkerKeyBoard, generatorMainKeyBoard, generatorArchiveKeyBoard, \
    generatorSetingsrKeyBoard


async def Setings(message: Message, state: FSMContext) -> None:
    await message.answer(text="Настройки", reply_markup = await generatorSetingsrKeyBoard())


async def new_the_specialist(call: CallbackQuery, state: FSMContext):
    await state.set_state(Specialist.specialistName)
    await call.answer("Введите имя")


async def process_new_the_specialist_name(message: Message, state: FSMContext, bot: Bot) -> None:
    with open('data1.json', 'r') as j:
            json_data = json.load(j)
            #     print(json_data)
            if not (message.text in json_data):
                print("State UPDETE Name")
                await state.update_data(specialistName=message.text)
                await state.set_state(Specialist.specialisttag)
            else:
                await bot.delete_message(message.chat.id,message_id=message.message_id)
                await message.answer("Ошибка ввода попробуйте снова")


def FindINvalues(json_data,text):
    for i in json_data.values():
        if text == i:
            return 1
    return 0
async def process_new_the_specialist_tag(message: Message, state: FSMContext, bot:Bot) -> None:
    with open('data1.json', 'r') as j:
            # json_data = dict()
            json_data = json.load(j)
            #     print(json_data)
            if not FindINvalues(json_data, message.text):
                print("State UPDETE Name")
                await state.update_data(specialisttag=message.text)
                await state.set_state(Specialist.specialisttag)
                data = await state.get_data()
                print(data)
                with open('data1.json', 'r') as j:
                    json_data = json.load(j)
                with open('data1.json', 'w') as outfile:
                    json_data[data.get("specialistName")] = data.get("specialisttag")
                    print(json_data)
                    json.dump(json_data, outfile)
                print(data)
                await state.clear()
                data = await state.get_data()
                print(data)
                #
            else:
                await bot.delete_message(message.chat.id,message_id=message.message_id)
                await message.answer("Ошибка ввода попробуйте снова")
