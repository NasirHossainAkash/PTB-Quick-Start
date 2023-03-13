import logging

from telegram.ext import CommandHandler


from bot import updater,dispatcher,job_queue
from bot.plugins import start_handler


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)





def main():
    dispatcher.add_handler(CommandHandler('start',start_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()