from aiogram import Dispatcher


def setup_middleware(dp: Dispatcher):
    from .throttling import ThrottlingMiddleware
    from .logging import LoggingMiddleware
    from .user import UsersMiddleware
    from .i18n import i18n
    from .schedule import ScheduleMiddleware

    dp.middleware.setup(UsersMiddleware())
    dp.middleware.setup(i18n)
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    dp.setup_middleware(ScheduleMiddleware())
