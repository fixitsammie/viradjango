"""This file is responsible for saving bittrex data to the database"""

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
from .bulk_creator import BulkCreateManager
mkt1=['BTC-LTC', 'BTC-DOGE', 'BTC-VTC', 'BTC-PPC', 'BTC-FTC', 'BTC-RDD', 'BTC-NXT', 'BTC-DASH', 'BTC-POT', 'BTC-BLK', 'BTC-EMC2', 'BTC-XMY', 'BTC-AUR', 'BTC-EFL', 'BTC-GLD', 'BTC-SLR', 'BTC-PTC', 'BTC-GRS', 'BTC-NLG', 'BTC-RBY', 'BTC-XWC', 'BTC-MONA', 'BTC-THC', 'BTC-ENRG', 'BTC-ERC', 'BTC-VRC', 'BTC-CURE', 'BTC-XMR', 'BTC-CLOAK', 'BTC-START', 'BTC-KORE', 'BTC-XDN', 'BTC-TRUST', 'BTC-NAV', 'BTC-XST', 'BTC-BTCD', 'BTC-VIA', 'BTC-PINK', 'BTC-IOC', 'BTC-CANN', 'BTC-SYS', 'BTC-NEOS', 'BTC-DGB', 'BTC-BURST', 'BTC-EXCL', 'BTC-SWIFT', 'BTC-DOPE', 'BTC-BLOCK', 'BTC-ABY', 'BTC-BYC', 'BTC-XMG', 'BTC-BLITZ', 'BTC-BAY', 'BTC-FAIR', 'BTC-SPR', 'BTC-VTR', 'BTC-XRP', 'BTC-GAME', 'BTC-COVAL', 'BTC-NXS', 'BTC-XCP', 'BTC-BITB', 'BTC-GEO', 'BTC-FLDC', 'BTC-GRC', 'BTC-FLO', 'BTC-NBT', 'BTC-MUE']
mkt2=['BTC-XEM', 'BTC-CLAM', 'BTC-DMD', 'BTC-GAM', 'BTC-SPHR', 'BTC-OK', 'BTC-SNRG', 'BTC-PKB', 'BTC-CPC', 'BTC-AEON', 'BTC-ETH', 'BTC-GCR', 'BTC-TX', 'BTC-BCY', 'BTC-EXP', 'BTC-INFX', 'BTC-OMNI', 'BTC-AMP', 'BTC-AGRS', 'BTC-XLM', 'USDT-BTC', 'BTC-CLUB', 'BTC-VOX', 'BTC-EMC', 'BTC-FCT', 'BTC-MAID', 'BTC-EGC', 'BTC-SLS', 'BTC-RADS', 'BTC-DCR', 'BTC-BSD', 'BTC-XVG', 'BTC-PIVX', 'BTC-XVC', 'BTC-MEME', 'BTC-STEEM', 'BTC-2GIVE', 'BTC-LSK', 'BTC-PDC', 'BTC-BRK', 'BTC-DGD', 'ETH-DGD', 'BTC-WAVES', 'BTC-RISE', 'BTC-LBC', 'BTC-SBD', 'BTC-BRX', 'BTC-ETC', 'ETH-ETC', 'BTC-STRAT', 'BTC-UNB', 'BTC-SYNX', 'BTC-TRIG', 'BTC-EBST', 'BTC-VRM', 'BTC-SEQ', 'BTC-REP', 'BTC-SHIFT', 'BTC-ARDR', 'BTC-XZC', 'BTC-NEO', 'BTC-ZEC', 'BTC-ZCL', 'BTC-IOP', 'BTC-GOLOS', 'BTC-UBQ', 'BTC-KMD', 'BTC-GBG']
mkt3=['BTC-SIB', 'BTC-ION', 'BTC-LMC', 'BTC-QWARK', 'BTC-CRW', 'BTC-SWT', 'BTC-MLN', 'BTC-ARK', 'BTC-DYN', 'BTC-TKS', 'BTC-MUSIC', 'BTC-DTB', 'BTC-INCNT', 'BTC-GBYTE', 'BTC-GNT', 'BTC-NXC', 'BTC-EDG', 'BTC-LGD', 'BTC-TRST', 'ETH-GNT', 'ETH-REP', 'USDT-ETH', 'ETH-WINGS', 'BTC-WINGS', 'BTC-RLC', 'BTC-GNO', 'BTC-GUP', 'BTC-LUN', 'ETH-GUP', 'ETH-RLC', 'ETH-LUN', 'ETH-GNO', 'BTC-APX', 'BTC-HMQ', 'ETH-HMQ', 'BTC-ANT', 'ETH-TRST', 'ETH-ANT', 'BTC-SC', 'ETH-BAT', 'BTC-BAT', 'BTC-ZEN', 'BTC-1ST', 'BTC-QRL', 'ETH-1ST', 'ETH-QRL', 'BTC-CRB', 'ETH-CRB', 'ETH-LGD', 'BTC-PTOY', 'ETH-PTOY', 'BTC-MYST', 'ETH-MYST', 'BTC-CFI', 'ETH-CFI', 'BTC-BNT', 'ETH-BNT', 'BTC-NMR', 'ETH-NMR', 'ETH-LTC', 'ETH-XRP', 'BTC-SNT', 'ETH-SNT', 'BTC-DCT', 'BTC-XEL', 'BTC-MCO', 'ETH-MCO', 'BTC-ADT']
mkt4=['ETH-ADT', 'BTC-FUN', 'ETH-FUN', 'BTC-PAY', 'ETH-PAY', 'BTC-MTL', 'ETH-MTL', 'BTC-STORJ', 'ETH-STORJ', 'BTC-ADX', 'ETH-ADX', 'ETH-DASH', 'ETH-SC', 'ETH-ZEC', 'USDT-ZEC', 'USDT-LTC', 'USDT-ETC', 'USDT-XRP', 'BTC-OMG', 'ETH-OMG', 'BTC-CVC', 'ETH-CVC', 'BTC-PART', 'BTC-QTUM', 'ETH-QTUM', 'ETH-XMR', 'ETH-XEM', 'ETH-XLM', 'ETH-NEO', 'USDT-XMR', 'USDT-DASH', 'ETH-BCC', 'USDT-BCC', 'BTC-BCC', 'BTC-DNT', 'ETH-DNT', 'USDT-NEO', 'ETH-WAVES', 'ETH-STRAT', 'ETH-DGB', 'ETH-FCT', 'USDT-OMG', 'BTC-ADA', 'BTC-MANA', 'ETH-MANA', 'BTC-SALT', 'ETH-SALT', 'BTC-TIX', 'ETH-TIX', 'BTC-RCN', 'ETH-RCN', 'BTC-VIB', 'ETH-VIB', 'BTC-MER', 'BTC-POWR', 'ETH-POWR', 'BTC-BTG', 'ETH-BTG', 'USDT-BTG', 'ETH-ADA', 'BTC-ENG', 'ETH-ENG', 'USDT-ADA', 'USDT-XVG', 'USDT-NXT', 'BTC-UKG', 'ETH-UKG']

