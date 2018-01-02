# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:43:54 2017

@author: fanl
"""

import pyodbc
import pandas as pd
conn=pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=txic_service,1433;DATABASE=txnfdb;UID=txtg;PWD=tianxiang')
cursor = conn.cursor()
cursor.execute('select * from fund. T_FUND_COM_SCALE')
#获取SQL列表，转换成dataframe格式
rows=cursor.fetchall()
col=['基金公司代码','公司简称','公司类型（内资合资）',
     '公告日期','封闭式基金资产净值','开放式基金资产净值',
     '封闭式基金份额','开放式基金份额','封闭式基金只数',
     '开放式基金只数','序列号','数据版本','入库时间','数据状态']
rawdata=[list(i)for i in list(rows) ]
data=pd.DataFrame(rawdata,columns=col)
print(data[:])