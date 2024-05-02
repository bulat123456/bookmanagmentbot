from aiogram_dialog import DialogManager

from src.database import BookService


async def get_books(
        book_service: BookService,
        dialog_manager: DialogManager,
        **_,
):
    query = dialog_manager.dialog_data['query']
    books = await book_service.get_by_query(query)
    return {"books": books, 'query': query}


async def get_book_by_id(
        book_service: BookService,
        dialog_manager: DialogManager,
        **_,
):
    book_id = dialog_manager.dialog_data['book_id']
    book = await book_service.get_by_id(book_id)
    return {"book": book}
