from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import ManagedWidget
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select

from src.database import BookService
from src.states.book import AddBook


async def input_title_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.dialog_data['title'] = message.text
    await manager.switch_to(AddBook.add_book_author)


async def input_author_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.dialog_data['author'] = message.text
    await manager.switch_to(AddBook.add_book_description)


async def input_description_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.dialog_data['description'] = message.text
    await manager.switch_to(AddBook.add_book_genre)


async def select_genre_handler(
        message: [Message, CallbackQuery],
        __: [ManagedWidget[Select], MessageInput],
        manager: DialogManager,
        item_id: str = None,
):
    book_service: BookService = manager.middleware_data['book_service']
    if isinstance(message, CallbackQuery):
        genre = (await book_service.get_by_id(int(item_id))).genre
        manager.dialog_data['genre'] = genre
    else:
        manager.dialog_data['genre'] = message.text
    await book_service.create(manager.dialog_data['title'], manager.dialog_data['author'],
                              manager.dialog_data['description'], manager.dialog_data['genre'])
    await manager.switch_to(AddBook.add_book_finish)
