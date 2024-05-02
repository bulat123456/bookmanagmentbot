from aiogram_dialog import DialogManager

from src.database import BookService


async def get_books(
        book_service: BookService,
        dialog_manager: DialogManager,
        **_,
):
    if dialog_manager.dialog_data.get('query'):
        books = await book_service.get_by_genre(dialog_manager.dialog_data['query'])
    else:
        books = await book_service.get_all()
    return {"books": books}


async def get_book_info(
        book_service: BookService,
        dialog_manager: DialogManager,
        **_
):
    book = await book_service.get_by_id(dialog_manager.dialog_data['book_id'])
    return {'book': book}
