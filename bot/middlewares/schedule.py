from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils.misc.logging import logger


class ScheduleMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler = None) -> None:
        logger.info('Setting up a ScheduleMiddleware...')
        self.scheduler = scheduler if scheduler else AsyncIOScheduler(timezone='Asia/Yekaterinburg')
        self.scheduler.start()
        logger.info('ScheduleMiddleware set successfully.')
        super(ScheduleMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict[str]):
        data['scheduler'] = self.scheduler

    async def on_process_callback_query(self, callback_query: CallbackQuery, data: dict[str]):
        data['scheduler'] = self.scheduler

    async def on_process_inline_query(self, inline_query: InlineQuery, data: dict[str]):
        data['scheduler'] = self.scheduler
