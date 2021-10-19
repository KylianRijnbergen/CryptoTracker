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


if __name__ == "__main__":
    p = Portfolio()
    print(p.balance)
