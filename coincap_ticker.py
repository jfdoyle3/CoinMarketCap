from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

while True:

    listings_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
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
            convert=input('What is your local currency?: ')
            parameters = {
              'start':start,
              'limit':limit,
              'sort_dir' :'desc',
              'convert':convert
            }

        if choice=='n':
            convert='USD'
            parameters = {
                  'start':'1',
                  'limit':'100',
                  'sort_dir' :'desc',
                  'convert': convert
                }


        response = session.get(listings_url, params=parameters)
        results = json.loads(response.text)
        #print(json.dumps(results, sort_keys=True, indent=4))
        data=results['data']

        print()
        for currency in data:
            rank=currency['cmc_rank']
            name=currency['name']
            symbol=currency['symbol']

            circulating_supply=currency['circulating_supply']
            total_supply=currency['total_supply']

            quotes=currency['quote'][convert]
            market_cap=quotes['market_cap']
            hour_change=quotes['percent_change_1h']
            day_change=quotes['percent_change_24h']
            week_change=quotes['percent_change_7d']
            price=quotes['price']
            volume=quotes['volume_24h']

            total_supply_string='{:,}'.format(total_supply)
            circulating_supply_string='{:,}'.format(circulating_supply)
            market_cap_string='{:,}'.format(market_cap)
            volume_string='{:,}'.format(volume)

            print(str(int(rank))+': '+ name+'('+symbol+')' )
            print('Market cap: \t\t$'+market_cap_string)
            print('Price: \t\t\t$'+str(int(price)))
            print('24h Volume: \t\t$'+volume_string)
            print('Hour change: \t\t'+ str(int(hour_change))+'%')
            print('Day change: \t\t'+str(int(day_change))+'%')
            print('Week change: \t\t'+str(int(week_change))+'%')
            print('Total supply: \t\t'+total_supply_string)
            print('Circulating supply: \t'+circulating_supply_string)
            print('Percentage of coins in circulation: '+str(int(circulating_supply/total_supply)))
            print()



    except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)

    choice=input('Again? (y/n)')
    if choice=='n':
            break;
