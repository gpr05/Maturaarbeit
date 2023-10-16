from math import exp
import numpy as np
import matplotlib.pylab as plt
import keyboard

Wg=np.random.rand(15,1)
Bg=np.random.rand(5,1)

tset4=[[46.14942747766261, 247.36208389705283, 74.08030744641174, 0.81659393, 0.91809978],[133.33315332807823, 117.71784034715313, 108.35543734187672, 0.81659393, 0.91809978],
       [197.66346409625467, 183.56815506745406, 134.3071830935232, 0.81659393, 0.91809978],[189.02759701085495, 82.06516146029526, 49.941384305976115, 0.81659393, 0.91809978],
       [207.77045285493006, 28.652714608810204, 117.00318360637586, 0.81659393, 0.91809978],[217.06198467287302, 254.42309173931255, 113.27118072812857, 0.81659393, 0.91809978],
       [200.69802924376225, 150.14609728332036, 24.68228158639408, 0.81659393, 0.91809978],[104.50758209407022, 213.72096341760204, 80.64609595214219, 0.81659393, 0.91809978],
       [234.60614035888858, 92.50591927648051, 169.84191157618739, 0.81659393, 0.91809978],[192.15905854374887, 23.788168811017936, 152.64503882316762, 0.81659393, 0.91809978],
       [135.02355074609744, 115.45833034239008, 125.95283619782644, 0.81659393, 0.91809978],[215.5057541073719, 221.50080521570374, 83.85481371566169, 0.81659393, 0.91809978],
       [183.52959442689735, 200.9138247697748, 135.5292693627817, 0.81659393, 0.91809978],[195.34023292787631, 123.34621893684788, 107.18389635903542, 0.81659393, 0.91809978],
       [179.6591004825346, 201.39125956349358, 241.52247183974075, 0.81659393, 0.91809978]]

def f(x):
    return 1/(1+exp(-x))

def fder(x):
    return (exp(-x))/((1+exp(-x))**2)
def H0pre(inp,W,B):
    return inp[0]*W[0]+inp[1]*W[1]+inp[2]*W[2]+B[0]

def H0(inp,W,B):
    return f(H0pre(inp,W,B))

def H1pre(inp,W,B):
    return inp[0]*W[3]+inp[1]*W[4]+inp[2]*W[5]+B[1]

def H1(inp,W,B):
    return f(H1pre(inp,W,B))

def H2pre(inp,W,B):
    return inp[0]*W[6]+inp[1]*W[7]+inp[2]*W[8]+B[2]

def H2(inp,W,B):
    return f(H2pre(inp,W,B))

def O0pre(inp,W,B):
    return float(H0(inp,W,B))*W[9]+float(H1(inp,W,B))*W[10]+float(H2(inp,W,B))*W[11]+B[3]

def O0(inp,W,B):
    return f(O0pre(inp,W,B))

def O1pre(inp,W,B):
    return float(H0(inp,W,B))*W[12]+float(H1(inp,W,B))*W[13]+float(H2(inp,W,B))*W[14]+B[4]

def O1(inp,W,B):
    return f(O1pre(inp,W,B))

def evalnn(inp,W,B):
    re=O0(inp,W,B)
    li=O1(inp,W,B)
    return re,li

def c(tval,W,B):
    re,li=evalnn(tval[0:3],W,B)
    return 0.5*(re-tval[3])**2+0.5*(li-tval[4])**2

def ctt(tval,W,B):
    ct=0
    for val in tval:
        ct+=c(val,W,B)
    return ct

