from bot import updater
from bot.plugins import start


def main():
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()