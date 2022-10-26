from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handlers import greet_user, search_cheapest, ask_for_city, check_city, dontknow, get_photo, my_calndr
from telegram_bot_calendar import LSTEP


def main():
    mybot = Updater('5538930168:AAGQJhWGQ7hfiZm1eVY_NL4debZjURvWyDg')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^([Пп]ривет)$'), greet_user))


    lowprice_conv = ConversationHandler(
        entry_points=[
            CommandHandler('lowprice', ask_for_city)
        ],
        states={
            'city': [MessageHandler(Filters.text, check_city)],
            'counter': [MessageHandler(Filters.text, search_cheapest)],
            'photo': [MessageHandler(Filters.text, get_photo)],
            'calendar': [CommandHandler(LSTEP, my_calndr)]
        },
        fallbacks=[MessageHandler(Filters.sticker, dontknow)]
    )

    dp.add_handler(lowprice_conv)

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
