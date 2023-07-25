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
x=MoveTank(left_motor_port=OUTPUT_B ,right_motor_port=OUTPUT_A,motor_class=LargeMotor)
rm= LargeMotor(OUTPUT_A)
lm= LargeMotor(OUTPUT_B)
lf=ColorSensor(INPUT_2)
cs=ColorSensor(INPUT_3)
em=MediumMotor(OUTPUT_C)

#x.on_for_seconds(25,25,2)
#em.on_for_rotations(SpeedRPM(30),4)
em.on(SpeedRPM(30))
'''
while em.is_running==True:
    print(cs.raw)
    if cs.raw==
exit()
'''
