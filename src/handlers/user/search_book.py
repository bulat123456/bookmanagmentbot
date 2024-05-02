from aiogram import Router, F, types
from aiogram_dialog import DialogManager, StartMode

from src.states.book import SearchBook

router = Router()


@router.message(F.text == 'Найти книгу')
async def search_book_handler(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        SearchBook.search_book_query,
    )
