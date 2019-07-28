from django.contrib import admin

# Register your models here.

from .models import Exchange, Pair, Ticker

admin.site.register(Exchange)
admin.site.register(Pair)
admin.site.register(Ticker)
