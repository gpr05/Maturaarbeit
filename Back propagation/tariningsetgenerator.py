import numpy as np
import matplotlib.pylab as plt
from math import e
import pandas as pd
import os

b=np.array([0.95764,0.45682,0.52884,0.4,0.566,1.23])
a=np.array([1.09934,0.9454,0.345,0.8993,0.3452,0.0345,1.236,0.4444,0.555])
rgb=[]
B=np.random.rand(8,1)
W=np.random.rand(18,1)
print(B,W)

def evalnn(rgb):
    re=(rgb[0]*a[0]*b[0]+rgb[1]*a[1]*b[0]+rgb[2]*a[2]*b[0]+
        rgb[0]*a[3]*b[1]+rgb[1]*a[4]*b[1]+rgb[2]*a[5]*b[1]+
        rgb[0]*a[6]*b[2]+rgb[1]*a[7]*b[2]+rgb[2]*a[8]*b[2])
    li=(rgb[0]*a[0]*b[3]+rgb[1]*a[1]*b[3]+rgb[2]*a[2]*b[3]+
        rgb[0]*a[3]*b[4]+rgb[1]*a[4]*b[4]+rgb[2]*a[5]*b[4]+
        rgb[0]*a[6]*b[5]+rgb[1]*a[7]*b[5]+rgb[2]*a[8]*b[5])
    return re,li



def f(x):
    return 1/(1+e**(-x))#x#1/(1+e**(-10*x+5))

def fder(x):
    return (e**x)/((1+e**x)**2)#1#(e**10*x+5)/((1+e**10*x+5)**2)

def evalnnWB(rgb):
    re=f(f(f(rgb[0]*W[0]+B[0])*W[3]+f(rgb[1]*W[1]+B[1])*W[4]+f(rgb[2]*W[2]+B[2])*W[5]+B[3])*W[12]+
         f(f(rgb[0]*W[0]+B[0])*W[6]+f(rgb[1]*W[1]+B[1])*W[7]+f(rgb[2]*W[2]+B[2])*W[8]+B[4])*W[13]+
         f(f(rgb[0]*W[0]+B[0])*W[9]+f(rgb[1]*W[1]+B[1])*W[10]+f(rgb[2]*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])
    li=f(f(f(rgb[0]*W[0]+B[0])*W[3]+f(rgb[1]*W[1]+B[1])*W[4]+f(rgb[2]*W[2]+B[2])*W[5]+B[3])*W[15]+
         f(f(rgb[0]*W[0]+B[0])*W[6]+f(rgb[1]*W[1]+B[1])*W[7]+f(rgb[2]*W[2]+B[2])*W[8]+B[4])*W[16]+
         f(f(rgb[0]*W[0]+B[0])*W[9]+f(rgb[1]*W[1]+B[1])*W[10]+f(rgb[2]*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])
    return rgb,re,li

def eval():
    for i in range(100):
        d=[0.0,0.0,0.0]
        for r in range(3):
            d[r]=np.random.random()*255
        rgb.append([evalnnWB(d)])
    df = pd.DataFrame([rgb] )#columns=["R", "G",'B','re','li'])  # doctest: +SKIP
    '''with pd.ExcelWriter("D:training sets.xlsx",mode='a',if_sheet_exists='overlay') as writer:
        df.to_excel(writer)  # doctest: +SKIP'''
    for g in range(100):
        print(rgb[g])
eval()
