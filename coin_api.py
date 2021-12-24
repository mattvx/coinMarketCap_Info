"""
This simple python script is used to print coin info
from coinMarketcap. Pass the coin name as an argument to the script
"""

import requests, json, sys

try:
    coin = sys.argv[1]
except IndexError:
    print('You forgot to pass the coin as an arg!')
    exit()

# paste coin market cap api key
api_key = 'paste_here_coinbase_api_key'

# headers
request_headers = {
    "X-CMC_PRO_API_KEY": api_key,
    "Accept": 'application/json',
}

# actual request
base_url = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?slug=' + coin, headers=request_headers)

if base_url.status_code == 400:
    print('Coin not found!!!')
    exit()

# json to dict
base_url_data = json.loads(base_url.content)

# selecting the "Coin Numeric ID" necessary to select other k:v from the dict
for k in base_url_data['data']:
    coinIndexValue = k

percent_change_24h = base_url_data['data'][coinIndexValue]['quote']['USD']['percent_change_24h']

# printing stuff on console
print('Coin ID: ' + str(base_url_data['data'][coinIndexValue]['id']))
print('Coin name: ' + base_url_data['data'][coinIndexValue]['name'])
print('Coin symbol: ' + base_url_data['data'][coinIndexValue]['symbol'])
print('Rank: ' + str(base_url_data['data'][coinIndexValue]['cmc_rank']))
print('USD Price: ' + str(base_url_data['data'][coinIndexValue]['quote']['USD']['price']))
print('Percent change in last 24h: ' + str(percent_change_24h) + '%')
print('Last Updated: ' + base_url_data['data'][coinIndexValue]['quote']['USD']['last_updated'])