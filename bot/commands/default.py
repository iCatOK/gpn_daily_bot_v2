from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand
from utils.misc.logging import logger

from loader import _, bot, i18n


def get_default_commands(lang: str = 'en') -> list[BotCommand]:
    commands = [
        BotCommand('/start', _('start bot', locale=lang)),
        BotCommand('/help', _('how it works?', locale=lang)),
    ]

    return commands


async def set_default_commands():
    logger.info("Setting default commands...")
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())

    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)
    logger.info("Commands is set successfully.")


async def set_user_commands(user_id: int, commands_lang: str):
    await bot.set_my_commands(get_default_commands(commands_lang), scope=BotCommandScopeChat(user_id))
