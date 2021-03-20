from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


listings_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   'start':'1',
#   'limit':'100',
#   'sort' : 'name',
#   'convert':'USD'
# }

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5233ea6b-e6f7-41c8-8926-857a768ce7f8',
}

session = Session()
session.headers.update(headers)

try:

    choice=input("Do you want to enter any custom parameters? (y/n)")
    if choice=='y':
        limit=input('What is the custom limit?: ')
        start=input('What is the custom start number?: ')
        sort=input('What do you want to sort by?: ')
        convert=input('What is your local currency?: ')

    listings_url += '&limit='+ limit+'&sort='+sort+'&start='+start+'&convert='+convert
    response = session.get(listings_url)
    results = json.loads(response.text)
    print(json.dumps(results, sort_keys=True, indent=4))

except (ConnectionError, Timeout, TooManyRedirects) as e:
     print(e)
