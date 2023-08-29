from math import exp
import numpy as np
import matplotlib.pylab as plt
import keyboard
import pandas

#erste versuch in training
#
W=np.random.rand(15,1)
B=np.random.rand(5,1)

                        #R                      G               B         re,li
tset=[[113.11902730375427,153.04650170648463,175.46373720136518,5.0,5.0],[175.0,175.0,175.0,5.0,2.0],[100.0,100.0,200.0,2.0,5.0]]
tset2=[[122,200,10,524.3120897791999, 533.6532256],[100, 100, 180,456.66741616, 510.14936],[20, 230, 18,352.413101372, 322.139278],[50, 50, 50, 202.74761647999998, 221.4676],[220, 130, 110, 704.902035172, 781.224002]]
tset3=[[187.3485634048458, 150.06230039857118, 102.96892854620899,0.91907491, 0.87311443],[78.35328219030872, 152.4715462721576, 156.86488887702208,0.91907492, 0.87311445],[157.808921335839, 210.7050624929489, 238.45021240253095,0.91907497, 0.87311453],[95.72308979813866, 69.5339003530957, 34.86122103755828,0.91904883, 0.87307573],[145.31661495820254, 205.17219401441102, 81.4888524227154,0.91907497, 0.87311453],[21.99138323403693, 0.9080220340470818, 4.861395253322934,0.91598381, 0.86853991],[4.798772151630699, 94.66655479513831, 166.37772931712823,0.91902879, 0.87304372],[48.68448631179256, 242.48245067741047, 29.121640100838867,0.91907497, 0.87311453],[101.74088348134059, 254.24763334186162, 41.89517926504668,0.91907497, 0.87311453],[215.81471642329257, 67.07490113186374, 154.17926522165655,0.9190436, 0.87306796],[207.18018572784592, 103.34557520876797, 179.33934217090905,0.91907286, 0.87311139],[232.71419262917715, 252.10125523653795, 211.6030212600609,0.91907497, 0.87311453],[88.72659772824302, 236.52813574120773, 241.72741756777222,0.91907497, 0.87311453],[245.13417070121412, 48.2736443745081, 80.13411875172542,0.91894898, 0.87292755],[83.33695419614408, 85.04281743840826, 251.54730622227348,0.91906672, 0.87310228],[43.02041691902869, 196.3968528461948, 41.9605439905398,0.91907497, 0.87311453],[130.92103087324773, 36.02059899979538, 18.261611179714738,0.91876701, 0.87265767],[2.0304526721220295, 234.31364912636212, 47.40802014943126,0.91870807, 0.87255075],[181.9982851516164, 69.01644049146817, 100.26327430780907,0.91904781, 0.87307421],[80.94246830415993, 229.94210277749943, 243.0721156436205,0.91907497, 0.87311453],[88.13055728784533, 243.92916722732556, 16.72057531226351,0.91907497, 0.87311452],[95.83047422751676, 208.84850575596346, 236.36610860614576,0.91907497, 0.87311453],[222.26540779003383, 43.37231635459465, 53.59488229780505,0.91889449, 0.87284672],[4.595469338667797, 35.504345976256275, 3.549408624566286,0.91851172, 0.87225095],[243.22777635743648, 4.015747369683181, 122.78596201017494,0.91652495, 0.86934568],[207.22753770217653, 163.61898652199272, 252.88927891476877,0.91907495, 0.87311449],[174.3446919475697, 30.24598169916302, 253.47102138798877,0.91860928, 0.87242388],[115.93032417605417, 133.09388111631773, 248.1879812074148,0.91907474, 0.87311419],[210.16618903906695, 148.5607035406906, 95.21163626690465,0.9190749, 0.87311442],[171.41077460145462, 208.26595338895507, 194.01400549814815,0.91907497, 0.87311453],[0.02220199930152489, 63.723517444334206, 140.1245783601545,0.91759599, 0.87085069],[129.74299326132677, 196.59662741756995, 237.3643309544332,0.91907497, 0.87311453],[252.0625146809579, 225.4135183110646, 58.83705181897425,0.91907497, 0.87311453],[153.5368283196219, 145.69883938079008, 79.43041888095915,0.91907488, 0.8731144],[97.80860376333571, 253.67246326018866, 89.48192726213767,0.91907497, 0.87311453],[73.56298602584683, 72.24198173485593, 189.80417514308533,0.9190536, 0.8730828],[11.676302003940698, 203.8506565554526, 221.13066091201628,0.9190748, 0.87311427],[224.50170188556052, 47.643922240160784, 88.85687376360117,0.91894301, 0.8729187],[6.477370554185351, 246.88750993277597, 68.30619454460314,0.91906401, 0.87309767],[105.56356201469399, 153.3193032220116, 19.514028307206534,0.91907492, 0.87311445],[47.780295573442245, 142.60152834663785, 249.0869064396774,0.91907486, 0.87311436],[229.70587188800454, 64.30982823876457, 232.33089218022857,0.91903646, 0.87305736],[202.5705936937251, 107.72086880887217, 128.93509210918455,0.91907345, 0.87311226],[135.3931992139662, 245.16377222393186, 49.156596592332484,0.91907497, 0.87311453],[185.34608958586307, 102.24525294246926, 126.73599159621352,0.91907268, 0.87311112],[90.89896174703694, 212.1301356620164, 160.2190349278552,0.91907497, 0.87311453],[68.23014877049839, 252.07468697010302, 129.94253883977015,0.91907497, 0.87311453],[80.5219092454006, 62.78278453304365, 96.80912341004907,0.91903184, 0.87305051],[111.09923305789182, 42.92697568096237, 125.83859953105464,0.91888852, 0.87283786],[165.91089108817184, 248.3098658763411, 174.39690420536905,0.91907497, 0.87311453],[177.09407069948102, 49.04719654918997, 95.55618018948584,0.91895594, 0.87293789],[1.448514956788295, 130.07052189996958, 195.8539170767631,0.91851246, 0.87225064],[141.5765993299457, 47.441812181737596, 73.89194722262295,0.91894103, 0.87291577],[125.23494575956067, 7.450298074212846, 24.905609594281092,0.9169758, 0.87000989],[40.45411737656982, 208.83954727318473, 101.04038167797748,0.91907497, 0.87311453],[117.98978475726406, 92.57780258332137, 150.75488326504086,0.91907026, 0.87310754],[32.43625364827867, 19.525812456596196, 44.32262547257196,0.91809646, 0.87166466],[121.74864907602317, 240.1222068313449, 168.74384271884608,0.91907497, 0.87311453],[48.38687360894213, 232.435285379906, 116.86249738179396,0.91907497, 0.87311453],[195.60955292963277, 158.02232989986254, 135.63479552795562,0.91907494, 0.87311448],[11.949686728108292, 246.60717820978726, 213.63209020715556,0.91907484, 0.87311432],[246.7190280082268, 55.110804426381115, 52.07929683287783,0.91899886, 0.87300157],[118.56120683915576, 115.011656377815, 58.014032408278325,0.91907409, 0.87311321],[219.01491236046945, 71.27519203287838, 0.943323204909034,0.91765768, 0.87082293],[159.71814846973848, 190.40794333513384, 97.50421299146811,0.91907497, 0.87311452],[226.20122086000066, 28.05986391737315, 247.0066969226717,0.91853145, 0.87230857],[66.20057424022684, 52.11559068828179, 107.65604843450329,0.91898002, 0.87297362],[142.413570761006, 234.540369001613, 62.10736323092478,0.91907497, 0.87311453],[3.7547572258783486, 160.8692674746242, 59.60865583599572,0.91897829, 0.87296586],[37.44766508380174, 222.55190897174214, 232.75644718044055,0.91907497, 0.87311453],[42.663511025953134, 21.39032540704388, 10.907771229966986,0.91821175, 0.87183517],[173.05479972025677, 202.2447732254836, 93.91925926954892,0.91907497, 0.87311453],[194.19181734021498, 40.70416852288664, 154.60861856994703,0.91885569, 0.87278917],[107.76938235912289, 135.6906666695157, 133.1322608266551,0.91907478, 0.87311425],[105.0893567683671, 71.25257308628701, 99.18894552077327,0.91905197, 0.87308038],[28.428591403734522, 83.48550667252691, 82.64884640995476,0.91906571, 0.87310078],[187.15371309033108, 0.10944185742192247, 155.69451070161816,0.91594375, 0.86849062],[57.56527817692119, 152.11904662128427, 236.43704345781853,0.91907492, 0.87311445],[247.1546266463841, 215.11205984843608, 135.0949740139031,0.91907497, 0.87311453],[158.14746122545031, 101.69499622108948, 115.93611781436847,0.91907258, 0.87311098],[103.74258942568402, 36.493258989345975, 50.40492011721464,0.91877734, 0.87267299],[25.356534760417983, 21.096040600623848, 93.80329622296767,0.91819483, 0.87181019],[34.338601598818634, 215.77177731658279, 69.79162213684815,0.91907497, 0.87311453],[34.76333545810881, 27.590610775657648, 100.4010268878899,0.91851321, 0.87228155],[140.12065508918278, 23.9898939785542, 138.02911582947746,0.91835302, 0.87204432],[106.79454808305456, 99.99156107414558, 233.02708322577976,0.91907226, 0.8731105],[84.05341309617337, 67.51940374650387, 86.13084169984224,0.91904462, 0.87306947],[137.99958314857102, 70.97705295645008, 224.39919671538416,0.91905149, 0.87307968],[182.0823248521584, 29.994312713603595, 188.96488856880094,0.91860089, 0.87241145],[49.337940496792704, 95.63677701529264, 248.05605322179937,0.91907122, 0.87310896],[2.159051763184517, 75.83469618695754, 8.965747246622938,0.91872257, 0.87257371],[17.662098244036965, 38.75130432866578, 40.18951765888448,0.91882224, 0.87273956],[87.90798272312465, 207.01631654940678, 225.75326668987083,0.91907497, 0.87311453],[232.20015089597553, 42.36456646651272, 110.54789207075262,0.9188807, 0.87282626],[40.64378643127257, 93.870310727955, 131.3303912664586,0.91907069, 0.87310818],[211.36350013163826, 149.8787747884856, 56.79951241293477,0.91907491, 0.87311443],[57.79715461543241, 95.35039658820244, 26.461591344577435,0.91907114, 0.87310884],[211.14274161578834, 59.98324811073504, 158.29669857544656,0.91902189, 0.87303575],[164.5319979219578, 12.99177539666716, 162.8901366571585,0.91757659, 0.87089631],[240.17137397052213, 222.0587288456426, 21.029810560685462,0.91907497, 0.87311453]]
tset4=[[46.14942747766261, 247.36208389705283, 74.08030744641174, 0.81659393, 0.91809978],[133.33315332807823, 117.71784034715313, 108.35543734187672, 0.81659393, 0.91809978],[197.66346409625467, 183.56815506745406, 134.3071830935232, 0.81659393, 0.91809978],[189.02759701085495, 82.06516146029526, 49.941384305976115, 0.81659393, 0.91809978],[207.77045285493006, 28.652714608810204, 117.00318360637586, 0.81659393, 0.91809978],[217.06198467287302, 254.42309173931255, 113.27118072812857, 0.81659393, 0.91809978],[200.69802924376225, 150.14609728332036, 24.68228158639408, 0.81659393, 0.91809978],[104.50758209407022, 213.72096341760204, 80.64609595214219, 0.81659393, 0.91809978],[234.60614035888858, 92.50591927648051, 169.84191157618739, 0.81659393, 0.91809978],[192.15905854374887, 23.788168811017936, 152.64503882316762, 0.81659393, 0.91809978],[135.02355074609744, 115.45833034239008, 125.95283619782644, 0.81659393, 0.91809978],[215.5057541073719, 221.50080521570374, 83.85481371566169, 0.81659393, 0.91809978],[183.52959442689735, 200.9138247697748, 135.5292693627817, 0.81659393, 0.91809978],[195.34023292787631, 123.34621893684788, 107.18389635903542, 0.81659393, 0.91809978],[179.6591004825346, 201.39125956349358, 241.52247183974075, 0.81659393, 0.91809978]]
#rgb zahlen/255
def f(x):
    return x#* 1/(1+exp(-x))#1/(1+e**(-10*x+5))

