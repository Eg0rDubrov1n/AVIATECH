from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name_Tasks = State()
    designated_People = State()
    Description = State()
    download_zip = State()

class SpeciaParametrsWite(StatesGroup):
    Name = State()
    Password = State()


class Specialist(StatesGroup):
    ID = State()
    chaeckSpecialistPassword = State()
# class FileSend(StatesGroup):
#     fileSend = State()

class ArchiveState(StatesGroup):
    NameProject = State()

class FormMesegeInlineKeyboard():
    MesegeID = None
    ChatID = None

class Tasks(StatesGroup):
    chosenUser = State()

