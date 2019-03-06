# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:46:28 2018

@author: 45740
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:29:55 2018

@author: 45740
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:08:21 2018

@author: 45740
"""

import os
import cv2
import sys
import numpy as np
from PIL import Image
import pandas as pd
import glob
import csv
 
with open("C:/Users/45740/Desktop/2222.csv",'r', encoding='UTF-8') as csvfile1:
    reader = csv.reader(csvfile1)
    rows= [row for row in reader]
with open("C:/Users/45740/Desktop/test_jr.csv",'r', encoding='UTF-8') as csvfile2:
    reader = csv.reader(csvfile2)
    row2= [row for row in reader]
data1=np.array(rows)
data2=np.array(row2)
print(data1[1][0])
print(data2[1][0])

for i in range(0,12954):
    for j in range(0,306):
        if data1[i][0]==data2[j][0]:
            data1[i][0]="oooo"
    print(i)
writer = csv.writer(open('C:/Users/45740/Desktop/output2.csv', 'w'))
writer.writerows(data1)
            

            
            
        