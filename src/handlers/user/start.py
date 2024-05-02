from aiogram import Router, types
from aiogram.filters.command import CommandStart

from src.keyboards.start import get_start_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer('Выберите действие на клавиатуре', reply_markup=get_start_keyboard())
