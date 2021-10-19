from coin import Coin
import pandas as pd
class Portfolio:
    """
    A class that holds information about our portfolio.
    """

    def __init__(self):
        self.assets = pd.read_csv("myholdings.csv")
        self.balance = self.holdings()

    def list_coins(self):
        coins = []
        for index in range(self.assets.shape[0]):
            coin = self.assets.iloc[index][0]
            coins.append(coin)
        return coins

    def holdings(self):
        holdings = dict()
        for coin in self.list_coins():
            if coin not in holdings:
                index = int(self.assets.index[self.assets["Coin"] == coin].tolist()[0])
                balance = self.assets.iloc[index][1]
                holdings[coin] = balance
        return holdings

    def get_value(self):
        value = 0
        for coin in self.balance.keys():
            c = Coin(coin)
            coinval = c.get_current_price() * self.balance[coin]
            value += coinval
        return round(value,2)


if __name__ == "__main__":
    pass
