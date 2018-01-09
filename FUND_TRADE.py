# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:33:27 2017

@author: fanl
"""
import pyodbc
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as sql
conn=pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=txic_service,1433;DATABASE=txnfdb;UID=txtg;PWD=tianxiang')
#SQL查询全部基金交易数据，并读取数据库列名称为表头(较慢)
fund_trade=sql.read_sql('select * from STOCK.T_FUND_TRADE',conn)
print(fund_trade)
#取出fund_trade中三列，分别为：交易日期，基金代码，收盘价,并且以交易代码为索引。
F_CLOSE=DataFrame(fund_trade[['F_TRADE_DATE','F_FUND_CODE','F_CLOSE']])
FC=F_CLOSE

#布尔型索引，根据基金代码列是否为制定基金代码，选择该基金的全部收盘价
codelist=(165516,161714)
FC[FC['F_FUND_CODE']==codelist]
F_CLOSE_CHOOSEN=DataFrame(FC[FC['F_FUND_CODE']==code
                                  for code in codelist)
FCC=F_CLOSE_CHOOSEN
FC
###20-23 想获取两只基金的历史收盘价？？？？
print(FC)
for code in codelist:
     print(code)
F_CLOSE_CHOOSEN={}
for code in codelist:
          F_CLOSE_CHOOSEN=DataFrame(F_CLOSE[F_CLOSE['F_FUND_CODE']==code])
A=F_CLOSE_CHOOSEN.sort_index(by='F_TRADE_DATE')
A
F_CLOSE_CHOOSEN
#根据交易日期列进行排序
F_CLOSE_CHOOSEN.sort_index(by='F_TRADE_DATE')
F_CLOSE['F_FUND_CODE'==165516]
F_CLOSE.ix[510220]
CODE_LIST=(510220,165516)
for code in CODE_LIST:
    print(code)
F_CLOSE_CHOOSE=DataFrame(F_CLOSE[F_CLOSE['F_FUND_CODE']==[code for code in CODE_LIST]])
