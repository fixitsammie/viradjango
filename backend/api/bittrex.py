import requests
import pytz
import time
import datetime
import sys
from dateutil.parser import parse
import pandas as pd
import random
from urllib.request import urlopen, Request
import json
import numpy as np
from numpy import array_split
import requests_cache
requests_cache.install_cache('test_cache', backend='sqlite', expire_after=300)

mkt1=('BTC-LTC', 'BTC-DOGE', 'BTC-VTC', 'BTC-PPC', 'BTC-FTC', 'BTC-RDD', 'BTC-NXT', 'BTC-DASH', 'BTC-POT', 'BTC-BLK', 'BTC-EMC2', 'BTC-XMY', 'BTC-AUR', 'BTC-EFL', 'BTC-GLD', 'BTC-SLR', 'BTC-PTC', 'BTC-GRS', 'BTC-NLG', 'BTC-RBY', 'BTC-XWC', 'BTC-MONA', 'BTC-THC', 'BTC-ENRG', 'BTC-ERC', 'BTC-VRC', 'BTC-CURE', 'BTC-XMR', 'BTC-CLOAK', 'BTC-START', 'BTC-KORE', 'BTC-XDN', 'BTC-TRUST', 'BTC-NAV', 'BTC-XST', 'BTC-BTCD', 'BTC-VIA', 'BTC-PINK', 'BTC-IOC', 'BTC-CANN', 'BTC-SYS', 'BTC-NEOS', 'BTC-DGB', 'BTC-BURST', 'BTC-EXCL', 'BTC-SWIFT', 'BTC-DOPE', 'BTC-BLOCK', 'BTC-ABY', 'BTC-BYC', 'BTC-XMG', 'BTC-BLITZ', 'BTC-BAY', 'BTC-FAIR', 'BTC-SPR', 'BTC-VTR', 'BTC-XRP', 'BTC-GAME', 'BTC-COVAL', 'BTC-NXS', 'BTC-XCP', 'BTC-BITB', 'BTC-GEO', 'BTC-FLDC', 'BTC-GRC', 'BTC-FLO', 'BTC-NBT', 'BTC-MUE')
mkt2=('BTC-XEM', 'BTC-CLAM', 'BTC-DMD', 'BTC-GAM', 'BTC-SPHR', 'BTC-OK', 'BTC-SNRG', 'BTC-PKB', 'BTC-CPC', 'BTC-AEON', 'BTC-ETH', 'BTC-GCR', 'BTC-TX', 'BTC-BCY', 'BTC-EXP', 'BTC-INFX', 'BTC-OMNI', 'BTC-AMP', 'BTC-AGRS', 'BTC-XLM', 'USDT-BTC', 'BTC-CLUB', 'BTC-VOX', 'BTC-EMC', 'BTC-FCT', 'BTC-MAID', 'BTC-EGC', 'BTC-SLS', 'BTC-RADS', 'BTC-DCR', 'BTC-BSD', 'BTC-XVG', 'BTC-PIVX', 'BTC-XVC', 'BTC-MEME', 'BTC-STEEM', 'BTC-2GIVE', 'BTC-LSK', 'BTC-PDC', 'BTC-BRK', 'BTC-DGD', 'ETH-DGD', 'BTC-WAVES', 'BTC-RISE', 'BTC-LBC', 'BTC-SBD', 'BTC-BRX', 'BTC-ETC', 'ETH-ETC', 'BTC-STRAT', 'BTC-UNB', 'BTC-SYNX', 'BTC-TRIG', 'BTC-EBST', 'BTC-VRM', 'BTC-SEQ', 'BTC-REP', 'BTC-SHIFT', 'BTC-ARDR', 'BTC-XZC', 'BTC-NEO', 'BTC-ZEC', 'BTC-ZCL', 'BTC-IOP', 'BTC-GOLOS', 'BTC-UBQ', 'BTC-KMD', 'BTC-GBG')
mkt3=('BTC-SIB', 'BTC-ION', 'BTC-LMC', 'BTC-QWARK', 'BTC-CRW', 'BTC-SWT', 'BTC-MLN', 'BTC-ARK', 'BTC-DYN', 'BTC-TKS', 'BTC-MUSIC', 'BTC-DTB', 'BTC-INCNT', 'BTC-GBYTE', 'BTC-GNT', 'BTC-NXC', 'BTC-EDG', 'BTC-LGD', 'BTC-TRST', 'ETH-GNT', 'ETH-REP', 'USDT-ETH', 'ETH-WINGS', 'BTC-WINGS', 'BTC-RLC', 'BTC-GNO', 'BTC-GUP', 'BTC-LUN', 'ETH-GUP', 'ETH-RLC', 'ETH-LUN', 'ETH-GNO', 'BTC-APX', 'BTC-HMQ', 'ETH-HMQ', 'BTC-ANT', 'ETH-TRST', 'ETH-ANT', 'BTC-SC', 'ETH-BAT', 'BTC-BAT', 'BTC-ZEN', 'BTC-1ST', 'BTC-QRL', 'ETH-1ST', 'ETH-QRL', 'BTC-CRB', 'ETH-CRB', 'ETH-LGD', 'BTC-PTOY', 'ETH-PTOY', 'BTC-MYST', 'ETH-MYST', 'BTC-CFI', 'ETH-CFI', 'BTC-BNT', 'ETH-BNT', 'BTC-NMR', 'ETH-NMR', 'ETH-LTC', 'ETH-XRP', 'BTC-SNT', 'ETH-SNT', 'BTC-DCT', 'BTC-XEL', 'BTC-MCO', 'ETH-MCO', 'BTC-ADT')
mkt4=('ETH-ADT', 'BTC-FUN', 'ETH-FUN', 'BTC-PAY', 'ETH-PAY', 'BTC-MTL', 'ETH-MTL', 'BTC-STORJ', 'ETH-STORJ', 'BTC-ADX', 'ETH-ADX', 'ETH-DASH', 'ETH-SC', 'ETH-ZEC', 'USDT-ZEC', 'USDT-LTC', 'USDT-ETC', 'USDT-XRP', 'BTC-OMG', 'ETH-OMG', 'BTC-CVC', 'ETH-CVC', 'BTC-PART', 'BTC-QTUM', 'ETH-QTUM', 'ETH-XMR', 'ETH-XEM', 'ETH-XLM', 'ETH-NEO', 'USDT-XMR', 'USDT-DASH', 'ETH-BCC', 'USDT-BCC', 'BTC-BCC', 'BTC-DNT', 'ETH-DNT', 'USDT-NEO', 'ETH-WAVES', 'ETH-STRAT', 'ETH-DGB', 'ETH-FCT', 'USDT-OMG', 'BTC-ADA', 'BTC-MANA', 'ETH-MANA', 'BTC-SALT', 'ETH-SALT', 'BTC-TIX', 'ETH-TIX', 'BTC-RCN', 'ETH-RCN', 'BTC-VIB', 'ETH-VIB', 'BTC-MER', 'BTC-POWR', 'ETH-POWR', 'BTC-BTG', 'ETH-BTG', 'USDT-BTG', 'ETH-ADA', 'BTC-ENG', 'ETH-ENG', 'USDT-ADA', 'USDT-XVG', 'USDT-NXT', 'BTC-UKG', 'ETH-UKG')

