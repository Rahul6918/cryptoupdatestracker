import requests


def get_prices():
    crypto_coins = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "LINK", "BNB", "XLM"]

    get_crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD,EUR,IND".format(",".join(crypto_coins))).json()["RAW"]

    data = {}
    for i in get_crypto_data:
        data[i] = {
            "coin": i,
            "price": get_crypto_data[i]["USD"]["PRICE"],
            "change_day": get_crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": get_crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data


if __name__ == "__main__":
    print(get_prices())
