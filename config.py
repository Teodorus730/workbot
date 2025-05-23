from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_username: str
    use_redis: bool


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_username=env.str("ADMIN"),
            use_redis=env.bool("USE_REDIS"),
        )
    )
