from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

KeyGlobal = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Архив"), KeyboardButton(text="Новый проект"), KeyboardButton(text="Настройки")]
    ]
)

KeyWorkWithDocument = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить"), KeyboardButton(text="Скачать"), KeyboardButton(text="Редактировать")],
        [KeyboardButton(text="/exit")]
    ]
)
# KeyWorkWithDocument = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[InlineKeyboardButton(text="Скачать", url=None, callback_data='downloads')]])
# #     inline_keyboard=[
# #         [],
# #         [InlineKeyboardButton(text="Отправить", url=None, callback_data='downloads')],
# #         [InlineKeyboardButton(text="Редактировать", url=None, callback_data='downloads')]
# #     ]
# # )