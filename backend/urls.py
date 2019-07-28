"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
#ehat 
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .api.views import login,sample_api
from django.conf import settings
from django.conf.urls.static import static

from .api.views import index_view, MessageViewSet,spill_data,udf_config,symbol_resolve,get_bars,symbol_search,get_server_time,symbol_info
#from .api.bittrex_main import bittrex_download
import django_registration
router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
# path('accounts/', include('password_reset.urls')),
urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    path('accounts/', include('django_registration.backends.one_step.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    #spill_data
     path('api/symbols/',symbol_resolve,name='symbol_resolve'),
      path('api/symbol_info/',symbol_info,name='symbol_info'),
      path('api/search/',symbol_search,name='symbol_search'),
      path('api/history/',get_bars,name='get_bars'),
    path('bittrex/',spill_data,name='spill_data'),
    path('api/bittrex/',spill_data,name='spill_dataa'),
     path('api/config/',udf_config,name='config'),
    path('api/time/',get_server_time,name='get_server_time'),
    
    #data download
    #path('api/data_download/bittrex',bittrex_download,name='bittrex_download'),

    # http://localhost:8000/api/admin/
    path('admin/', admin.site.urls),
    path('auth/',obtain_jwt_token),
    path('api/login',login),
    path('api/sampleapi', sample_api)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


