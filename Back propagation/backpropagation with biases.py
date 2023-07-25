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
    B=tval[2]
    ret=tval[3]
    lit=tval[4]
    gradW=np.zeros((18,1))
    gradB=np.zeros((8,1))
    re,li=evalnn(tval[0:3])
    gradW[0]= (re-ret)*(R*a[0]+G*a[1]+B*a[2])+(li-lit)
    gradW[1]= (re-ret)*(R*a[3]+G*a[4]+B*a[5])+(li-lit)
    gradW[2]= (re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[3]= (re-ret)*(R*a[0]+G*a[1]+B*a[2])+(li-lit)
    gradW[4]= (re-ret)*(R*a[3]+G*a[4]+B*a[5])+(li-lit)
    gradW[5]= (re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[6]= (re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[7]= (re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[8]= (re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[9]= (re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[10]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[11]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[12]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[13]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[14]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[15]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[16]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)
    gradW[17]=(li-lit)*(R*a[6]+G*a[7]+B*a[8])+(li-lit)

    gradB[0]=(re-ret)*R*b[0]+(li-lit)*R*b[3]
    gradB[1]=(re-ret)*G*b[0]+(li-lit)*G*b[3]
    gradB[2]=(re-ret)*B*b[0]+(li-lit)*B*b[3]
    gradB[3]=(re-ret)*R*b[1]+(li-lit)*R*b[4]
    gradB[4]=(re-ret)*G*b[1]+(li-lit)*G*b[4]
    gradB[5]=(re-ret)*B*b[1]+(li-lit)*B*b[4]
    gradB[6]=(re-ret)*R*b[2]+(li-lit)*R*b[5]
    gradB[7]=(re-ret)*G*b[2]+(li-lit)*G*b[5]
    return gradW, gradB

def gradctot(tval):

    gradWtot=np.zeros((17,1))
    gradBtot=np.zeros((8,1))
    for i in tval :#range(3):
        gradW, gradB =gradc(i)
        gradWtot+=gradW
        gradBtot+=gradB
    return gradWtot, gradBtot

def adjustment(val,eps):
    c=a
    d=b
    tot=np.zeros((15,1))
    aadj,badj=gradctot(val)
    tot[0:9]=aadj
    tot[8:14]=badj
    lengh=np.linalg.norm(tot)
    W[0]=W[0]-(Wadj[0]/lengh)*eps
    W[1]=W[1]-(Wadj[1]/lengh)*eps
    W[2]=W[2]-(Wadj[2]/lengh)*eps
    W[3]=W[3]-(Wadj[3]/lengh)*eps
    W[4]=  W[4]-(Wadj[]/lengh)*eps
    W[5]=  W[5]-(Wadj[]/lengh)*eps
    W[6]=  W[6]-(Wadj[]/lengh)*eps
    W[7]=  W[7]-(Wadj[]/lengh)*eps
    W[8]=  W[8]-(Wadj[]/lengh)*eps
    W[9]=  W[9]-(Wadj[]/lengh)*eps
    W[10]=W[10]-(Wadj[]/lengh)*eps
    W[11]=W[11]-(Wadj[]/lengh)*eps
    W[12]=W[12]-(Wadj[]/lengh)*eps
    W[13]=W[13]-(Wadj[]/lengh)*eps
    W[14]=W[14]-(Wadj[]/lengh)*eps
    W[15]=W[15]-(Wadj[]/lengh)*eps
    W[16]=W[16]-(Wadj[]/lengh)*eps
    W[17]=W[17]-(Wadj[]/lengh)*eps
    B[0]=  B[1]-(Badj[]/lengh)*eps
    B[1]=  B[2]-(Badj[]/lengh)*eps
    B[2]=  B[3]-(Badj[]/lengh)*eps
    B[3]=  B[4]-(Badj[]/lengh)*eps
    B[4]=  B[5]-(Badj[]/lengh)*eps
    B[5]=  B[6]-(Badj[]/lengh)*eps
    B[6]=  B[7]-(Badj[]/lengh)*eps
    B[7]=  B[8]-(Badj[]/lengh)*eps
    middelta=(np.mean(W-c)+np.mean(B-d))/2
    return W,B,middelta, lengh

def train(set,eps):
    errold=ctt(set)
    errnew=0
    n=0
    H=[]
    while ctt(set)>0.0:#abs(errold-errnew)>0.01 and n<=10000:
        if errold-errnew<0:
            eps=eps/2
        a,b,change,leng =adjustment(set,eps)
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
    return a,b
print(train(tset2,20))
#print(adjustment(tset,0.1))
print(evalnn(tset2[0][0:3]))
print(evalnn(tset2[1][0:3]))
print(evalnn(tset2[2][0:3]))
print(ctt(tset2))
