import requests
import json

BASE_ENDPOINT = "https://coincheck.com"

def get_ticker():
    """ティッカー"""
    ENDPOINT = BASE_ENDPOINT + "/api/ticker"
    res = requests.get(ENDPOINT)
    return res.json()

def get_trades(pair="btc_jpy"):
    """全取引履歴"""
    ENDPOINT = BASE_ENDPOINT + "/api/trades"
    PARAMS = {"pair": pair}
    res = requests.get(ENDPOINT, params=PARAMS)
    return res.json()

def get_order_books():
    """板情報"""
    ENDPOINT = BASE_ENDPOINT + "/api/order_books"
    res = requests.get(ENDPOINT)
    return res.json()

def get_exchange_orders_rate(order_type, pair="btc_jpy"):
    """レート取得"""
    ENDPOINT = BASE_ENDPOINT + "/api/exchange/orders/rate"
    PARAMS = {
        "order_type": order_type,
        "pair": pair,
        #"price": 28000
        "amount": 1.0
    }
    res = requests.get(ENDPOINT, params=PARAMS)
    return res.json()

def get_rate(pair="btc_jpy"):
    """販売レート取得"""
    ENDPOINT = BASE_ENDPOINT + "/api/rate/" + pair
    res = requests.get(ENDPOINT)
    return res.json()


ticker = get_ticker()
print("ティッカー")
print(json.dumps(ticker, indent=4, ensure_ascii=False))

trades = get_trades()
print("全取引情報")
print(json.dumps(trades, indent=4, ensure_ascii=False))

order_books = get_order_books()
print("板情報")
print(json.dumps(order_books, indent=4, ensure_ascii=False))

exchange_orders_rate_sell = get_exchange_orders_rate("sell")
print("レート取得（売り）")
print(json.dumps(exchange_orders_rate_sell, indent=4, ensure_ascii=False))

exchange_orders_rate_buy = get_exchange_orders_rate("buy")
print("レート取得（買い）")
print(json.dumps(exchange_orders_rate_buy, indent=4, ensure_ascii=False))

rate = get_rate()
print("販売レート取得")
print(json.dumps(rate, indent=4, ensure_ascii=False))

