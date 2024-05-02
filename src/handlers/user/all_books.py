from aiogram import Router, F, types
from aiogram_dialog import DialogManager, StartMode

from src.states.book import AllBooks

router = Router()


@router.message(F.text == 'Посмотреть все книги')
async def all_books_handler(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        AllBooks.all_books_select,
        mode=StartMode.NEW_STACK
    )
