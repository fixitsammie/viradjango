from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer,Ticker,Pair,Exchange

import time
# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


from django.shortcuts import render
import json

from django.http import JsonResponse

from .bittrex_data import data_load
#from .bittrex_main import data_load
from .test_data import inside
from .out import outside
        


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

#@csrf_exempt
#@api_view(["GET"])
def spill_data(request):
    response_data = {
            "success": "true",
            "message": "",
            "result": [
            {
            "y": 2,
            "x": 3,
            },
            {
            "x": 3,
            "y": 5,
            },
            {
            "x": 5,
            "y": 7,
            }]}
    response_data['message'] = 'Some error message'
    response_data=data_load
    
    return JsonResponse(response_data)
    #return Response(response_data, status=HTTP_200_OK)


#@csrf_exempt
#@api_view(["GET"])
def udf_config(request):
    response= {"supports_search": True,
                "supports_group_request": False,
                "supports_marks": False,
                "supports_timescale_marks": False,
                "supports_time": True,
                "exchanges": [
                {
                "value": "BTC-VTC",
                "name": "Bittrex",
                "desc": "Bittrex"
                },
                {
                "value": "Bittrex",
                "name": "Bittrex",
                "desc": "Bittrex"
                },
                {
                "value": "Bitfinex",
                "name": "Bitfinex",
                "desc": "Bitfinex"
                },
                {
                "value": "Binance",
                "name": "Binance",
                "desc": "Binance"
                }
                ],
                "symbols_types": [
               
                
                {
                 "name": "Bitcoin",
                "value": "bitcoin"
                }
                ],
                "supported_resolutions": [
                 "D",
                "2D",
                "3D",
                "W",
                "3W",
                "M",
                "6M"
                ]}
    return JsonResponse(response)

def symbol_resolve(request):
    symbol=request.GET['symbol']
    symbol_split=symbol.split(':')
    try:
        exchange=symbol_split[1]
    except:
        exchange=''
    the_symbol=symbol_split[0]
    the_symbol_full=symbol
    
    symbol={
        'name': the_symbol_full,
        'exchange-traded': the_symbol,
        'exchange-listed': the_symbol,
        'timezone': 'America/New_York',
        'minmov': 1,
        'minmov2': 0,
        'pointvalue': 1,
        'session': '24x7',
        'has_intraday': True,
        'has_no_volume': False,
        'description': the_symbol,
        'type': 'bitcoin',
        'supported_resolutions': [
       
        'D',
        '2D',
        '3D',
        'W',
        '3W',
        'M',
        '6M'
        ],
        'pricescale': '100',
        'ticker': the_symbol_full
        }
    response={'symbol':symbol}
    return JsonResponse(symbol)

def symbol_info(request):
    group=request.GET['group']
    symbol={
        'symbol': ["BTC","ALAPL", "MSFT", "SPX"],
        'description': ["Bitcoin","Apple Inc", "Microsoft corp", "S&P 500 index"],
        'exchange-listed': "NYSE",
        'exchange-traded': "NYSE",
        'minmovement': 1,
        'minmovement2': 0,
        'pricescale': [1,1, 1, 100],
        'has-dwm': True,
        'has-intraday': True,
        'has-no-volume': [False,False, False, True],
        'type': ["bitcoin","stock", "stock", "index"],
        'ticker': ["BTCUSD","AASPL~0", "MSFT~0", "$SPX500"],
        'timezone': "America/New_York",
        'session-regular': "0900-1600",
        }
    if group=='NYSE':
        print('NYSE')
        symbol['type']=["stock","stock","stock","stock"]
    elif group=='FOREX':
        symbol['type']=["stock","stock","stock","stock"]
        print('FX')
    else:
        print('gbabe')
        symbol['type']=["stock","stock","stock","stock"]
    symbol={
        'symbol': ["BTC","ALAPL", "MSFT", "SPX"],
        'description': ["Bitcoin","Apple Inc", "Microsoft corp", "S&P 500 index"],
        'exchange-listed': "NYSE",
        'exchange-traded': "NYSE",
        'minmovement': 1,
        'minmovement2': 0,
        'pricescale': [1,1, 1, 100],
        'has-dwm': True,
        'has-intraday': True,
        'has-no-volume': [False,False, False, True],
        'type': ["bitcoin","stock", "stock", "index"],
        'ticker': ["USDT-BTC","AASPL~0", "MSFT~0", "$SPX500"],
        'timezone': "America/New_York",
        'session-regular': "24x7",
        }
    response={'symbol':symbol}
    return JsonResponse(symbol)

