# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:33:27 2017

@author: fanl
"""
import pyodbc
import pandas as pd
import pandas.io.sql as sql
conn=pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=txic_service,1433;DATABASE=txnfdb;UID=txtg;PWD=tianxiang')
#读取数据库列名称
filedfund=sql.read_sql('select * from fund.T_FUND_IN_SHARE where F_NEW=1',conn)
filedfund[2]
import pandas as pd
import pandas_datareader as web
all_data={}
for ticker in ['AAPL','IBM','MSFT','GOOG']:
    all_data[ticker]=web.get_data_yahoo(ticker,'1/1/2000','1/1/2018')
price=pd.DataFrame({tic:data['Adj Close']
                    for tic,data in all_data.iteritems()})
volume=pd.DataFrame({tic:data['Volume']
                    for tic,data in all_data.iteritems()})
print(price)
