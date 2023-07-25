#!/usr/bin/env python3

import os
import sys
import numpy as np
import random as rd
from time import*
from ev3dev2 import*
from ev3dev2.motor import LargeMotor,OUTPUT_A,OUTPUT_B,SpeedRPM
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import  ColorSensor


#TODO:
rm= LargeMotor(OUTPUT_A)
lm= LargeMotor(OUTPUT_B)
lf=ColorSensor(INPUT_2)
#em=MediumMotor(OUTPUT_C)
#ld=ColorSensor(INPUT_3)
#ld=ColorSensor(INPUT_3)


class net():
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)
        self.y          = y
        self.output     = np.zeros(y.shape)
    def __init__(self,red,blue,green):
        self.red =red
        self.blue =blue
        self.green =green
    #def


while True:
    colors=lf.rgb
    #vm=net(colors[0],colors[1],colors[2])
    lm.on(SpeedRPM(vm[0]))
    rm.on(SpeedRPM(vm[1]))
