from telegram import Update
from telegram.ext import CallbackContext,CommandHandler

from bot import dispatcher

def start(update:Update,context:CallbackContext):
    update.message.reply_text("Hello world")


dispatcher.add_handler(CommandHandler('start',start))