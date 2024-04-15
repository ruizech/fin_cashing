#
import requests
import random
import time
from archived.api_spot import APISpot

swap_account = {
    "name": "Accounting token swap",
    "memo": "BM accounting token swap",
    "api_key": "92e0c23802163a5f43d3599bd2b43f126b6a94af",
    "secret_key": "14c70a9b46cf54575e2a9c7810553300f2e9e75cee5423ca94bbd7c65c908524"
}

# Sharon
# swap_account = {
#     "name": "Accounting token swap",
#     "memo": "NJ Accounting",
#     "api_key": "c85bdc56ee49cb630cb0007a3869276a360671fb",
#     "secret_key": "e6b833835f24c873d3b937cd35192fdb010ee1054329033be1cd352a7cc9d2de"
# }

# Jimmy account

# swap_account = {
#     "name": "Meta-era account",
#     "memo": "metaera",
#     "api_key": "c79ad342b2dd9f9096542814f542c8f2de4eebc5",
#     "secret_key": "9153fd4d9f0b022d21454deea686287db70b7084988fab5b30e845d603638f17"
# }


spotAPI = APISpot(swap_account["api_key"], swap_account["secret_key"], swap_account["memo"])
balances = spotAPI.get_wallet()[0]["data"]["wallet"]


def get_trade_history(symbol):
    trades = spotAPI.get_symbol_trades(symbol)[0]['data']['trades']
    total_usdt = 0
    for i in range(len(trades)):
        total_usdt += float(trades[i]['amount'])

    return total_usdt

# print(spotAPI.get_symbol_trades("ARC_USDT")[0]['data']['trades'])

# print(get_trade_history("BMX_USDT"))

coins = []
for coin_item in balances:
    coin = coin_item["id"]
    if coin in ["ZPTC"]:
        symbol = coin + "_USDC"
    else:
        symbol = coin + "_USDT"

    if coin == 'USDT':
        print("USDT:", coin_item['available'])

    coins.append(coin)

    # get price
    price_url = f"https://api-cloud.bitmart.com/spot/v1/ticker_detail?symbol={symbol}"

    orderbook_url = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}"
    orderbook = requests.get(orderbook_url).json()["data"]
    try:
        #price = float(requests.get(price_url).json()["data"]["last_price"])
        bid1_price = float(orderbook["buys"][0]["price"])
    except:
        #price = 0
        bid1_price=0

    available = float(coin_item["available"])
    frozen = float(coin_item["frozen"])
    balance = (available + frozen) * bid1_price

    if balance >= 5.0: #only print coin with balance >= 5
        print(f"{coin}: {available}, {frozen}, {available+frozen}, {balance}")



    #print(coin, ":", float(coin_item["available"]), ",", float(coin_item["frozen"]), ",",
    #      float(coin_item["available"]) + float(coin_item["frozen"]), ",", (float(coin_item["available"]) + float(coin_item["frozen"])) * bid1_price)

excluded_coins = ["GIGA"]

included_coins = {"VSC": 0.028}
# included_coins = {"EVER": 0.0315}
# included_coins = {"BMX": 0.197}
# included_coins = {"PORK": 0.0000004}

while True:
    for coin_item in balances:
        try:
            coin = coin_item["id"]
            if coin not in excluded_coins and coin not in ["USDT", "USDC"] and coin in included_coins:
                # print(coin_item["id"], ":", float(coin_item["available"]), ",", float(coin_item["frozen"]), ",",
                #   float(coin_item["available"]) + float(coin_item["frozen"]))
                print()
                if coin in ["ZPTC"]:
                    symbol = coin + "_USDC"
                else:
                    symbol = coin + "_USDT"

                # get orderbook
                orderbook_url = f"https://api-cloud.bitmart.com/spot/v1/symbols/book?symbol={symbol}"
                orderbook = requests.get(orderbook_url).json()["data"]
                bid1_price = float(orderbook["buys"][0]["price"])

                # get order size
                # rand between 10 to 50 usdt
                order_value = random.randint(100, 200)
                order_amount = order_value / bid1_price
                if order_amount > float(coin_item["available"]):
                    order_amount = float(coin_item["available"])




                # place order
                if bid1_price >= included_coins[coin]:
                    print(symbol, bid1_price, order_amount)
                    oid = spotAPI.post_submit_limit_sell_order(symbol, size=order_amount, price=bid1_price)[0]["data"]["order_id"]
                    # cancel order
                    spotAPI.post_cancel_order(symbol, oid)
                else:
                    print(f"{symbol} price is too low, selling stops")

        except Exception as e:
            print(symbol, e)

    time.sleep(random.randint(10, 20))

