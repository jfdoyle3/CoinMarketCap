import xlsxwriter
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

start=1
f=1

crypto_workbook=xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet=crypto_workbook.add_worksheet()

crypto_sheet.write('A1','Name')
crypto_sheet.write('B1','Symbol')
crypto_sheet.write('C1','Market Cap')
crypto_sheet.write('D1','Price')
crypto_sheet.write('E1','24H Volume')
crypto_sheet.write('F1','Hour Change')
crypto_sheet.write('G1','Day Change')
crypto_sheet.write('H1','Week Change')

for i in range(10):
        listings_url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': '5233ea6b-e6f7-41c8-8926-857a768ce7f8',
        }
        parameters = {
          'start':start,
        }
        session = Session()
        session.headers.update(headers)
        response = session.get(listings_url, params=parameters)
        results = json.loads(response.text)
        data=results['data']
        for currency in data:
            rank=currency['cmc_rank']
            name=currency['name']
            symbol=currency['symbol']

            quotes=currency['quote']['USD']
            market_cap=quotes['market_cap']
            hour_change=quotes['percent_change_1h']
            day_change=quotes['percent_change_24h']
            week_change=quotes['percent_change_7d']
            price=quotes['price']
            volume=quotes['volume_24h']

            crypto_sheet.write(f,0,name)
            crypto_sheet.write(f,1,symbol)
            crypto_sheet.write(f,2,str(int(market_cap)))
            crypto_sheet.write(f,3,str(int(price)))
            crypto_sheet.write(f,4,str(int(volume)))
            crypto_sheet.write(f,5,str(int(hour_change)))
            crypto_sheet.write(f,6,str(int(day_change)))
            crypto_sheet.write(f,7,str(int(week_change)))

            f+=1

        start=100

crypto_workbook.close()
