from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Cancel, Button
from aiogram_dialog.widgets.text import Const

from src.keyboards.start import get_start_keyboard


async def cancel_handler(
        call: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    state: FSMContext = manager.middleware_data['state']
    if state:
        await state.clear()
    await call.message.delete()
    await call.message.answer('Выберите действие на клавиатуре', reply_markup=get_start_keyboard())


cancel_button = Cancel(
    text=Const('◀️ Назад'),
    on_click=cancel_handler
)