def symbol_info23(request):
    symbol=request.GET['symbol']
    symbol={
        "name": "USDBTC",
        "exchange-traded": "Bitrex",
        "exchange-listed": "Bitrex",
        "timezone": "America/New_York",
        "minmov": 1,
        "minmov2": 0,
        "pointvalue": 0.0001,
        "session": "24x7",
        "has_intraday": False,
        "has_no_volume": False,
        "description": "Bittrex",
        "type": "bitcoin",
        "supported_resolutions": [
        "1", "15", "240",
        "D",
        "2D",
        "3D",
        "W",
        "3W",
        "M",
        "6M"
        ],
        "pricescale": 10000,
        "ticker": "USDT-BTC:Bittrex"}
    response={'symbol':symbol}
    return JsonResponse(response)
def symbol_search(request):
    query=request.GET['query']
    exchange=request.GET['exchange']
    symbol_type=request.GET['type']
    limit=request.GET['limit']
    response=[{
"symbol": "AZO",
"full_name": "AZO",
"description": "AutoZone, Inc.",
"exchange": "Bittrex",
"ticker":"AZO",
"type": "bitcoin"
}
    ]
    response={'symbol':str(query)}
    return JsonResponse(response)
from datetime import datetime
from django.utils import timezone


def get_bars(request):
    symbol=request.GET['symbol']
    symbol_split=symbol.split(':')
    if len(symbol_split)==2:
        symbol_name=symbol_split[0]
        exchange_name=symbol_split[1]
    #TODO handle if only one symbol is sent
    time_from=request.GET['from']
    time_to=request.GET['to']
    try:
        dt_time_from=datetime.fromtimestamp(int(time_from))
    except:
        if(int(time_from))<0:
            dt_time_from=datetime(2000,1,1)
        else:
            dt_time_from=datetime(3000,1,1)
    try:
        dt_time_to=datetime.fromtimestamp(int(time_to))
    except:
        if(int(time_to))<0:
            dt_time_to=datetime(2000,1,1)
        else:
            dt_time_to=datetime(3000,1,1)
    dt_time_from= timezone.make_aware(dt_time_from, timezone.get_current_timezone())
    dt_time_to=timezone.make_aware(dt_time_to, timezone.get_current_timezone())
    try:
        pair=Pair.objects.get(name=str(symbol_name))
    except:
        pair=None
    print(pair)
    resolution=request.GET['resolution']
    print("{0},{1},{2}".format(time_from,time_to,resolution))
    if pair:
        b=Ticker.objects.filter(pair=pair,ticker_updated_time__gte=dt_time_from).filter(ticker_updated_time__lte=dt_time_to)
    else:
        b=[]
    t=[]
    c=[]
    o=[]
    h=[]
    l=[]
    v=[]

    for i in b:
        t.append(int(time.mktime(i.ticker_updated_time.timetuple())))
        c.append(float(i.ticker_close))
        o.append(float(i.ticker_open))
        h.append(float(i.ticker_high))
        l.append(float(i.ticker_low))
        v.append(float(i.ticker_volume))

    response={}
    if not b:
        response['s']='nodata'
        response['nextTime']: 1426118400
        #TODO add next time variable
    else:
        response={
           's': "ok",
           't': t,
           'c': c,
           'o': o,
           'h': h,
           'l': l,
           'v': v}
    #response=data_load['result']
    return JsonResponse(response,safe=False)
'''
if dt_time_from < smallest time record:
    next_time=smallest_record
else if dt_time_from > smallest time record and dt_time_to<largest time
    next_time=current_time+one day
else:
    next_time=largest time
'''

def get_server_time(request):
    import time
    current_time=int(time.time())
    response={'time':str(current_time)}
    return JsonResponse(response)