def build_address(pair):
    address='https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName={0}&tickInterval=oneMin&_=1499127220008'.format(pair)
    return address

    
def strtime(date):
    d=datetime.datetime.fromtimestamp(int(date),tz=pytz.utc).strftime('%Y.%m.%d')
    return d

def r(coin):
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


def multi_down(mkt,filename):
    mkt=tuple([coin for coin in mkt if r(coin)['success']])
    global df
    df=pd.DataFrame([pd.Series(np.array([candle['O'] for candle in r(coin)['result']]),
              index=np.array([parse(candle['T']).date().isoformat().replace('-','.') for candle in r(coin)['result']])) for coin in mkt if r(coin)['success'] ],index=mkt)
    df=df.transpose()
    dc=pd.DataFrame([pd.Series(np.array([candle['C'] for candle in r(coin)['result']]),
              index=np.array([parse(candle['T']).date().isoformat().replace('-','.') for candle in r(coin)['result']])) for coin in mkt if r(coin)['success'] ],index=mkt)
    dc=dc.transpose()
    dv=pd.DataFrame([pd.Series(np.array([candle['BV'] for candle in r(coin)['result']]),
              index=np.array([parse(candle['T']).date().isoformat().replace('-','.') for candle in r(coin)['result']])) for coin in mkt if r(coin)['success'] ],index=mkt)
    dv=dv.transpose()
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,'Open')
    dc.to_excel(writer,'Close')
    dv.to_excel(writer,'Volume')
    writer.save()

multi_down(mkt=mkt1,filename="mkt1.xlsx")
multi_down(mkt=mkt2,filename="mkt2.xlsx")
multi_down(mkt=mkt3,filename="mkt3.xlsx")
multi_down(mkt=mkt4,filename="mkt4.xlsx")
#multi_down(mkt=mkt1,filename="mkt1.xlsx")
#this is how to stop an excel file from running
print('done')
