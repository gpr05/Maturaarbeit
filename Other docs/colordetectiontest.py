#!/usr/bin/env python3

import os
import sys
from time import*
from ev3dev2 import*
from ev3dev2.motor import MediumMotor,LargeMotor,OUTPUT_A,OUTPUT_B,OUTPUT_C,OUTPUT_D, SpeedPercent, MoveTank, SpeedRPM
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor, InfraredSensor,ColorSensor
from ev3dev2.led import LEDS

#TODO:
rm= LargeMotor(OUTPUT_A)
lm= LargeMotor(OUTPUT_B)
lf=ColorSensor(INPUT_2)
em=MediumMotor(OUTPUT_C)
ld=ColorSensor(INPUT_3)
em=MediumMotor(OUTPUT_C)
y=0
x=0
for i in range(10000):
    x+=sum(lf.raw)
    y=x/(i+1)
    print(y)
