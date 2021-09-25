import json
import requests
from config import keys

class ConvertionExeption(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(values):

        if len(values) != 3:
            raise ConvertionExeption('Неверное количество параметров')

        quote, base, amount = values

        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/bd4330e0d9af18ee29b783b4/latest/{quote_ticker}/')
        total_base = float(json.loads(r.content)['conversion_rates'][base_ticker])*amount
        return round(total_base, 3)



