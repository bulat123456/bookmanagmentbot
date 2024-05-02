from aiogram import F
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, SwitchTo
from aiogram_dialog.widgets.text import Const, Multi, Format

from src.dialogs.base import cancel_button, Paginator
from src.states.book import SearchBook
from .handlers import input_query_handler, select_book_handler
from .getters import get_books, get_book_by_id

search_book_query_window = Window(
    Const('Введите поисковой запрос'),
    MessageInput(
        func=input_query_handler
    ),
    cancel_button,
    state=SearchBook.search_book_query
)


search_book_select_window = Window(
    Multi(
        Format('Найденные книги по запросу "{query}".', when=F['books']),
        Format('По запросу "{query}" книг найдено не было.', when=~F['books'])
    ),
    Paginator(
        Select(
            Format("{item.title} | {item.author}"),
            items="books",
            id="select_book",
            item_id_getter=lambda item: item.id,
            on_click=select_book_handler,
        ),
        id="books",
        width=1,
        height=5,
    ),
    cancel_button,
    state=SearchBook.search_book_result,
    getter=get_books
)


all_books_info_window = Window(
    Format(
        'Название: {book.title}\n'
        'Автор: {book.author}\n'
        'Описание: {book.description}\n'
        'Жанр: {book.genre}\n'
    ),
    SwitchTo(
        Const('◀️ Назад'),
        id='back',
        state=SearchBook.search_book_result
    ),
    state=SearchBook.search_book_info,
    getter=get_book_by_id
)

search_book_dialog = Dialog(
    search_book_query_window,
    search_book_select_window,
    all_books_info_window
)
