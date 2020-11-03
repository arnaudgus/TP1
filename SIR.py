import numpy as np
import matplotlib.pyplot as plt

b = 0.4
G = 0.04
tau = 0.1 
S0 = 9980
I0 = 3
R0 = 0

nt = 1000

S = np.zeros(nt)
R = np.zeros(nt)
I = np.zeros(nt)
t = np.zeros(nt)
I[0] = I0
S[0] = S0
R[0] = R0

for i in range(999):
    Ni = S[i]+I[i]+R[i]
    S[i+1] = S[i] + tau*((-b*I[i]*S[i])/Ni)
    I[i+1] = I[i] + tau*(((b*I[i]*S[i])/Ni)-(G*I[i]))
    R[i+1] = R[i] + tau*(G * I[i])
    t[i+1] = t[i] + tau
    
fig, ax = plt.subplots()
 #, loc="lower right", title="Legend Title")
ax.plot(t, S, color ="blue", label="S - 'infectables'")
ax.plot(t, I, color ="red", label="I - 'infectés'")
ax.plot(t, R, color ="yellow", label="R - 'removed")
leg = ax.legend()
plt.show()