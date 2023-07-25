#!/usr/bin/env python3

import os
import sys
from time import*
from ev3dev2 import*
from ev3dev2.motor import MediumMotor,LargeMotor,OUTPUT_A,OUTPUT_B,OUTPUT_C,OUTPUT_D, SpeedPercent, MoveTank, SpeedRPM
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor, InfraredSensor,ColorSensor
from ev3dev2.led import LEDS
#import matplotlib.pylab as plt

#TODO:
rm= LargeMotor(OUTPUT_A)
lm= LargeMotor(OUTPUT_B)
lf=ColorSensor(INPUT_2)
#em=MediumMotor(OUTPUT_C)
#ld=ColorSensor(INPUT_3)
#ld=ColorSensor(INPUT_3)
trgt=332.25
#71.5
print(trgt)

pg=0.2500 #kp error
ig=0.01125#ki errsum
dg=0.2 #kd errdiff
row=0
column=0
val=["velocity",'distance','reflection','errorold','target','errbias','error','errsumbias','errsum','differrbias','differr','rotation','','','']

def status(integral,derivative):
    if abs(integral)<5 and abs(derivative)>40:
        lm.off(True)
        rm.off(True)
        if derivative>0:
            vs=50
            vr=0
            return 1
        else:
            vs=0
            vr=50
            return 2
    else:
        return 0
inte=0
lr=0
erh=[0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
v=50
history=[]
lf.raw
while True:
    c=sum(lf.raw)
    error=sum(lf.raw)-trgt
    erh[1:19]=erh[0:18]
    erh[0]=error
    inte=sum(erh[0:19])
    der=error-erh[1]
    status1=status(inte,der)
    while status1==1 or status1==2:
        if status1==1:
            vs=50
            vr=-20
        else:
            vs=-20
            vr=50
        lm.on(SpeedRPM(vs))
        rm.on(SpeedRPM(vr))
        error=sum(lf.raw)-trgt
        if abs(error)<=10:
            status1=False
    rot=pg*error+ig*inte+dg*der
    if abs(inte)>350:
        v=12
    else:
        v=25
    x1=v+rot
    x2=v-rot
    while abs(x1)>=175 or abs(x2)>=175:
        if x1>175:
            x1=174
        elif x1<-175:
            x1=-174
        if x2<-175:
            x2=-174
        elif x2>175:
            x2=174
    lm.on(SpeedRPM(x1))
    rm.on(SpeedRPM(x2))
    a=[v,c,lr,trgt,pg,error,ig,inte,dg,der,rot,pg*error,ig*inte,dg*der]
    '''plt.plot(a)
    plt.show()'''
    history.append(a)
    b=[pg*error,ig*inte,dg*der]
    print(val,b,a)
