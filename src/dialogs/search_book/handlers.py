from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import ManagedWidget
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select

from src.states.book import SearchBook


async def input_query_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.dialog_data['query'] = message.text
    await manager.switch_to(SearchBook.search_book_result)


async def select_book_handler(
        message: CallbackQuery,
        __: ManagedWidget[Select],
        manager: DialogManager,
        item_id: str,
):
    manager.dialog_data['book_id'] = int(item_id)
    await manager.switch_to(SearchBook.search_book_info)
