import logging

from telegram import ParseMode
from telegram.ext import Updater,Defaults


from config import Credentials

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


defaults = Defaults(parse_mode=ParseMode.HTML,run_async=True,disable_web_page_preview=True)
updater = Updater(token=Credentials.BOT_TOKEN,defaults=defaults)
dispatcher = updater.dispatcher
job_queue = updater.job_queue


