from aiogram import Router

from . import start
from . import add_new
from . import delete_book
from . import search_book
from . import all_books

router = Router()

router.include_router(start.router)
router.include_router(add_new.router)
router.include_router(delete_book.router)
router.include_router(search_book.router)
router.include_router(all_books.router)
