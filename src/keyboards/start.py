from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text='Добавить книгу'),
        KeyboardButton(text="Удалить книгу"),
    )
    builder.row(
        KeyboardButton(text="Найти книгу"),
    )
    builder.row(
        KeyboardButton(text="Посмотреть все книги"),
    )
    return builder.as_markup(resize_keyboard=True)
