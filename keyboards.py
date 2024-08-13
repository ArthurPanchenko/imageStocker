from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db.scripts import get_user_pictures


home_keyboard_markup = [
    [InlineKeyboardButton(text='Home', callback_data='home')]
]

home_keyboard = InlineKeyboardMarkup(inline_keyboard=home_keyboard_markup)

start_kb_markup = [
    [
        InlineKeyboardButton(text='My pictures', callback_data='list_pictures')
    ]
]

start_keyboard = InlineKeyboardMarkup(inline_keyboard=start_kb_markup)


def my_pictures_keyboard_builder(user_id):
    pictures = get_user_pictures(user_id)
    builder = InlineKeyboardBuilder()

    for picture in pictures:
        builder.row(
            InlineKeyboardButton(
                text=picture[0],
                callback_data=f'picture_{picture[1]}'
            )
        )
    
    builder.row(
        InlineKeyboardButton(
            text='Home',
            callback_data='home'
        )
    )

    return builder.as_markup()