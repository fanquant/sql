# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:46:21 2017

@author: fanl
"""

import sqlite3 as sq3
query='CREATE TABLE numbs(Date date,No1 real,No2 real)'
con=sq3.connect(path+'numbs.db')