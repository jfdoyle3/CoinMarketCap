import json
import requests

global_url='https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

request=requests.get(global_url)
results=request.json()

print(json.dumps(results, sort_keys=True, indent=4))
