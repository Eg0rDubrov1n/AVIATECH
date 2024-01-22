from aiofiles import os
from aiogram import Bot
import json
from aiogram.fsm.context import FSMContext
from aiogram import types

from core.keyboards.inline import generatorMainKeyBoard, FORMPRINT, simpleQuestion
from core.unit.SignalState import Form, Specialist, FormMesegeInlineKeyboard
from aiogram.types import Message, CallbackQuery
PATH = "C:/Users/User/PycharmProjects/botIheteOtchet/FILE/"

async def process_name(message: Message, state: FSMContext, bot: Bot) -> None:
        existsFile = await os.path.exists(f"{PATH}{message.text}")
        print(existsFile)
        await state.update_data(namePjoject=message.text)

        await bot.delete_message(message.chat.id, message_id=message.message_id)
        if existsFile:
            await bot.edit_message_text(
                text=f"Ошибка ввода: Проект под именем {message.text} уже существует желаете заменит его. Желаете сохранить изменения в это проект?",
                reply_markup=await  simpleQuestion("NameProjectExistsYet"),
                chat_id=FormMesegeInlineKeyboard.ChatID,
                message_id=FormMesegeInlineKeyboard.MesegeID)
        else:
            await bot.edit_message_text(text="ОБНОВА", reply_markup=await generatorMainKeyBoard(state),
                                        chat_id=FormMesegeInlineKeyboard.ChatID,
                                        message_id=FormMesegeInlineKeyboard.MesegeID)


async def process_nameError(call: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    if (call == None or "NO_" in call.data):
        await state.update_data(namePjoject=None)

    await bot.edit_message_text(text="ОБНОВА", reply_markup=await generatorMainKeyBoard(state),
                                chat_id=FormMesegeInlineKeyboard.ChatID,
                                message_id=FormMesegeInlineKeyboard.MesegeID)





async def process_Description(message: Message, state: FSMContext, bot:Bot) -> None:
    print("State UPDETE Description")
    await state.update_data(Description=message.text)
    await bot.edit_message_text(text="ОБНОВА", reply_markup=await generatorMainKeyBoard(state),
                                chat_id=FormMesegeInlineKeyboard.ChatID, message_id=FormMesegeInlineKeyboard.MesegeID)


async def download_zipAction(message: Message, bot : Bot, state: FSMContext):
    # print(type(message.document.file_id))
    file_id = message.document.file_id
    # file = await bot.get_file(file_id)
    # file_path = file.file_path
    # print(file_path)
    await state.update_data(download_zip=file_id)
    await bot.edit_message_text(text="ОБНОВА", reply_markup=await generatorMainKeyBoard(state),
                                chat_id=FormMesegeInlineKeyboard.ChatID, message_id=FormMesegeInlineKeyboard.MesegeID)

    # await bot.download_file(file_path, f"text.{file_path[file_path.rfind('.'):]}")
    # file_path = file.file_path
    # print("DOWNLOAD ZIPPPP__>")
    # destination = r'C:\\Users\\User\\PycharmProjects\\Новая_папка'
    # destination_file = bot.download_file(file_path, destination)

# @dp.message(Form.nameOfTheSpecialist)
