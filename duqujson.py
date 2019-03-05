# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:58:36 2018

@author: 45740
"""
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
#s=json.load("C:/Users/45740/Desktop/00e90efc3.json")
#s2 = json.loads(s)
#print(s2)
rop="G:/json"
lis=os.listdir(rop)
n=[]
m=[]
def rle_encode(img):
        '''
        img: numpy array, 1 - mask, 0 - background
        Returns run length as string formated
        '''
        pixels = img.flatten()
        pixels = np.concatenate([[0], pixels, [0]])
        runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
        runs[1::2] -= runs[::2]
        return ' '.join(str(x) for x in runs)
for i in lis:
    a=[]
    imgp=os.path.join(rop,i)
    with open(imgp,encoding='utf-8') as f:
        line = f.read()
        d = json.loads(line)
        points=d["shapes"]
        print(type(points))
        name=d["imagePath"]
        print(name)
        
        for i in range(len(points)):
            l=points[i]["points"]
            a.append(l)
        f.close()
    
        for j in range(len(a)):
            n.append(name)
            b=a[j]
           
            b=np.array(b,dtype = np.int32)
            
            im = np.zeros((768,768), dtype = "uint8")
            
            cv2.polylines(im, [b], 1, 255)
            
            cv2.fillPoly(im, [b], 255)
            mask = im
            mask_rle = rle_encode(mask.T)
            m.append(mask_rle)
dataframe = pd.DataFrame({'EncodedPixels':m,'ImageId':n})


dataframe.to_csv("C:/Users/45740/Desktop/duo.csv",index=True,sep=',')
  
#cv2.imshow("Mask", mask)"""
