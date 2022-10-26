from utils import get_kb
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

def ask_for_city(update, context):
    update.message.reply_text('Введите город:')
    return 'city'

def check_city(update, context):
    update.message.reply_text('Сколько подобрать отелей?')
    #update.message.reply_text('Календарь', MyTranslationCalendar())
    return 'counter'

def dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю')

def greet_user(update, context):
    name = update.message.chat.first_name
    update.message.reply_text(f'Привет {name}', reply_markup=get_kb())

def search_cheapest(update, context):
    update.message.reply_text(f'Начинаю поиск... ТОП {update.message.text}')
    update.message.reply_text('Выгружаем фото?')
    #return get_photo()
    return 'photo'

def get_photo(update, context):
    a = 'https://exp.cdn-hotels.com/hotels/37000000/36790000/36789900/36789845/d4aada11_z.jpg'
    #update.message.reply_text('Выгружаем фото')
    update.message.reply_photo(a)
    return 'calendar'

def my_calndr(update, context):
    calendar, step = DetailedTelegramCalendar().build()
    update.message.reply_text(f'Select {LSTEP[step]}', reply_markup=calendar)
    # {LSTEP[step]}
