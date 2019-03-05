# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:06:16 2018

@author: 45740
"""

import csv
import numpy as np
import os 
import shutil
import pandas as pd


with open("F:/谷歌下载/csv/yingshe.csv",'r', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]
#print (rows)
data=np.array(rows)
#print("out0=",type(data),data.shape)
#print("out1=",type)
a=[]
for i in range(6843):
    if data[i][0]==str(0):
        a.append(5)
    if data[i][0]==str(1):
        a.append(4)
    if data[i][0]==str(2):
        a.append(3)
    if data[i][0]==str(3):
        a.append(2)
    if data[i][0]==str(4):
        a.append(1)
      
dataframe = pd.DataFrame({'new_label':a})


dataframe.to_csv("F:/谷歌下载/csv/est.csv",index=True,sep=',')
        
            
            