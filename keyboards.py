from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db.scripts import get_user_pictures


start_kb_markup = [
    [
        InlineKeyboardButton(text='Rate pictures', callback_data='rate_pictures')
    ],
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
            callback_data=f'back_to_home'
        )
    )

    return builder.as_markup()