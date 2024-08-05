from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb_markup = [
    [
        InlineKeyboardButton(text='Rate pictures', callback_data='rate_pictures')
    ],
    [
        InlineKeyboardButton(text='My pictures', callback_data='list_pictures')
    ]
]

start_keyboard = InlineKeyboardMarkup(inline_keyboard=start_kb_markup)

