from config_bot import TOKEN
import commond_bot as combot
from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', combot.play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, combot.get_candy)],

            2: [MessageHandler(Filters.text & ~Filters.command, combot.get_user_hod)]
        },
        fallbacks=[CommandHandler('stop', combot.stop)]
    )
    dp.add_handler(CommandHandler("start", combot.start))
    dp.add_handler(CommandHandler("rules", combot.rules))
    dp.add_handler(CommandHandler("exit", combot.exit))
    dp.add_handler(play_handler)

    updater.start_polling()
    updater.idle()
