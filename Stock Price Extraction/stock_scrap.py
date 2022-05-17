import datetime
import pandas as pd
stockcode ='SBIN'

ts1 = str(int(datetime.datetime(2020, 7, 20).timestamp())) 
ts2 = str(int(datetime.datetime(2020, 7, 25).timestamp()))

interval = '1d'
# interval = '1wk'
#interval = '1mo'

events = 'history'
#events = 'div'
#events = 'split'

url = 'https://query1.finance.yahoo.com/v7/finance/download/'\
      + stockcode + '.NS?period1=' + ts1 + '&period2=' + ts2 + '&interval='\
      + interval + '&events=' + events

print(url)
print (ts1, ts2)
try:
    stockdata = pd.read_csv(url)
    stockdata.to_csv(f'{stockcode}.csv')
    print(stockdata)
except:
    print("Not able to fetch value for code : "+stockcode)
    print("Either stock code is not correct or could be connectivity issue..")