"""This file is responsible for saving binance data to the database"""

import requests
import pytz
import time
import datetime
import sys
from dateutil.parser import parse
import random
#from urllib.request import urlopen, Request
import json

import requests_cache
requests_cache.install_cache('test_cache', backend='sqlite', expire_after=300)

from .models import Ticker,Pair,Exchange 
from django.http import JsonResponse
mkt1=['ETHBTC', 'LTCBTC', 'BNBBTC']
#mkt9=[mkt1,mkt2,mkt3,mkt4]
mkt9=[mkt1]
#mkt9=[['BTC-PAY', 'USD-BTC']]



from dateutil import tz,parser
default_date=datetime.datetime.combine(datetime.datetime.now(), datetime.time(0,tzinfo=tz.gettz("America/New_York")))

from binance.client import Client
binance_api_key='CUH2llyqro5IZ5xYXUsNjrrUZZq2VKPbqXJ9qJAj5iTpRVkpTXiTjj57g88tkXXJ'
binance_api_secret='NPwVZjuZzpk9lXvdpWT1GxHlkxIAQCoh2spIkl7Pl8qPBz7qkPimn5xQDgirwc9z'
client = Client(binance_api_key, binance_api_secret)

def bit_fix(coin):
	name=coin[0:3]+"-"+coin[3:]
	name=name.upper()
	return name






def binance_download(request):
	exchange_name='Binance'
	try:
		exchange=Exchange.objects.get(name=exchange_name)
	except:
		Exchange(name=exchange_name).save()
		exchange=Exchange.objects.get(name=exchange_name)
		
	response_dict={}
	for mkt in mkt9:
		for current_pair in mkt:
			first_coin=current_pair
			try:
			    klines = client.get_historical_klines(current_pair, Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017")
			except:
				klines=None
			if klines:
				bit_fix_name=bit_fix(first_coin)
				try:
					pair=Pair.objects.get(name=bit_fix_name)
				except:
					Pair(name=bit_fix_name,exchange=exchange).save()
					pair=Pair.objects.get(name=bit_fix_name,exchange=exchange)
				added=0
				for candle in klines:
					_time=candle[0]/1000
					candle_ticker_updated=datetime.datetime.fromtimestamp(int(_time),tz=pytz.utc)
					candle_ticker_time=str(_time)
					candle_ticker_open=candle[1]
					candle_ticker_close=candle[4]
					candle_ticker_high=candle[2]
					candle_ticker_low=candle[3]
					candle_ticker_volume=candle[5]
					candle_ticker_ordinary_volume=candle[5]
					print(candle_ticker_time)
					print(type(candle_ticker_time))
					if not Ticker.objects.filter(pair=pair,ticker_time=candle_ticker_time,ticker_updated_time=candle_ticker_updated).exists():
						ticker=Ticker(pair=pair,
										ticker_open=candle_ticker_open,
										ticker_close=candle_ticker_close,
										ticker_volume=candle_ticker_ordinary_volume,
										ticker_low=candle_ticker_low,
										ticker_high=candle_ticker_high,
										ticker_bulk_volume=candle_ticker_volume,
										ticker_time=candle_ticker_time,
										ticker_updated_time=candle_ticker_updated
										)
						ticker.save()
						added=added+1
					    
				response_dict[current_pair]='Success : Added {} new {} pairs'.format(added,first_coin)
				print('Added {} new {} pairs'.format(added,first_coin))	
			else:
				response_dict[current_pair]='error'
		time.sleep(10)
	
	return JsonResponse(response_dict)	