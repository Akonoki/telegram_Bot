import telebot
from config import TOKEN, keys
from extenxions import Convertor, ConvertionExeption


bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу с ботом, введите комманду боту в следующем формате:' \
           '\n <имя валюты> <в какую валюту перевести> <количество валюты>\n' \
           'Увидеть список доступных валют: комманда /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    values = list(map(str.lower, values))
    try:
        result = Convertor.get_price(values)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \т {e}')
    else:
        text = f'Цена за {values[2]} {values[0]} в {values[1]} -- {result} {keys[values[1]]}'
        bot.reply_to(message, text)


bot.polling()
