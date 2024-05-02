from aiogram import Router, F, types
from aiogram_dialog import DialogManager, StartMode

from src.states.book import AddBook

router = Router()


@router.message(F.text == 'Добавить книгу')
async def add_book_handler(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        AddBook.add_book_title,
        mode=StartMode.NEW_STACK
    )
