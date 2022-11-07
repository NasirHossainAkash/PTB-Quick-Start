import logging

from telegram import ParseMode
from telegram.ext import Updater,Defaults


from config import bot_token

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


defaults = Defaults(parse_mode=ParseMode.HTML,run_async=True)
updater = Updater(token=bot_token,defaults=defaults)
dispatcher = updater.dispatcher


