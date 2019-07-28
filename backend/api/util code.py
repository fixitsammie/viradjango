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


from backend.api.bittrex_data import data_load
from backend.api.models import Pair,Exchange
from dateutil.parser import parse
from datetime import datetime,time
from dateutil import tz,parser
default_date=datetime.combine(datetime.now(), time(0,tzinfo=tz.gettz("America/New_York")))


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


parse(i['T'],default=default_date)
models.TestModel.objects.bulk_create(instances)