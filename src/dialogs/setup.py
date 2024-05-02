from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs as _setup_dialogs

from .add_book import add_book_dialog
from .delete_book import delete_book_dialog
from .search_book import search_book_dialog
from .all_books import all_books_dialog


def setup_dialogs(dispatcher: Dispatcher):
    dialogs = [add_book_dialog, delete_book_dialog, search_book_dialog, all_books_dialog]
    dispatcher.include_routers(*dialogs)
    _setup_dialogs(dispatcher)