def fder(x):
    return 1#(exp(-x))/((1+exp(-x))**2)#(e**10*x+5)/((1+e**10*x+5)**2)

def H0pre(inp):
    return inp[0]*W[0]+inp[1]*W[1]+inp[2]*W[2]+B[0]

def H0(inp):
    return f(H0pre(inp))

def H1pre(inp):
    return inp[0]*W[3]+inp[1]*W[4]+inp[2]*W[5]+B[1]

def H1(inp):
    return f(H1pre(inp))

def H2pre(inp):
    return inp[0]*W[6]+inp[1]*W[7]+inp[2]*W[8]+B[2]

def H2(inp):
    return f(H2pre(inp))

def O0pre(inp):
    return float(H0(inp))*W[9]+float(H1(inp))*W[10]+float(H2(inp))*W[11]+B[3]

def O0(inp):
    return f(O0pre(inp))

def O1pre(inp):
    return float(H0(inp))*W[12]+float(H1(inp))*W[13]+float(H2(inp))*W[14]+B[4]

def O1(inp):
    return f(O1pre(inp))

def evalnn(inp):
    re=O0(inp)
    li=O1(inp)
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
    inp=[0.0,0.0,0.0]
    inp[0:3]=tval[0:3]
    ret=tval[3]
    lit=tval[4]
    gradW=np.zeros((15,1))
    gradB=np.zeros((5,1))
    re,li=evalnn(tval[0:3])

    gradW[0]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H0pre(inp)))*inp[0]*W[9]  +(li-lit)*float(fder(O1pre(inp)))*float(fder(H0pre(inp)))*inp[0]*W[12]
    gradW[1]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H0pre(inp)))*inp[1]*W[9]  +(li-lit)*float(fder(O1pre(inp)))*float(fder(H0pre(inp)))*inp[1]*W[12]
    gradW[2]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H0pre(inp)))*inp[2]*W[9]  +(li-lit)*float(fder(O1pre(inp)))*float(fder(H0pre(inp)))*inp[2]*W[12]
    gradW[3]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H1pre(inp)))*inp[0]*W[10] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H1pre(inp)))*inp[0]*W[13]
    gradW[4]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H1pre(inp)))*inp[1]*W[10] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H1pre(inp)))*inp[1]*W[13]
    gradW[5]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H1pre(inp)))*inp[2]*W[10] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H1pre(inp)))*inp[2]*W[13]
    gradW[6]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H2pre(inp)))*inp[0]*W[11] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H2pre(inp)))*inp[0]*W[14]
    gradW[7]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H2pre(inp)))*inp[1]*W[11] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H2pre(inp)))*inp[1]*W[14]
    gradW[8]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H2pre(inp)))*inp[2]*W[11] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H2pre(inp)))*inp[2]*W[14]

    gradW[9]= (re-ret)*float(fder(O0pre(inp)))*float(H0(inp))
    gradW[10]=(re-ret)*float(fder(O0pre(inp)))*float(H1(inp))
    gradW[11]=(re-ret)*float(fder(O0pre(inp)))*float(H2(inp))
    gradW[12]=(li-lit)*float(fder(O1pre(inp)))*float(H0(inp))
    gradW[13]=(li-lit)*float(fder(O1pre(inp)))*float(H1(inp))
    gradW[14]=(li-lit)*float(fder(O1pre(inp)))*float(H2(inp))

    gradB[0]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H0pre(inp)))*W[9]  +(li-lit)*float(fder(O1pre(inp)))*float(fder(H0pre(inp)))*W[12]
    gradB[1]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H1pre(inp)))*W[10] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H1pre(inp)))*W[13]
    gradB[2]= (re-ret)*float(fder(O0pre(inp)))*float(fder(H2pre(inp)))*W[11] +(li-lit)*float(fder(O1pre(inp)))*float(fder(H2pre(inp)))*W[14]
    gradB[3]= (re-ret)*float(fder(O0pre(inp)))
    gradB[4]= (li-lit)*float(fder(O1pre(inp)))
    return gradW, gradB
