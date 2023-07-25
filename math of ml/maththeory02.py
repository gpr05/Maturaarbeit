'''for n in range (300):
    if ((364/365)**n<0.5):
        print(n)
        break
import numpy as np
import matplotlib.pylab as plt
#s=np.zeros((1000000,2))
w=[0,0]
for m in range(2,31):
    matches=0
    for n in range (1000000):
        match =0
        b=np.random.randint(0,364,m)
        for i in range(m):
            for j in range(m):
                if (i!=j) and (b[i]==b[j]):
                    match+=1
        if match!=0:
            matches+=1
    w.append(matches/1000000)
    #s[m-2]=[m,matches/1000000]
    print('%2d %0.6f'%(m,matches/1000000))
    #plt.plot(s)
    #plt.show()
plt.plot(w)
plt.show()
'''
import numpy as np
t=np.random.binomial(5,0.3,size=1000)
s=np.bincount(t)
print(s)
print(s/s.sum())
