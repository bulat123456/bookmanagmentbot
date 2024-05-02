# Бот для управления книжной библиотекой

____
# Установка

1. Если у вас еще не установлен Python, то скачайте его с [официального сайта](https://www.python.org/downloads/) и
   установите poetry.
____
```cmd
pip install poetry
```
____
2. Отлично, теперь откройте файл `config.example.toml` и введите свои данные. Если вы не знаете как какие-либо значения, обратитесь к разделу "
   Заполнение конфига"
3. Переименуйте файл `config.example.toml` в `config.toml`
4. Запустите миграции для БД: `poetry run alembic revision --autogenerate -m "init"`, `poetry run alembic upgrade head`
4. Запустите бота командой `poetry run python bot.py`
____
# Заполнение конфига
____
## telegram
```toml
bot_token = '<BOT`S TOKEN>'
```
Получить токен бота можно [здесь](https://t.me/BotFather)
____
## database
```toml
dsn = 'sqlite+aiosqlite:///database.db'
```
Можно оставить без изменений.