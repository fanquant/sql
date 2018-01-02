# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:20:52 2017

@author: fanl
"""

###做柱状图    T_FUND_COM_SCALE：F_COM_NAME-F4
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

























import numpy as np
import  matplotlib.mlab as mlab
import matplotlib.pyplot as plt
cursor.execute('select * from fund. T_FUND_COM_SCALE')
x=[]
y=[]
for row in cursor:
    x.append(row.F2('\n',''))
    y.append(row.F4('\n',''))
print(x)
print(y)
fig=plt.figure
plt.scatter(x,y,color='blue')
plt.xlabel('X-开放式基金资产净值')
plt.ylabel('Y-开放式基金份额')
plt.title('开放式基金资产净值-开放式基金份额')
plt.show()

