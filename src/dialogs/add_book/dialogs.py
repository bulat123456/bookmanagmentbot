from aiogram import F
from aiogram_dialog import (
    Window, Dialog,
)
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Format, Multi, Const

from src.dialogs.base.cancel import cancel_button
from src.states.book import AddBook
from .getters import get_genres
from .handlers import input_title_handler, input_author_handler, input_description_handler, select_genre_handler
from ..base import Paginator

add_book_title_window = Window(
    Const('Введите название книги'),
    MessageInput(
        func=input_title_handler
    ),
    cancel_button,
    state=AddBook.add_book_title
)

add_book_author_window = Window(
    Const('Введите автора книги'),
    MessageInput(
        func=input_author_handler
    ),
    cancel_button,
    state=AddBook.add_book_author
)

add_book_description_window = Window(
    Const('Введите описание книги'),
    MessageInput(
        func=input_description_handler
    ),
    cancel_button,
    state=AddBook.add_book_description
)

add_book_genre_window = Window(
    Multi(
        Const('Выберите жанр книги на клавиатуре или введите свой', when=F['genres']),
        Const('Введите жанр книги', when=~F['genres'])
    ),
    Paginator(
        Select(
            Format("{item.genre}"),
            items="genres",
            id="select_genre",
            item_id_getter=lambda item: item.id,
            on_click=select_genre_handler,
        ),
        id="genres",
        width=1,
        height=5,
    ),
    MessageInput(
        func=select_genre_handler
    ),
    cancel_button,
    state=AddBook.add_book_genre,
    getter=get_genres
)

add_book_finish_window = Window(
    Const('Вы успешно закончили добавление книги!'),
    cancel_button,
    state=AddBook.add_book_finish
)

add_book_dialog = Dialog(
    add_book_title_window,
    add_book_author_window,
    add_book_description_window,
    add_book_genre_window,
    add_book_finish_window
)
