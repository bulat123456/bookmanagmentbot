from aiogram import F
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Multi, Const, Format

from src.dialogs.base import Paginator, cancel_button
from src.states.book import DeleteBook
from .getters import get_books
from .handlers import select_delete_book_handler

delete_book_select_window = Window(
    Multi(
        Const('Выберите книгу для удаления.', when=F['books']),
        Const('В базе нет книг для удаления.', when=~F['books'])
    ),
    Paginator(
        Select(
            Format("{item.title} | {item.author}"),
            items="books",
            id="select_books",
            item_id_getter=lambda item: item.id,
            on_click=select_delete_book_handler,
        ),
        id="books",
        width=1,
        height=5,
    ),
    cancel_button,
    state=DeleteBook.delete_book_select,
    getter=get_books
)

delete_book_finish_window = Window(
    Const('Книга успешно удалена.'),
    cancel_button,
    state=DeleteBook.delete_book_finish
)

delete_book_dialog = Dialog(
    delete_book_select_window,
    delete_book_finish_window
)
