from aiofiles import os
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
import aspose.zip as az
import tempfile
from core.keyboards.reply import KeyWorkWithDocument

from core.setings import settings
# from core.unit.SignalState import FileSend
from aiogram.types.input_file import FSInputFile
from openpyxl import load_workbook

from core.keyboards.inline import generatorWorkerKeyBoard, generatorMainKeyBoard, generatorArchiveKeyBoard


async def Archive(message: Message, state: FSMContext) -> None:
    from core.unit.SignalState import ArchiveState
    await state.set_state(ArchiveState.NameProject)
    # await message.answer(text="Проекты", reply_markup = KeyWorkWithDocument)

    await message.answer(text="Проекты", reply_markup = await generatorArchiveKeyBoard())

async def ActionWithProject(call: CallbackQuery, state: FSMContext):
    # print(call.data)
    await state.update_data(NameProject = call.data)
    await call.message.answer(text = call.data, reply_markup = KeyWorkWithDocument)

async def SendFileArchive(message: Message, state: FSMContext, bot: Bot) -> None:
    data = await state.get_data()
    name = data.get("NameProject")
    if name != None:
        await bot.send_document(message.chat.id,FSInputFile(f"{settings.bots.path_save}{name}"))
    else:
        print("EEEEEEEEEEEEELSE")
async def Editing(message: Message, state: FSMContext, bot: Bot) -> None:

    data = await state.get_data()
    name = settings.bots.path_save + data.get("NameProject")
    wb = load_workbook(filename=f'{name}')

    # fileTEXT = open(f"{name}/{data.get('namePjoject')}.txt", 'a')



async def ForwardGroup(message: Message, state: FSMContext, bot: Bot) -> None:
    pass
# await bot.send_document(call.message.chat.id,FSInputFile(f'{settings.bots.path_save}{call.data}'))
    # call.message.answer()
# async def SendFileArchive(call: CallbackQuery, state: FSMContext, bot: Bot):
#     # print(call.data)
#     await bot.send_document(call.message.chat.id,FSInputFile(f'{settings.bots.path_save}{call.data}'))
#     # call.message.answer()
