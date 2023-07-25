import numpy as np
nb=0
N=1000000
for i in range(N):
    s=np.random.randint(0,50,3)
    fail=False
    for t in range(3):
        if s[t]<4:
            fail=True
        if not fail:
            nb+=1
print('no boston in the fall= %0.4f'%(nb/N,))
