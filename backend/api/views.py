from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer


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
    response= {"supports_search": true,
                "supports_group_request": false,
                "supports_marks": true,
                "supports_timescale_marks": true,
                "supports_time": true,
                "exchanges": [
                {
                "value": "",
                "name": "All Exchanges",
                "desc": ""
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
                "value": "Poloniex",
                "name": "Poloniex",
                "desc": "Poloniex"
                }
                ],
                "symbols_types": [
                {
                "name": "All types",
                "value": ""
                },
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
    {
"name": "USDBTC",
"exchange-traded": "Bitrex",
"exchange-listed": "Bitrex",
"timezone": "America/New_York",
"minmov": 1,
"minmov2": 0,
"pointvalue": 1,
"session": "24x7",
"has_intraday": false,
"has_no_volume": false,
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
"pricescale": 100,
"ticker": "USDBTC"
}
    response={'symbol':str(symbol)}
    return JsonResponse(response)


def symbol_search(request):
    query=request.GET['query']
    exchange=request.GET['exchange']
    symbol_type=request.GET['type']
    limit=request.GET['limit']
    response=[
    {
        "symbol": "<short symbol name>",
        "full_name": "<full symbol name>", 
        "description": "<symbol description>",
        "exchange": "<symbol exchange name>",
        "ticker": "<symbol ticker name, optional>",
        "type": "bitcoin" 
    },{
"symbol": "AZO",
"full_name": "AZO",
"description": "AutoZone, Inc.",
"exchange": "NYSE",
"type": "stock"
}
    ]
    response={'symbol':str(query)}
    return JsonResponse(response)

def get_bars(request):
    symbol=request.GET['symbol']
    time_from=request.GET['from']
    time_to=request.GET['to']
    resolution=request.GET['resolution']
    response={
   s: "ok",
   t: [1386493512, 1386493572, 1386493632, 1386493692],
   c: [42.1, 43.4, 44.3, 42.8],
   o: [41.0, 42.9, 43.7, 44.5],
   h: [43.0, 44.1, 44.8, 44.5],
   l: [40.4, 42.1, 42.8, 42.3],
   v: [12000, 18500, 24000, 45000]
   }
    return JsonResponse(response)

def get_server_time(request):
    import time
    return JsonResponse(response)
