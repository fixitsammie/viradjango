from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer,Ticker,Pair

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
                "supports_marks": True,
                "supports_timescale_marks": True,
                "supports_time": True,
                "exchanges": [
                
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
                "value": "Poloniex",
                "name": "Poloniex",
                "desc": "Poloniex"
                }
                ],
                "symbols_types": [
               
                {
                "name": "Stock",
                "value": "stock"
                },
                {
                "name": "Bitcoin",
                "value": "bitcoin"
                },
                {
                "name": "Index",
                "value": "index"
                }
                ],
                "supported_resolutions": [
                "1", "15", "240", "D",
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
    
    symbol={
        'name': the_symbol,
        'exchange-traded': exchange,
        'exchange-listed': exchange,
        'timezone': 'Africa/Lagos',
        'minmov': 0.1,
        'minmov2': 0,
        'pointvalue': 1,
        'session': '0930-1630',
        'has_intraday': False,
        'has_no_volume': False,
        'description': the_symbol,
        'type': 'stock',
        'supported_resolutions': [
        '1', '15', '240',
        'D',
        '2D',
        '3D',
        'W',
        '3W',
        'M',
        '6M'
        ],
        'pricescale': '1',
        'ticker': the_symbol
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
        'session-regular': "0900-1600",
        }
    response={'symbol':symbol}
    return JsonResponse(symbol)

def symbol_info2(request):
    symbol=request.GET['symbol']
    symbol={
        "name": "USDBTC",
        "exchange-traded": "Bitrex",
        "exchange-listed": "Bitrex",
        "timezone": "America/New_York",
        "minmov": 1,
        "minmov2": 0,
        "pointvalue": 1,
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
        "pricescale": 1,
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
def get_bars(request):
    symbol=request.GET['symbol']
    time_from=request.GET['from']
    time_to=request.GET['to']
    dt_time_from=datetime.fromtimestamp(int(time_from))
    dt_time_to=datetime.fromtimestamp(int(time_to))
    try:
        pair=Pair.objects.get(name=str(symbol))
    except:
        pair='hi'
    print(pair)
    resolution=request.GET['resolution']
    print("{0},{1},{2}".format(time_from,time_to,resolution))
    b=Ticker.objects.filter(ticker_updated_time__gte=dt_time_from).filter(ticker_updated_time__lte=dt_time_to)
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

    response={
       's': "ok",
       't': [1386493512, 1386493572, 1386493632, 1386493692],
       'c': [42.1, 43.4, 44.3, 42.8],
       'o': [41.0, 42.9, 43.7, 44.5],
       'h': [43.0, 44.1, 44.8, 44.5],
       'l': [40.4, 42.1, 42.8, 42.3],
       'v': [12000, 18500, 24000, 45000]
       }
    response={
       's': "ok",
       't': t,
       'c': c,
       'o': o,
       'h': h,
       'l': l,
       'v': v
       }
    #response=data_load['result']
    return JsonResponse(response,safe=False)

def get_server_time(request):
    import time
    current_time=int(time.time())
    response={'time':str(current_time)}
    return JsonResponse(response)


