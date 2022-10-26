from telegram import ReplyKeyboardMarkup


def get_kb():
    btns = [
        ['/lowprice', '/highprice'],
        ['/bestdeal', '/history']
    ]
    kb = ReplyKeyboardMarkup(btns, resize_keyboard=True)
    return kb
    