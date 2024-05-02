from src.database import BookService


async def get_genres(
        book_service: BookService,
        **_,
):
    genres = await book_service.get_genres()
    return {"genres": genres}
