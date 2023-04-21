from datetime import datetime, timedelta

from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.commands import get_admin_commands, get_default_commands
from bot.commands import set_admin_commands
from bot.keyboards.default import get_default_markup
from loader import dp, bot, _
from models import User
from utils import schedule_events


@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    if user.is_admin:
        await set_admin_commands(user.id, user.language)

    text = _('Hello {full_name}!').format(full_name=user.name)

    await message.answer(text, reply_markup=get_default_markup(user))


@dp.message_handler(i18n_text='Help 🆘')
@dp.message_handler(CommandHelp())
async def _help(message: Message, user: User):
    commands = get_admin_commands(user.language) if user.is_admin else get_default_commands(user.language)

    text = _('Help 🆘') + '\n\n'
    for command in commands:
        text += f'{command.command} - {command.description}\n'

    await message.answer(text)


@dp.message_handler(i18n_text='Delayed message')
@dp.message_handler(commands=['delay'])
async def _delayed_message(message: Message, scheduler: AsyncIOScheduler):
    scheduler.add_job(schedule_events.send_message_time,
                      trigger='date',
                      run_date=datetime.now() + timedelta(seconds=10),
                      kwargs={'bot': bot})

    await message.answer('Через 10 секунд придёт сообщение')

