from aiogram.fsm.state import State, StatesGroup


class AddBook(StatesGroup):
    add_book_title = State()
    add_book_author = State()
    add_book_description = State()
    add_book_genre = State()
    add_book_finish = State()


class DeleteBook(StatesGroup):
    delete_book_select = State()
    delete_book_finish = State()


class SearchBook(StatesGroup):
    search_book_query = State()
    search_book_result = State()
    search_book_info = State()


class AllBooks(StatesGroup):
    all_books_select = State()
    all_books_search_by_genre = State()
    all_books_info = State()