def gradctot(tval):

    gradWtot=np.zeros((15,1))
    gradBtot=np.zeros((5,1))
    for i in tval :#range(3):
        gradW, gradB =gradc(i)
        gradWtot+=gradW
        gradBtot+=gradB
    return gradWtot, gradBtot

def epschange(val,eps):
    tot=np.zeros((20,1))
    Wadj,Badj=gradctot(val)
    tot[:15]=Wadj
    tot[15:]=Badj
    lengh=np.linalg.norm(tot)
    Wnew=np.zeros((15,1))
    Bnew=np.zeros((5,1))
    Wnew[0:]=W[0:]
    Bnew[0:]=B[0:]
    Wnew[0]=W[0]-(Wadj[0]/lengh)*eps
    Wnew[1]=W[1]-(Wadj[1]/lengh)*eps
    Wnew[2]=W[2]-(Wadj[2]/lengh)*eps
    Wnew[3]=W[3]-(Wadj[3]/lengh)*eps
    Wnew[4]=  W[4]-(Wadj[4]/lengh)*eps
    Wnew[5]=  W[5]-(Wadj[5]/lengh)*eps
    Wnew[6]=  W[6]-(Wadj[6]/lengh)*eps
    Wnew[7]=  W[7]-(Wadj[7]/lengh)*eps
    Wnew[8]=  W[8]-(Wadj[8]/lengh)*eps
    Wnew[9]=  W[9]-(Wadj[9]/lengh)*eps
    Wnew[10]=W[10]-(Wadj[10]/lengh)*eps
    Wnew[11]=W[11]-(Wadj[11]/lengh)*eps
    Wnew[12]=W[12]-(Wadj[12]/lengh)*eps
    Wnew[13]=W[13]-(Wadj[13]/lengh)*eps
    Wnew[14]=W[14]-(Wadj[14]/lengh)*eps
    Bnew[0]=  B[0]-(Badj[0]/lengh)*eps
    Bnew[1]=  B[1]-(Badj[2]/lengh)*eps
    Bnew[2]=  B[2]-(Badj[2]/lengh)*eps
    Bnew[3]=  B[3]-(Badj[3]/lengh)*eps
    Bnew[4]=  B[4]-(Badj[4]/lengh)*eps
    return Wnew,Bnew
