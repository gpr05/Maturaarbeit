import numpy as np
import matplotlib.pylab as plt

#erste versuch in training
#
#b=np.ones((6,1))
b=np.random.rand(6,1) #np.array([1,1,1,1,1,1])
#a=np.ones((9,1))#np.array([1,1,1,1,1,1,1,1,1])
a=np.random.rand(9,1)
                        #R                      G               B         re,li
tset=[[113.11902730375427,153.04650170648463,175.46373720136518,5.0,5.0],[175.0,175.0,175.0,5.0,2.0],[100.0,100.0,200.0,2.0,5.0]]
tset2=[[122,200,10,524.3120897791999, 533.6532256],[100, 100, 180,456.66741616, 510.14936],[20, 230, 18,352.413101372, 322.139278],[50, 50, 50, 202.74761647999998, 221.4676],[220, 130, 110, 704.902035172, 781.224002]]
#rgb zahlen/255
def evalnn(rgb):
    re=(rgb[0]*a[0]*b[0]+rgb[1]*a[1]*b[0]+rgb[2]*a[2]*b[0]+
        rgb[0]*a[3]*b[1]+rgb[1]*a[4]*b[1]+rgb[2]*a[5]*b[1]+
        rgb[0]*a[6]*b[2]+rgb[1]*a[7]*b[2]+rgb[2]*a[8]*b[2])
    li=(rgb[0]*a[0]*b[3]+rgb[1]*a[1]*b[3]+rgb[2]*a[2]*b[3]+
        rgb[0]*a[3]*b[4]+rgb[1]*a[4]*b[4]+rgb[2]*a[5]*b[4]+
        rgb[0]*a[6]*b[5]+rgb[1]*a[7]*b[5]+rgb[2]*a[8]*b[5])
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
    gradb=np.zeros((6,1))
    grada=np.zeros((9,1))
    re,li=evalnn(tval[0:3])
    gradb[0]=(re-ret)*(R*a[0]+G*a[1]+B*a[2])
    gradb[1]=(re-ret)*(R*a[3]+G*a[4]+B*a[5])
    gradb[2]=(re-ret)*(R*a[6]+G*a[7]+B*a[8])
    gradb[3]=(li-lit)*(R*a[0]+G*a[1]+B*a[2])
    gradb[4]=(li-lit)*(R*a[3]+G*a[4]+B*a[5])
    gradb[5]=(li-lit)*(R*a[6]+G*a[7]+B*a[8])

    grada[0]=(re-ret)*R*b[0]+(li-lit)*R*b[3]
    grada[1]=(re-ret)*G*b[0]+(li-lit)*G*b[3]
    grada[2]=(re-ret)*B*b[0]+(li-lit)*B*b[3]
    grada[3]=(re-ret)*R*b[1]+(li-lit)*R*b[4]
    grada[4]=(re-ret)*G*b[1]+(li-lit)*G*b[4]
    grada[5]=(re-ret)*B*b[1]+(li-lit)*B*b[4]
    grada[6]=(re-ret)*R*b[2]+(li-lit)*R*b[5]
    grada[7]=(re-ret)*G*b[2]+(li-lit)*G*b[5]
    grada[8]=(re-ret)*B*b[2]+(li-lit)*B*b[5]
    return grada, gradb

def gradctot(tval):

    gradbtot=np.zeros((6,1))
    gradatot=np.zeros((9,1))
    for i in tval :#range(3):
        grada, gradb =gradc(i)
        gradatot+=grada
        gradbtot+=gradb
        '''
        R=tval[i][0]
        G=tval[i][1]
        B=tval[i][2]
        ret=tval[i][3]
        lit=tval[i][4]
        re,li=evalnn(tval[i][0:3])
        gradbtot[0]+=(re-ret)*(R*a[0]+G*a[1]+B*a[2])+(li-lit)*0
        gradbtot[1]+=(re-ret)*(R*a[3]+G*a[4]+B*a[5])
        gradbtot[2]+=(re-ret)*(R*a[6]+G*a[7]+B*a[8])
        gradbtot[3]+=(li-lit)*(R*a[0]+G*a[1]+B*a[2])
        gradbtot[4]+=(li-lit)*(R*a[3]+G*a[4]+B*a[5])
        gradbtot[5]+=(li-lit)*(R*a[6]+G*a[7]+B*a[8])

        gradatot[0]+=(re-ret)*R*b[0]+(li-lit)*R*b[3]
        gradatot[1]+=(re-ret)*G*b[0]+(li-lit)*G*b[3]
        gradatot[2]+=(re-ret)*B*b[0]+(li-lit)*B*b[3]
        gradatot[3]+=(re-ret)*R*b[1]+(li-lit)*R*b[4]
        gradatot[4]+=(re-ret)*G*b[1]+(li-lit)*G*b[4]
        gradatot[5]+=(re-ret)*B*b[1]+(li-lit)*B*b[4]
        gradatot[6]+=(re-ret)*R*b[2]+(li-lit)*R*b[5]
        gradatot[7]+=(re-ret)*G*b[2]+(li-lit)*G*b[5]
        gradatot[8]+=(re-ret)*B*b[2]+(li-lit)*B*b[5]'''
    return gradatot, gradbtot

def adjustment(val,eps):
    c=a
    d=b
    tot=np.zeros((15,1))
    aadj,badj=gradctot(val)
    tot[0:9]=aadj
    tot[8:14]=badj
    lengh=np.linalg.norm(tot)
    a[0]= a[0]-(aadj[0]/lengh)*eps
    a[1]= a[1]-(aadj[1]/lengh)*eps
    a[2]= a[2]-(aadj[2]/lengh)*eps
    a[3]= a[3]-(aadj[3]/lengh)*eps
    a[4]= a[4]-(aadj[4]/lengh)*eps
    a[5]= a[5]-(aadj[5]/lengh)*eps
    a[6]= a[6]-(aadj[6]/lengh)*eps
    a[7]= a[7]-(aadj[7]/lengh)*eps
    a[8]= a[8]-(aadj[8]/lengh)*eps

    b[0]= b[0]-(badj[0]/lengh)*eps
    b[1]= b[1]-(badj[1]/lengh)*eps
    b[2]= b[2]-(badj[2]/lengh)*eps
    b[3]= b[3]-(badj[3]/lengh)*eps
    b[4]= b[4]-(badj[4]/lengh)*eps
    b[5]= b[5]-(badj[5]/lengh)*eps
    middelta=(np.mean(a-c)+np.mean(b-d))/2
    return a,b,middelta, lengh

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
