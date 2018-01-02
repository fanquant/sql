# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:44:36 2017

@author: fanl
"""

import pyodbc
import pandas as pd
conn=pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=txic_service,1433;DATABASE=txnfdb;UID=txtg;PWD=tianxiang')
cursor = conn.cursor()
cursor.execute('select * from fund. T_ASSET_SUM')
#获取SQL列表，转换成dataframe格式
rows=cursor.fetchall()
col=['基金公司ID','基金公司名称','公告日期',
     '开始日期','截止日期','数据来源',
     '基金类型ID','基金类型','股票市值',
     '债券合计','银行存款及清算备付金','其他资产',
     '买入返售证券','应收证券清算款','权证','积极投资',
     '指数化投资','资产净值','资产总值','序列号','数据版本',
     '入库时间','数据状态']
rawdata=[list(i)for i in list(rows) ]
data_T_ASSET_SUM=pd.DataFrame(rawdata,columns=col)
print(data_T_ASSET_SUM)