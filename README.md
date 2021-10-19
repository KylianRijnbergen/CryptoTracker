--- This tool is currently in development ---

HOW TO USE:
To use the tool, create a file called "myholdings.csv".
In this file, denote assets in the format: "Ticker,Balance" (no spaces).
The first line should be: "Coin,Balance".

e.g.

Coin,Balance
BTC,0
ETH,1
BNB,2
ADA,3

In addition, add your COINMARKETCAP API key to your system environment variables.
The variable name must be "COINMARKETCAP_API_KEY".

You can now run main.py to obtain the value of your portfolio. This value will be in EUR.
