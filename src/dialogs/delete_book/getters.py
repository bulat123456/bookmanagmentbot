from src.database import BookService


async def get_books(
        book_service: BookService,
        **_,
):
    books = await book_service.get_all()
    return {"books": books}
