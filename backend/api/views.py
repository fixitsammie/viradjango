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
        
