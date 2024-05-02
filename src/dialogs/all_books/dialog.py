from aiogram import F
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, SwitchTo
from aiogram_dialog.widgets.text import Multi, Const, Format

from src.dialogs.base import Paginator, cancel_button
from src.states.book import AllBooks
from .getters import get_books, get_book_info
from .handlers import select_book_handler, input_genre_handler

all_books_select_window = Window(
    Multi(
        Const('Выберите книгу из списка или нажмите кнопку "Поиск по жанру", если есть надобность.', when=F['books']),
        Const('В базе нет книг.', when=~F['books'])
    ),
    Paginator(
        Select(
            Format("{item.title} | {item.author}"),
            items="books",
            id="select_books",
            item_id_getter=lambda item: item.id,
            on_click=select_book_handler,
        ),
        id="books",
        width=1,
        height=5,
    ),
    SwitchTo(
        Const('Поиск по жанру'),
        id='search_by_genre',
        state=AllBooks.all_books_search_by_genre,
        when=F['books']
    ),
    cancel_button,
    state=AllBooks.all_books_select,
    getter=get_books
)


all_books_search_by_genre_window = Window(
    Const('Введите поисковой запрос'),
    MessageInput(
        func=input_genre_handler
    ),
    cancel_button,
    state=AllBooks.all_books_search_by_genre
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
        state=AllBooks.all_books_select
    ),
    state=AllBooks.all_books_info,
    getter=get_book_info
)


all_books_dialog = Dialog(
    all_books_select_window,
    all_books_search_by_genre_window,
    all_books_info_window
)
