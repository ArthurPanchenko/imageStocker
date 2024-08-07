from aiogram.fsm.state import State, StatesGroup


class CreatePicture(StatesGroup):

    picture_title = State()
    picture_quote = State()
    