def adjustment(val,eps):
    Wold=np.zeros((15,1))
    Bold=np.zeros((5,1))
    Wold[0:]=W[0:]
    Bold[0:]=B[0:]
    tot=np.zeros((20,1))
    Wadj,Badj=gradctot(val)
    tot[0:15]=Wadj
    tot[15:20]=Badj
    lengh=np.linalg.norm(tot) #in a new function to determine Wheter to divide epsilon
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
    B[0]=  B[0]-(Badj[0]/lengh)*eps
    B[1]=  B[1]-(Badj[2]/lengh)*eps
    B[2]=  B[2]-(Badj[2]/lengh)*eps
    B[3]=  B[3]-(Badj[3]/lengh)*eps
    B[4]=  B[4]-(Badj[4]/lengh)*eps
    middelta=(np.mean(W-Wold)+np.mean(B-Bold))/2
    return W,B,middelta, lengh

def train(set,eps):
    errold=ctt(set)
    errnew=0
    W=None
    B=None
    n=0
    H=[]
    while ctt(set)>0.0 and keyboard.is_pressed('q')==False:# and n<100000 :#and eps>10**-10:#abs(errold-errnew)>0.01 and n<=10000:
        errnew=2*errold
        while errnew> errold:
            epschange(set,eps)
            errnew=ctt(set)
        errold=errnew
        errnew=ctt(set)
        W,B,change,leng =adjustment(set,eps)
        #pandas.
        print([n,change,float(errnew), leng, eps])
        H.append([float(errnew),leng])

        if n%500==0:
            plt.plot(H)
            plt.show()
        #print(H[n])
        n+=1
    plt.plot(H)
    plt.show()
    return W,B
print(train(tset4,0.01))
#print(adjustment(tset,0.1))
'''for i in tset3:
   print(evalnn(i[0:3]))'''
print(evalnn(tset4[1][0:3]))
print(evalnn(tset4[2][0:3]))
print(ctt(tset4))
