
import requests
import pandas as pd
import numpy as np
import time
import random

import requests_cache
requests_cache.install_cache('test_cache', backend='sqlite', expire_after=300)

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

def multi_down(symbols,filename):
	df=pd.DataFrame([pd.Series(np.array([candle[2] for candle in r(coin)]),
	                           index=np.array([pd.to_datetime(candle[0],unit='ms').date().isoformat().replace('-','.')
	                                           for candle in r(coin)] )) for coin in symbols],index=symbols)
	dg=pd.DataFrame([pd.Series(np.array([candle[5] for candle in r(coin)]),
	                           index=np.array([pd.to_datetime(candle[0],unit='ms').date().isoformat().replace('-','.')
	                                           for candle in r(coin)] )) for coin in symbols],index=symbols)   
	                
	df=df.transpose()
	dg=dg.transpose()
	writer = pd.ExcelWriter(filename)
	df.to_excel(writer,'Close')
	dg.to_excel(writer,'Volume')
	writer.save()
    

multi_down(symbols=mk1,filename="BFX1.xlsx")
multi_down(symbols=mk2,filename="BFX2.xlsx")
multi_down(symbols=mk3,filename="BFX3.xlsx")
multi_down(symbols=mk4,filename="BFX4.xlsx")
print('done')
