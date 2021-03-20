from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


map_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5233ea6b-e6f7-41c8-8926-857a768ce7f8',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(map_url)
    results = json.loads(response.text)
    data=results['data']
    #print(json.dumps(results, sort_keys=True, indent=4))
    for currency in data:
        rank=currency['id']
        name=currency['name']
        symbol=currency['symbol']
        print(str(int(rank))+': '+name+'('+symbol+')')


except (ConnectionError, Timeout, TooManyRedirects) as e:
     print(e)
