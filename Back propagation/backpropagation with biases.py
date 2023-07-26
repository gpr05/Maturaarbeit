import base64
import numpy as np
import matplotlib.pylab as plt

#erste versuch in training
#
W=np.random.rand(18,1)
B=np.random.rand(8,1)

                        #R                      G               B         re,li
tset=[[113.11902730375427,153.04650170648463,175.46373720136518,5.0,5.0],[175.0,175.0,175.0,5.0,2.0],[100.0,100.0,200.0,2.0,5.0]]
tset2=[[122,200,10,524.3120897791999, 533.6532256],[100, 100, 180,456.66741616, 510.14936],[20, 230, 18,352.413101372, 322.139278],[50, 50, 50, 202.74761647999998, 221.4676],[220, 130, 110, 704.902035172, 781.224002]]
#rgb zahlen/255
def f(x):
    return x

def fder(x):
    return 1

def evalnn(rgb):
    re=f(f(f(rgb[0]*W[0]+B[0])*W[3]+f(rgb[1]*W[1]+B[1])*W[4]+f(rgb[2]*W[2]+B[2])*W[5]+B[3])*W[12]+
         f(f(rgb[0]*W[0]+B[0])*W[6]+f(rgb[1]*W[1]+B[1])*W[7]+f(rgb[2]*W[2]+B[2])*W[8]+B[4])*W[13]+
         f(f(rgb[0]*W[0]+B[0])*W[9]+f(rgb[1]*W[1]+B[1])*W[10]+f(rgb[2]*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])
    li=f(f(f(rgb[0]*W[0]+B[0])*W[3]+f(rgb[1]*W[1]+B[1])*W[4]+f(rgb[2]*W[2]+B[2])*W[5]+B[3])*W[15]+
         f(f(rgb[0]*W[0]+B[0])*W[6]+f(rgb[1]*W[1]+B[1])*W[7]+f(rgb[2]*W[2]+B[2])*W[8]+B[4])*W[16]+
         f(f(rgb[0]*W[0]+B[0])*W[9]+f(rgb[1]*W[1]+B[1])*W[10]+f(rgb[2]*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])
    return re,li

def c(tval):
    re,li=evalnn(tval[0:3])
    return 0.5*(re-tval[3])**2+0.5*(li-tval[4])**2

def ctt(tval):
    ct=0
    for val in tval:
        ct+=c(val)
    return ct

def gradc(tval):
    R=tval[0]
    G=tval[1]
    b=tval[2]
    ret=tval[3]
    lit=tval[4]
    gradW=np.zeros((18,1))
    gradB=np.zeros((8,1))
    re,li=evalnn(tval[0:3])
    gradW[0]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  R+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  R+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*R+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  R+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  R+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*R+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[1]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* G+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* G+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*G+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* G+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* G+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*G+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[2]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradW[3]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  1+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  1+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[4]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 1+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 1+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[5]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 1))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 1))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[6]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  1+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  1+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[7]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 1+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 1+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[8]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 1))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 1))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[9]= (re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*1+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*1+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[10]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*1+fder(b*W[2]+B[2])*W[11]*0)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*1+fder(b*W[2]+B[2])*W[11]*0)))

    gradW[11]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*1)))+(li-lit)*fder(

                            f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* 0))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* 0))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*1)))
#stopped here
    gradW[12]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradW[13]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradW[14]=(re-ret)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]+B[6])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[12]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[13]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[14]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradW[15]=(li-lit)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradW[16]=(li-lit)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradW[17]=(li-lit)*fder(f(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]+
                            f(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]+
                            f(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]+B[7])*(
                            (fder(f(R*W[0]+B[0])*W[3]+f(G*W[1]+B[1])*W[4]+f(b*W[2]+B[2])*W[5]+B[3])*W[15]*(fder(R*W[0]+B[0])*W[3]*  0+fder(G*W[1]+B[1])*W[4]* 0+fder(b*W[2]+B[2])*W[5]* b))+
                            (fder(f(R*W[0]+B[0])*W[6]+f(G*W[1]+B[1])*W[7]+f(b*W[2]+B[2])*W[8]+B[4])*W[16]*(fder(R*W[0]+B[0])*W[6]*  0+fder(G*W[1]+B[1])*W[7]* 0+fder(b*W[2]+B[2])*W[8]* b))+
                            (fder(f(R*W[0]+B[0])*W[9]+f(G*W[1]+B[1])*W[10]+f(b*W[2]+B[2])*W[11]+B[5])*W[17]*(fder(R*W[0]+B[0])*W[9]*0+fder(G*W[1]+B[1])*W[10]*0+fder(b*W[2]+B[2])*W[11]*b)))

    gradB[0]=(re-ret)*           R*W[0]+                 (li-lit)*                   R*W[3]
    gradB[1]=(re-ret)*           G*W[0]+                 (li-lit)*                   G*W[3]
    gradB[2]=(re-ret)*           b*W[0]+                 (li-lit)*                   b*W[3]
    gradB[3]=(re-ret)*           R*W[1]+                 (li-lit)*                   R*W[4]
    gradB[4]=(re-ret)*           G*W[1]+                 (li-lit)*                   G*W[4]
    gradB[5]=(re-ret)*           b*W[1]+                 (li-lit)*                   b*W[4]
    gradB[6]=(re-ret)*           R*W[2]+                 (li-lit)*                   R*W[5]
    gradB[7]=(re-ret)*           G*W[2]+                 (li-lit)*                   G*W[5]
    return gradW, gradB