def get_all_exchanges(request):
    a=Exchange.objects.all()
    b=[]
    for i in a:
         pairs=Pair.objects.filter(exchange=i)
         pairs_=[j.name for j in pairs]
         exch_={'name':i.name,'pairs':pairs_}
         b.append(exch_)
    response={'exchanges':[{'name':'Bittrex','pairs':['BTCUSD','FETSDS']},{'name':'Poloniex','pairs':['BTUSD','XETSDS']}]}
    response={'exchanges':b}
    return JsonResponse(response)


'''
if dt_time_from < smallest time record:
    next_time=smallest_record
else if dt_time_from > smallest time record and dt_time_to<largest time
    next_time=current_time+one day
else:
    next_time=largest time
'''

from django.http import Http404
def react_get_bars_r(request):
    exchange=request.GET['e']
    fsym=request.GET['fsym']
    tsym=request.GET['tsym']
    toTs=request.GET['toTs']
    limit=request.GET['limit']
    pair_name="{}-{}".format(fsym,tsym)
    response={}
    pair=None
    try:
        exch=Exchange.objects.get(name=exchange)
    except Exchange.DoesNotExist:
        exch=None
        response['s']='nodata'
    if exch:
        try:
            pair=Pair.objects.get(name=pair_name,exchange=exch)
        except Pair.DoesNotExist:
            pair=None
            response['s']='nodata'
            
    
    time_to=toTs
    try:
        dt_time_to=datetime.fromtimestamp(int(time_to))
    except:
        if(int(time_to))<0:
            dt_time_to=datetime(2000,1,1)
        else:
            dt_time_to=datetime(3000,1,1)
    dt_time_to=timezone.make_aware(dt_time_to, timezone.get_current_timezone())
    Datum=[]
    if pair:
        if Ticker.objects.filter(pair=pair,ticker_updated_time__lte=dt_time_to).exists():
            b=Ticker.objects.filter(pair=pair,ticker_updated_time__lte=dt_time_to)[:int(limit)]
            #first is e.g 2012, last is e.g 2019
            response["Response"]= "Success"
            response["Type"]= 100
            response["Aggregated"]= False
            response["FirstValueInArray"]=True
            response["ConversionType"]={"type":"force_direct","conversionSymbol":""}
            response["RateLimit"]={}
            response["HasWarning"]=False
            c=reversed(b)
            for i in c:
                time_=int(time.mktime(i.ticker_updated_time.timetuple()))
                open_=float(i.ticker_open)
                close_=float(i.ticker_close)
                high_=float(i.ticker_high)
                low_=float(i.ticker_low)
                volumeto_=float(i.ticker_volume)
                volumefrom_=volumeto_*open_
                '''
                open_=round(float(i.ticker_open),2)
                close_=round(float(i.ticker_close),2)
                high_=round(float(i.ticker_high),2)
                low_=round(float(i.ticker_low),2)
                volumeto_=round(float(i.ticker_volume),2)
                volumefrom_=round(volumeto_*open_,2)
                '''
                tmp={"time":time_,"close":close_,"high":high_,"low":low_,"open":open_,"volumeto":volumeto_,"volumefrom":volumefrom_}
                Datum.append(tmp)
            else:
                response["TimeFrom"]=toTs
                response["TimeTo"]=toTs
                #implement no data
            finally:
                response["TimeFrom"]=Datum[-1]["time"]
                response["TimeTo"]=last=Datum[0]["time"]
                response["Data"]=Datum
        else:
            response["TimeFrom"]=toTs
            response["TimeTo"]=toTs
            response["Response"]= "Success"
            response["Type"]= 100
            response["Aggregated"]= False
            response["FirstValueInArray"]=True
            response["ConversionType"]={"type":"force_direct","conversionSymbol":""}
            response["RateLimit"]={}
            response["HasWarning"]=False
            response["Data"]="noData"

    else:
        response["TimeFrom"]=toTs
        response["TimeTo"]=toTs
        response["Response"]= "Success"
        response["Type"]= 100
        response["Aggregated"]= False
        response["FirstValueInArray"]=True
        response["ConversionType"]={"type":"force_direct","conversionSymbol":""}
        response["RateLimit"]={}
        response["HasWarning"]=False
        response["Data"]="noData"
    
    return JsonResponse(response)



def react_get_bars(request):
   
    response_data=inside
    #response_data=outside
    
    return JsonResponse(response_data)
    #return Response(response_data, status=HTTP_200_OK)