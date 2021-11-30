import requests
from config import authkey
date = []
open = []
high = []
low = []
close = []
volume = []

def list_stocks(ticker,timeframe,timeinterval):
    auth = requests.get('https://financialmodelingprep.com/api/v4/historical-price/{}/{}/{}?apikey={}'.format(ticker,timeframe,timeinterval,authkey))
    fmp = auth.json()
    for x in range(len(fmp['results'])):
        date.append(fmp['results'][x]['formated'])
        open.append(fmp['results'][x]['o'])
        high.append(fmp['results'][x]['h'])
        low.append(fmp['results'][x]['l'])
        close.append(fmp['results'][x]['c'])
        volume.append(fmp['results'][x]['v'])