def gradctot(tval):

    gradWtot=np.zeros((18,1))
    gradBtot=np.zeros((8,1))
    for i in tval :#range(3):
        gradW, gradB =gradc(i)
        gradWtot+=gradW
        gradBtot+=gradB
    return gradWtot, gradBtot

def adjustment(val,eps):
    c=W
    d=B
    tot=np.zeros((26,1))
    Wadj,Badj=gradctot(val)
    tot[0:18]=Wadj
    tot[17:25]=Badj
    lengh=np.linalg.norm(tot)
    W[0]=W[0]-(Wadj[0]/lengh)*eps
    W[1]=W[1]-(Wadj[1]/lengh)*eps
    W[2]=W[2]-(Wadj[2]/lengh)*eps
    W[3]=W[3]-(Wadj[3]/lengh)*eps
    W[4]=  W[4]-(Wadj[4]/lengh)*eps
    W[5]=  W[5]-(Wadj[5]/lengh)*eps
    W[6]=  W[6]-(Wadj[6]/lengh)*eps
    W[7]=  W[7]-(Wadj[7]/lengh)*eps
    W[8]=  W[8]-(Wadj[8]/lengh)*eps
    W[9]=  W[9]-(Wadj[9]/lengh)*eps
    W[10]=W[10]-(Wadj[10]/lengh)*eps
    W[11]=W[11]-(Wadj[11]/lengh)*eps
    W[12]=W[12]-(Wadj[12]/lengh)*eps
    W[13]=W[13]-(Wadj[13]/lengh)*eps
    W[14]=W[14]-(Wadj[14]/lengh)*eps
    W[15]=W[15]-(Wadj[15]/lengh)*eps
    W[16]=W[16]-(Wadj[16]/lengh)*eps
    W[17]=W[17]-(Wadj[17]/lengh)*eps
    B[0]=  B[0]-(Badj[0]/lengh)*eps
    B[1]=  B[1]-(Badj[2]/lengh)*eps
    B[2]=  B[2]-(Badj[2]/lengh)*eps
    B[3]=  B[3]-(Badj[3]/lengh)*eps
    B[4]=  B[4]-(Badj[4]/lengh)*eps
    B[5]=  B[5]-(Badj[5]/lengh)*eps
    B[6]=  B[6]-(Badj[6]/lengh)*eps
    B[7]=  B[7]-(Badj[7]/lengh)*eps
    middelta=(np.mean(W-c)+np.mean(B-d))/2
    return W,B,middelta, lengh

def train(set,eps):
    errold=ctt(set)
    errnew=0
    W=None
    B=None
    n=0
    H=[]
    while ctt(set)>0.0 and eps>10**-10:#abs(errold-errnew)>0.01 and n<=10000:
        if errold-errnew<0:
            eps=eps/2
        W,B,change,leng =adjustment(set,eps)
        errold=errnew
        errnew=ctt(set)
        print([n,change,float(errnew), leng, eps])
        H.append([float(errnew),leng])

        if n%10000==0:
            plt.plot(H)
            plt.show()
        #print(H[n])
        n+=1
    plt.plot(H)
    plt.show()
    return W,B
print(train(tset2,20))
#print(adjustment(tset,0.1))
print(evalnn(tset2[0][0:3]))
print(evalnn(tset2[1][0:3]))
print(evalnn(tset2[2][0:3]))
print(ctt(tset2))
