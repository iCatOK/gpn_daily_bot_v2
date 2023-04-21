from aiogram import Bot
from data import config


async def send_message_time(bot: Bot):
    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'Отправилось сообщение #1 (один раз)')


async def send_message_chronically(bot: Bot):
    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'Отправилось сообщение #2 (в одно и то же время)')


async def send_message_interval(bot: Bot):
    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, 'Отправилось сообщение #3 (интервал)')
