import requests

ticker = "Insta"
api_key = "491d605f661542d0910b711c5bb6cd04"

def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()

    if 'price' in response:
        price = response['price']
        return price
    else: 
        print("The price is not")
        return None
  


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()

    if 'price' in response:
        price = response['price']
        return price
    else: 
        print("The price is not available")
        return None
   

stockdata = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

# exchange = stockdata['exchange']
# currency = stockdata['currency']
# open_price = stockdata['open']
# high_price = stockdata['high']
# low_price = stockdata['low']
# close_price = stockdata['close']
# volume = stockdata['volume']
name = stockdata['name']

print(name, stock_price)