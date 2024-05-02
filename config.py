from dataclasses import dataclass

import toml


@dataclass
class Telegram:
    bot_token: str


@dataclass
class Database:
    dsn: str


@dataclass
class Config:
    telegram: Telegram
    database: Database

    @classmethod
    def from_file(cls, filename: str) -> "Config":
        config = toml.load(filename)
        return cls(
            telegram=Telegram(**config["telegram"]),
            database=Database(**config['database'])
        )
