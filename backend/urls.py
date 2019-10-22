from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from .api.views import index_view,udf_config,symbol_resolve,get_bars,symbol_search,get_server_time,symbol_info,get_all_exchanges,react_get_bars_r,logout_request
from .api.bittrex_main import bittrex_download
from .api.binance_main import binance_download
from .api.bitfinex_main import bitfinex_download
import django_registration
router = routers.DefaultRouter()
from django_registration.backends.one_step.views import RegistrationView

# path('accounts/', include('password_reset.urls')),
urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),
   
    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),
path('accounts/register/',
        RegistrationView.as_view(success_url='/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
path('logout',logout_request,name='logout_request'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('data/histoday',react_get_bars_r,name='react_get_bars_r'),
    #spill_data
     path('api/symbols',symbol_resolve,name='symbol_resolve'),
     path('api/symbols/',symbol_resolve,name='symbol_resolve2'),
      path('api/symbol_info',symbol_info,name='symbol_info'),
      path('api/search/',symbol_search,name='symbol_search'),
      path('api/history',get_bars,name='get_bars'),
     path('api/config/',udf_config,name='config'),
    path('api/time/',get_server_time,name='get_server_time'),

    path('api/exchanges',get_all_exchanges,name='get_all_exchanges'),
    
    #data download
    path('api/data_download/bittrex',bittrex_download,name='bittrex_download'),
    path('api/data_download/binance',binance_download,name='binance_download'),
    path('api/data_download/bitfinex',bitfinex_download,name='bitfinex_download'),

    # http://localhost:8000/api/admin/
    path('admin/', admin.site.urls),
    path('auth/',obtain_jwt_token)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


