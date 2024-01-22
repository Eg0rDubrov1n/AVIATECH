from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    namePjoject = State()
    nameOfTheSpecialist = State()
    Description = State()
    download_zip = State()

class Specialist(StatesGroup):
    specialistName = State()
    specialisttag = State()

# class FileSend(StatesGroup):
#     fileSend = State()

class ArchiveState(StatesGroup):
    NameProject = State()

class FormMesegeInlineKeyboard():
    MesegeID = None
    ChatID = None

class Tasks(StatesGroup):
    chosenUser = State()

