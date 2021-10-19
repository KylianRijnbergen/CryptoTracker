import os
from requests import Session
from requests.exceptions import ConnectionError, TooManyRedirects, Timeout
import json


class Coin:
    """
    A class that holds the basic information for our currencies.
    """

    def __init__(self, ticker):
        self.ticker = ticker
        self.name, self.id = self.get_coin_name_and_id()

    def get_coin_name_and_id(self):
        key = os.environ.get('COINMARKETCAP_API_KEY')

        url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }

        parameters = {
            'symbol': self.ticker
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            data = json.loads(response.text)

        name = data['data'][self.ticker]['name']
        cid = data['data'][self.ticker]['id']
        return name, cid

    def get_current_price(self):
        key = os.getenv("COINMARKETCAP_API_KEY")

        url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }
        parameters = {
            'id': self.id,
            'convert': 'EUR'

        }

        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            price = data['data'][f'{self.id}']['quote']['EUR']['price']
            return price

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print("An error occured!")
            return -1

    def __str__(self):
        return f"Coin is {self.ticker}. Name is {self.name}, and id is {self.id}. Price is {self.get_current_price()}"


if __name__ == "__main__":
    pass
