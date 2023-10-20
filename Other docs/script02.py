#!/usr/bin/env python3

from time import*
from ev3dev2 import*
from ev3dev2.motor import LargeMotor,OUTPUT_A,OUTPUT_B, SpeedRPM
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import ColorSensor

#TODO:
rm= LargeMotor(OUTPUT_A)
lm= LargeMotor(OUTPUT_B)
lf=ColorSensor(INPUT_2)
trgt=332.25
print(trgt)

pg=0.2500 #kp error
ig=0.01125#ki errsum
dg=0.2 #kd errdiff

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
    rot=pg*error+ig*inte+dg*der
    lm.on(SpeedRPM(v+rot))
    rm.on(SpeedRPM(v-rot))
