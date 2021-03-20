from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

currency='JPY'
url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert='+currency

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5233ea6b-e6f7-41c8-8926-857a768ce7f8',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url)
  results = json.loads(response.text)
  # print(json.dumps(results, sort_keys=True, indent=4))
  active_cryptocurrencies=results['data']['active_cryptocurrencies']
  active_market_pairs=results['data']['active_market_pairs']
  btc_dominance=results['data']['btc_dominance']
  total_market_cap=results['data']['quote'][currency]['total_market_cap']
  total_volume_24h=results['data']['quote'][currency]['total_volume_24h']
  last_updated=results['data']['last_updated']

  active_cryptocurrencies_string='{:,}'.format(active_cryptocurrencies)
  active_market_pairs_string='{:,}'.format(active_market_pairs)
  total_market_cap_string='{:,}'.format(total_market_cap)
  total_volume_24h_string='{:,}'.format(total_volume_24h)

  print()
  print('There are currently '+active_cryptocurrencies_string+' active cryptocurrencies and '+active_market_pairs_string+' active markets.')
  print('The global cap for '+ currency+' cryptocurrencies is '+total_market_cap_string+' and the 24h global volume is '+total_volume_24h_string+'.')
  print('Bitcoin\'s total percentage of the global cap is '+str(int(btc_dominance))+"%.")
  print()
  print('This information was last updated on '+str(last_updated)+'.')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
