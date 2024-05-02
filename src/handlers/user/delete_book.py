from aiogram import Router, F, types
from aiogram_dialog import DialogManager, StartMode

from src.states.book import DeleteBook

router = Router()


@router.message(F.text == 'Удалить книгу')
async def delete_book(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        DeleteBook.delete_book_select,
        mode=StartMode.NEW_STACK
    )
