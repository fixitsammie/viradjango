
import requests
import random

import time
import pytz
import datetime
from dateutil.parser import parse
import sys

#from urllib.request import urlopen, Request
import json
import requests_cache
requests_cache.install_cache('test_cache', backend='sqlite', expire_after=300)

from .models import Ticker,Pair,Exchange 
from django.http import JsonResponse

def bifi_build(interval,pair):
    return "https://api.bitfinex.com/v2/candles/trade:{0}:t{1}/hist".format(interval,pair.upper())

def r(coin):
    url=bifi_build('1D',coin)
    try:
        response=requests.get(url).json()
    except:
        time.sleep(random.randint(45,55))
        try:
            response=requests.get(url).json()
        except:
            raise TimeoutError("cant get candles from bitfinex")
    return response

mk1=['btcusd', 'ltcusd', 'ltcbtc', 'ethusd', 'ethbtc', 'etcbtc', 'etcusd', 'rrtusd', 'rrtbtc', 'zecusd', 'zecbtc', 'xmrusd', 'xmrbtc', 'dshusd', 'dshbtc', 'btceur', 'xrpusd', 'xrpbtc', 'iotusd', 'iotbtc', 'ioteth', 'eosusd', 'eosbtc', 'eoseth', 'sanusd', 'sanbtc', 'saneth']
mk2=[ 'sntbtc', 'snteth', 'ioteur', 'batusd', 'batbtc', 'bateth', 'mnausd', 'mnabtc', 'mnaeth', 'funusd', 'funbtc', 'funeth', 'zrxusd', 'zrxbtc', 'zrxeth' , 'omgusd', 'omgbtc', 'omgeth', 'bchusd', 'bchbtc', 'bcheth', 'neousd', 'neobtc', 'neoeth', 'etpusd', 'etpbtc', 'etpeth']
mk3=['tnbusd', 'tnbbtc', 'tnbeth', 'spkusd', 'spkbtc', 'spketh', 'trxusd', 'trxbtc', 'trxeth', 'rcnusd', 'rcnbtc', 'rcneth', 'rlcusd', 'rlcbtc', 'rlceth', 'aidusd', 'aidbtc', 'aideth', 'sngusd', 'sngbtc', 'sngeth', 'repusd', 'repbtc', 'repeth', 'elfusd', 'elfbtc', 'elfeth']
mk4=['qtmusd', 'qtmbtc', 'qtmeth', 'avtusd', 'avtbtc', 'avteth', 'edousd', 'edobtc', 'edoeth', 'btgusd', 'btgbtc', 'datusd', 'datbtc', 'dateth', 'qshusd', 'qshbtc', 'qsheth', 'yywusd', 'yywbtc', 'yyweth', 'gntusd', 'gntbtc', 'gnteth', 'sntusd']



#mkt9=[mkt1,mkt2,mkt3,mkt4]
#mkt9=[mkt1]
mkt9=[['ethusd']]

from dateutil import tz,parser
default_date=datetime.datetime.combine(datetime.datetime.now(), datetime.time(0,tzinfo=tz.gettz("America/New_York")))

def bit_fix(coin):
	name=coin[0:3]+"-"+coin[3:]
	name=name.upper()
	return name





def bitfinex_download(request):
	exchange_name='Bitfinex'
	try:
		exchange=Exchange.objects.get(name=exchange_name)
	except:
		Exchange(name=exchange_name).save()
		exchange=Exchange.objects.get(name=exchange_name)
		
	response_dict={}
	for mkt in mkt9:
		for current_pair in mkt:
			first_coin=current_pair
			if r(first_coin):
				bit_fix_name=bit_fix(first_coin)
				try:
					pair=Pair.objects.get(name=bit_fix_name)
				except:
					Pair(name=bit_fix_name,exchange=exchange).save()
					pair=Pair.objects.get(name=bit_fix_name,exchange=exchange)
				added=0
				for candle in r(first_coin):
					print(candle[0])
					_time=candle[0]/1000
					candle_ticker_updated=datetime.datetime.fromtimestamp(int(_time),tz=pytz.utc)
					candle_ticker_time=str(candle[0])
					candle_ticker_open=candle[1]
					candle_ticker_close=candle[2]
					candle_ticker_high=candle[3]
					candle_ticker_low=candle[4]
					candle_ticker_volume=candle[5]
					candle_ticker_ordinary_volume=candle[5]
					
					if not Ticker.objects.filter(pair=pair,ticker_time=candle_ticker_time,ticker_updated_time=candle_ticker_updated).exists():
						ticker=Ticker(pair=pair,
										ticker_open=candle_ticker_open,
										ticker_close=candle_ticker_close,
										ticker_volume=candle_ticker_ordinary_volume,
										ticker_low=candle_ticker_low,
										ticker_high=candle_ticker_high,
										ticker_bulk_volume=candle_ticker_volume*candle_ticker_open,
										ticker_time=candle_ticker_time,
										ticker_updated_time=candle_ticker_updated
										)
						ticker.save()
						added=added+1
					    
				response_dict[bit_fix_name]='Success : Added {} new {} pairs'.format(added,bit_fix_name)
				print('Added {} new {} pairs'.format(added,first_coin))	
			else:
				response_dict[bit_fix_name]='error'
		time.sleep(10)
	
	return JsonResponse(response_dict)	
