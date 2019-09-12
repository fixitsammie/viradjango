from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class Exchange(models.Model):
    name=models.CharField(max_length=40)
    def  __str__(self):
        return "{0}".format(self.name)

class Pair(models.Model):
    name=models.CharField(max_length=20)
    exchange=models.ForeignKey('Exchange', on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    def  __str__(self):
        return "{0} {1}".format(self.name,self.exchange.name)
    
#,unique_for_date="ticker_updated_time"
class Ticker(models.Model):
    pair=models.ForeignKey('Pair', on_delete=models.CASCADE)
    ticker_open=models.DecimalField(max_digits=30,decimal_places=10)
    ticker_close=models.DecimalField(max_digits=30,decimal_places=10)
    ticker_volume=models.DecimalField(max_digits=30,decimal_places=10)
    ticker_low=models.DecimalField(max_digits=30,decimal_places=10)
    ticker_high=models.DecimalField(max_digits=30,decimal_places=10)
    ticker_bulk_volume=models.DecimalField(max_digits=30,decimal_places=10)
    ticker_time=models.CharField(max_length=40)
    ticker_updated_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    def  __str__(self):
        return "{0} {1} {2}".format(self.pair.exchange.name, self.pair.name,self.ticker_time)
    
    
