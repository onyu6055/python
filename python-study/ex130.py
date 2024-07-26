import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()
['data']


변동폭 = float(btc["data"]['max_price']) - float(btc["data"]['min_price'])
시작가 = float(btc["data"]['opening_price'])
최고가 = float(btc["data"]['max_price'])

if (시작가 + 변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")