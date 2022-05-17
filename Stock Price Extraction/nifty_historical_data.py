import datetime
import pandas as pd
ts1 = str(int(datetime.datetime(2022, 1, 1).timestamp())) 
ts2 = str(int(datetime.datetime.today().timestamp()))

interval = '1d'
# interval = '1wk'
# interval = '1mo'

events = 'history'

url = 'https://query1.finance.yahoo.com/v7/finance/download/%5ENSEI?period1='\
       + ts1 + '&period2=' + ts2 + '&interval=' + interval + '&events=history&includeAdjustedClose=true'

print(url)
print (ts1, ts2)
try:
    stockdata = pd.read_csv(url)
    stockdata.to_csv('stockdata.csv')
    print(stockdata)
except:
    print("Not able to fetch value for code : Nifty50")
    print("Either stock code is not correct or could be connectivity issue..")