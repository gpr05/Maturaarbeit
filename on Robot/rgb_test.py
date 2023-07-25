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
trgt=[0.0,0.0,0.0]
a=[0.0,0.0,0.0]
b=[0.0,0.0,0.0]
#[113.11902730375427, 153.04650170648463, 175.46373720136518]
#332.25
#71.5
for i in range(100000):
    a[0]+=lf.rgb[0]
    a[1]+=lf.rgb[1]
    a[2]+=lf.rgb[2]
    b[0]=lf.rgb[0]
    b[1]=lf.rgb[1]
    b[2]=lf.rgb[2]
    trgt[0]=a[0]/(i+1)
    trgt[1]=a[1]/(i+1)
    trgt[2]=a[2]/(i+1)
    print(trgt)