def gradc(tval,W,B):
    inp=[0.0,0.0,0.0]
    inp[0:3]=tval[0:3]
    ret=tval[3]
    lit=tval[4]
    gradW=np.zeros((15,1))
    gradB=np.zeros((5,1))
    re,li=evalnn(tval[0:3],W,B)

    gradW[0]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*inp[0]*W[9]  +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*inp[0]*W[12]
    gradW[1]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*inp[1]*W[9]  +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*inp[1]*W[12]
    gradW[2]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*inp[2]*W[9]  +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*inp[2]*W[12]
    gradW[3]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*inp[0]*W[10] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*inp[0]*W[13]
    gradW[4]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*inp[1]*W[10] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*inp[1]*W[13]
    gradW[5]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*inp[2]*W[10] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*inp[2]*W[13]
    gradW[6]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*inp[0]*W[11] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*inp[0]*W[14]
    gradW[7]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*inp[1]*W[11] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*inp[1]*W[14]
    gradW[8]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*inp[2]*W[11] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*inp[2]*W[14]

    gradW[9]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(H0(inp,W,B))
    gradW[10]=(re-ret)*float(fder(O0pre(inp,W,B)))*float(H1(inp,W,B))
    gradW[11]=(re-ret)*float(fder(O0pre(inp,W,B)))*float(H2(inp,W,B))
    gradW[12]=(li-lit)*float(fder(O1pre(inp,W,B)))*float(H0(inp,W,B))
    gradW[13]=(li-lit)*float(fder(O1pre(inp,W,B)))*float(H1(inp,W,B))
    gradW[14]=(li-lit)*float(fder(O1pre(inp,W,B)))*float(H2(inp,W,B))

    gradB[0]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*W[9] +(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H0pre(inp,W,B)))*W[12]
    gradB[1]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*W[10]+(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H1pre(inp,W,B)))*W[13]
    gradB[2]= (re-ret)*float(fder(O0pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*W[11]+(li-lit)*float(fder(O1pre(inp,W,B)))*float(fder(H2pre(inp,W,B)))*W[14]
    gradB[3]= (re-ret)*float(fder(O0pre(inp,W,B)))
    gradB[4]= (li-lit)*float(fder(O1pre(inp,W,B)))
    return gradW, gradB

def gradctot(tval,W,B):
    gradWtot=np.zeros((15,1))
    gradBtot=np.zeros((5,1))
    for i in tval :
        gradW, gradB =gradc(i,W,B)
        gradWtot+=gradW
        gradBtot+=gradB
    return gradWtot, gradBtot

def adjustment(val,eps,Wadj,Badj):
    global Wg,Bg
    W=np.zeros((15,1))
    B=np.zeros((5,1))
    tot=np.zeros((20,1))

    tot[0:15]=Wadj
    tot[15:20]=Badj
    lengh=np.linalg.norm(tot)
    W[0]=Wg[0]-(Wadj[0]/lengh)*eps
    W[1]=Wg[1]-(Wadj[1]/lengh)*eps
    W[2]=Wg[2]-(Wadj[2]/lengh)*eps
    W[3]=Wg[3]-(Wadj[3]/lengh)*eps
    W[4]=  Wg[4]-(Wadj[4]/lengh)*eps
    W[5]=  Wg[5]-(Wadj[5]/lengh)*eps
    W[6]=  Wg[6]-(Wadj[6]/lengh)*eps
    W[7]=  Wg[7]-(Wadj[7]/lengh)*eps
    W[8]=  Wg[8]-(Wadj[8]/lengh)*eps
    W[9]=  Wg[9]-(Wadj[9]/lengh)*eps
    W[10]=Wg[10]-(Wadj[10]/lengh)*eps
    W[11]=Wg[11]-(Wadj[11]/lengh)*eps
    W[12]=Wg[12]-(Wadj[12]/lengh)*eps
    W[13]=Wg[13]-(Wadj[13]/lengh)*eps
    W[14]=Wg[14]-(Wadj[14]/lengh)*eps
    B[0]=  Bg[0]-(Badj[0]/lengh)*eps
    B[1]=  Bg[1]-(Badj[2]/lengh)*eps
    B[2]=  Bg[2]-(Badj[2]/lengh)*eps
    B[3]=  Bg[3]-(Badj[3]/lengh)*eps
    B[4]=  Bg[4]-(Badj[4]/lengh)*eps
    middelta=(np.mean(Wg-W)+np.mean(Bg-B))/2
    return W,B, middelta, lengh

def train(set):
    global Wg,Bg
    W=np.zeros((15,1))
    B=np.zeros((5,1))
    leng=None
    change=None
    n=0
    eps=1
    H=[]
    errold=ctt(set,Wg,Bg)
    errnew=2*errold
    while ctt(set,Wg,Bg)>1e-35 and keyboard.is_pressed('q')==False and eps>=1e-100:
        Wadj,Badj=gradctot(set,Wg,Bg)
        eps=1
        while errnew>=errold and eps>=1e-100:
            W,B,change,leng=adjustment(set, eps,Wadj,Badj)
            errnew=ctt(set,W,B)
            eps/=2

        Wg[0:]=W[0:]
        Bg[0:]=B[0:]
        errold=errnew
        errnew=ctt(set,Wg,Bg)
        print([n,change,float(errnew), leng, eps])
        H.append([float(errnew),leng, eps])

        if n%1000==0 and n!=0:
            plt.plot(H[-1000:])
            plt.legend(['error','leng','eps'])
            plt.show()
        n+=1
    plt.plot(H)
    plt.legend(['error','leng','eps'])
    plt.show()
    return W,B
print(train(tset4))
print(evalnn(tset4[1][0:3],Wg,Bg))
print(evalnn(tset4[2][0:3],Wg,Bg))
print(ctt(tset4,Wg,Bg))
