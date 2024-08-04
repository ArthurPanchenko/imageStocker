from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from services.generate_image import generate_image

router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer('Working LOL')

@router.message()
async def message(msg: Message):
    text_for_gen = msg.text
    path_to_image = await generate_image(text_for_gen)
    image = FSInputFile(path_to_image)

    await msg.answer_photo(image)