#mkt9=[mkt1,mkt2,mkt3,mkt4]
mkt9=[mkt1]
def build_address(pair):
    address='https://international.bittrex.com/Api/v2.0/pub/market/GetTicks?_=149912722000&marketName={0}&tickInterval=day'.format(pair)
    return address

    
def strtime(date):
    d=datetime.datetime.fromtimestamp(int(date),tz=pytz.utc).strftime('%Y.%m.%d')
    return d

def sr(coin):
    url=build_address(coin)
    try:
        response = requests.get(url).json()
    except:
        time.sleep(random.randint(15, 25))
        try: 
            response = requests.get(url).json()
        except:
            raise TimeoutError("cant get candles from trex")
    return response

def r(coin):
    url=build_address(coin)
    response = requests.get(url).json()
    if response:
        print('good')
    else:
        print('bad')
        raise TimeoutError('cant get candles')
    return response
    

"""
import numpy as np
from numpy import array_split
import pandas as pd
"""

from dateutil import tz,parser
default_date=datetime.datetime.combine(datetime.datetime.now(), datetime.time(0,tzinfo=tz.gettz("America/New_York")))



exchange_name='Bittrex'
try:
	exchange=Exchange.objects.get(name=exchange_name)
except:
	Exchange(name=exchange_name).save()
	exchange=Exchange.objects.get(name=exchange_name)



	
def bittrex_download(request):
	response_dict={}
	bulk_mgr = BulkCreateManager(chunk_size=1000)
	for mkt in mkt9:
		for current_pair in mkt:
			first_coin=current_pair
			if r(first_coin)['success']:
				try:
					pair=Pair.objects.get(name=first_coin)
				except:
					Pair(name=first_coin,exchange=exchange).save()
					pair=Pair.objects.get(name=first_coin,exchange=exchange)
				for candle in r(first_coin)['result']:
					candle_ticker_updated=parse(candle['T'],default=default_date)
					candle_ticker_time=candle['T']
					candle_ticker_open=candle['O']
					candle_ticker_close=candle['C']
					candle_ticker_high=candle['H']
					candle_ticker_low=candle['L']
					candle_ticker_volume=candle['BV']
					candle_ticker_ordinary_volume=candle['V']
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
					bulk_mgr.add(ticker)
					print('{} added one of them'.format(first_coin))
					#ticks.append(ticker)
					#ticker.save()
					#Ticker.objects.bulk_create(ticks)
				response_dict[current_pair]='success'
			else:
				response_dict[current_pair]='error'
		time.sleep(10)
	bulk_mgr.done()
	print(response_dict)
	return JsonResponse(response_dict)

#get a link that updates the data every midnight
#dashboard that shows health of everybody
#write a function that will sleep for 30 minutes before requesting for the second mkt etc