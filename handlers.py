from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

import text
from services.generate_image import generate_image
from keyboards import start_keyboard
from states import CreatePicture


router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greeting_text, reply_markup=start_keyboard)


@router.message()
async def generate_image_handler(msg: Message, state: FSMContext):
    text_for_gen = msg.text
    
    path_to_image = await generate_image(text_for_gen)
    image = FSInputFile(path_to_image)

    await msg.answer_photo(image, caption=text.generated_picture_caption)
    await state.update_data(image=path_to_image)
    await state.set_state(CreatePicture.picture_title)


@router.message(F.text, CreatePicture.picture_title)
async def name_generated_picture(msg: Message, state: FSMContext):
    data = await state.get_data()
    image = FSInputFile(data['image'])
    await msg.answer_photo(image, caption=text.named_picture_caption.format(msg.text))