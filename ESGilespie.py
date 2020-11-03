import numpy as np
import matplotlib.pyplot as plt
import math
import random
import numpy.random as npr
from random import randint
"""
E + S <-> ES -> E + P
"""

### Definition of the variables
k1=0.5
k2=1.5
k3=0.5
S0=200
E0=100
N=999
p = 1

### Init
t=np.zeros(N)
S=np.zeros(N)
E=np.zeros(N)
ES=np.zeros(N)
P=np.zeros(N)

S[0]=S0
E[0]=E0
ES[0]=0
P[0]=0

### Algo
for i in range(1, N):
    # 1 define the weights
    p1 = k1 * E[i-1] * S[i-1]
    p2 = k2 * ES[i-1]
    p3 = k3 * ES[i-1]
    # pr = k1 * E[i] * S[i] + k2 * ES[i] + k3 * ES[i]
    ptot = p1 + p2 + p3
    
    # 2 Pick the time of the next event
    r = random.random()
    tau = - 1/ptot * math.log(r) # tau = waiting time until next event
    
    # 3 Choose and realize the event 
    r2 = random.random() * ptot
    if r2 < p1:
        E[i] = E[i-1] - 1
        S[i] = S[i-1] - 1
        ES[i] = ES[i-1] + 1
        P[i] = P[i-1]
    elif r2 < p1 + p2:
        E[i] = E[i-1] + 1
        S[i] = S[i-1] + 1
        ES[i] = ES[i-1] - 1
        P[i] = P[i-1]
    else :
        E[i] = E[i-1] + 1
        S[i] = S[i-1]
        ES[i] = ES[i-1] - 1
        P[i] = P[i-1] + 1
        
    t[i] = t[i-1] + tau

plt.figure()
plt.plot(t, E)
plt.plot(t, ES, c="red")
plt.plot(t, S, c="black")
plt.plot(t, P, c="yellow")
plt.show()
