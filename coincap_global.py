from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5233ea6b-e6f7-41c8-8926-857a768ce7f8',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url)
  data = json.loads(response.text)
  print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
