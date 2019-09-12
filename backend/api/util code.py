exchange=Exchange(name='Bittrex')
pair=Pair.get('name'='BTCUSD')
ticker_pair=
ticker_open=
ticker_close=
ticker_volume=
ticker_low=
ticker_high=
ticker_bulk_volume=
ticker_time=
ticker_update_time=

for i in b:
...     Ticker(pair=a,ticker_open=i['O'],ticker_close=i['C'],ticker_volume=i['V'],ticker_low=i['L'],
...     ticker_high=i['H'],ticker_bulk_volume['BV'],ticker_time=ticker_time


int(datetime)
import datetime from datetime

datetime.fromtimestamp(int(time_from))

from dateutil.parser import parse
.date().isoformat().replace('-','.')

parse(candle['T']).date().isoformat().replace('-','.')


import datetime from datetime
parse(i['T'])

parse(i['T']).date().timetuple()

ticker_time=time.mktime(parse(i['T']).date().timetuple())

tzinfo=timezone.utc

for i in b:
	Ticker(pair=a,ticker_open=i['O'],
	ticker_close=i['C'],ticker_volume=i['V'],
	ticker_low=i['L'],
	ticker_high=i['H'],ticker_bulk_volume=i['BV'],
	ticker_time=i['T'],ticker_updated=parse(i['T'],default=default_date) ).save()

from dateutil import tzinfo
NYC=tz.gettz('America/New_York')
dateutil.parser.parse('2017-08-02 12:34 am +06:00')


from backend.api.bittrex_data import dataload
from backend.api.models import Pair,Exchange,Ticker
from dateutil.parser import parse
from datetime import datetime,time
from dateutil import tz,parser
default_date=datetime.combine(datetime.now(), time(0,tzinfo=tz.gettz("America/New_York")))

a=Pair.objects.get(pk=1)
b=data_load['result']
c=[]
def gen_tickers(b):
	for i in b:
		Ticker(pair=a,ticker_open=i['O'],
		ticker_close=i['C'],ticker_volume=i['V'],
		ticker_low=i['L'],
		ticker_high=i['H'],ticker_bulk_volume=i['BV'],
		ticker_time=i['T'],ticker_updated_time=parse(i['T'],default=default_date) )
		c.append(i)
Ticker.objects.bulk_create(c)

'''
parse(i['T'],default=default_date)
models.TestModel.objects.bulk_create(instances)
'''
a=Pair.objects.get(pk=1)
for i in b:
	ticker=Ticker(pair=a,ticker_open=i['O'],
	ticker_close=i['C'],ticker_volume=i['V'],
	ticker_low=i['L'],
	ticker_high=i['H'],ticker_bulk_volume=i['BV'],
	ticker_time=i['T'],ticker_updated_time=parse(i['T'],default=default_date) )
	c.append(ticker)
	#bulk_mgr.add(ticker)

Ticker.objects.bulk_create(c)
from backend.api.bulk_creator import BulkCreateManager
bulk_mgr = BulkCreateManager(chunk_size=1000)
for i in b:
	ticker=Ticker(pair=a,ticker_open=i['O'],
	ticker_close=i['C'],ticker_volume=i['V'],
	ticker_low=i['L'],
	ticker_high=i['H'],ticker_bulk_volume=i['BV'],
	ticker_time=i['T'],ticker_updated_time=parse(i['T'],default=default_date) )
	bulk_mgr.add(ticker)

cloud_sql_proxy.exe -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306