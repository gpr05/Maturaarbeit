import numpy as np
import matplotlib.pylab as plt

b=np.array([0.95764,0.45682,0.52884,0.4,0.566,1.23])
a=np.array([1.09934,0.9454,0.345,0.8993,0.3452,0.0345,1.236,0.4444,0.555])
rgb=[220,130,110]

def evalnn(rgb):
    re=(rgb[0]*a[0]*b[0]+rgb[1]*a[1]*b[0]+rgb[2]*a[2]*b[0]+
        rgb[0]*a[3]*b[1]+rgb[1]*a[4]*b[1]+rgb[2]*a[5]*b[1]+
        rgb[0]*a[6]*b[2]+rgb[1]*a[7]*b[2]+rgb[2]*a[8]*b[2])
    li=(rgb[0]*a[0]*b[3]+rgb[1]*a[1]*b[3]+rgb[2]*a[2]*b[3]+
        rgb[0]*a[3]*b[4]+rgb[1]*a[4]*b[4]+rgb[2]*a[5]*b[4]+
        rgb[0]*a[6]*b[5]+rgb[1]*a[7]*b[5]+rgb[2]*a[8]*b[5])
    return re,li
print(rgb, evalnn(rgb))
