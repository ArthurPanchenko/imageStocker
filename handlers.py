from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

import text
import keyboards
from services.generate_image import generate_image
from db.scripts import create_picture_db, get_picture_by_id
from states import CreatePicture


router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greeting_text, reply_markup=keyboards.start_keyboard)
    await state.set_state(CreatePicture.picture_quote)


@router.callback_query(F.data == 'home')
async def home_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text.greeting_text, reply_markup=keyboards.start_keyboard)
    await state.set_state(CreatePicture.picture_quote)


@router.message(F.text, CreatePicture.picture_quote)
async def generate_image_handler(msg: Message, state: FSMContext):
    text_for_gen = msg.text
    
    path_to_image = await generate_image(text_for_gen)
    image = FSInputFile(path_to_image)

    await state.update_data(image=path_to_image)
    await state.set_state(CreatePicture.picture_title)
    await msg.answer_photo(image, caption=text.generated_picture_caption)


@router.message(F.text, CreatePicture.picture_title)
async def name_generated_picture(msg: Message, state: FSMContext):
    data = await state.get_data()
    image = FSInputFile(data['image'])
    title = msg.text

    create_picture_db(title, data['image'], msg.from_user.id)

    await msg.answer_photo(
        image,
        caption=text.named_picture_caption.format(title),
        reply_markup=keyboards.home_keyboard
    )
    await state.set_state(CreatePicture.picture_quote)


@router.callback_query(F.data == 'list_pictures')
async def my_pictures(call: CallbackQuery):
    await call.message.answer(text.my_pictures_text, reply_markup=keyboards.my_pictures_keyboard_builder(call.from_user.id))


@router.callback_query(F.data.startswith('picture_'))
async def picture(call: CallbackQuery):
    picture_id = int(call.data.split('_')[-1])

    picture = get_picture_by_id(picture_id)

    image = FSInputFile(picture.picture_url)
    
    await call.message.answer_photo(
        image,
        caption=f'{picture.title}\nPublished {picture.published}',
        reply_markup=keyboards.home_keyboard    
    )

