import requests

amount = input('Choice: \n1. USD\2. EUR\3. ')

response = requests.get('sait')
exchange_rate = response.json()['rates']
usd_rate = exchange_rate['USD']
USD_AMOUND = amount * usd_rate

us_dollars = USD_AMOUND

