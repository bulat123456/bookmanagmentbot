from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import ManagedWidget
from aiogram_dialog.widgets.kbd import Select

from src.database import BookService
from src.states.book import DeleteBook


async def select_delete_book_handler(
        message: CallbackQuery,
        __: ManagedWidget[Select],
        manager: DialogManager,
        item_id: str,
):
    book_service: BookService = manager.middleware_data['book_service']
    book = await book_service.get_by_id(int(item_id))
    book.is_delete = True
    await book_service.update(book)
    await manager.switch_to(DeleteBook.delete_book_finish)
