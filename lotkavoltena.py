import numpy as np
import matplotlib.pyplot as plt

#Params
prey0 = 10
pred0 = 10
a = 1.1
b = 0.4
d = 0.1
g = 0.4
tau = 0.1 #
nt = 1000

Pr = np.zeros(nt)
Pd = np.zeros(nt)
t = np.zeros(nt)
Pr[0] = prey0
Pd[0] = pred0

for i in range(nt-1):
    Pr[i+1] = Pr[i] + tau*((Pr[i]*a) - (Pr[i]*b*Pd[i]))
    Pd[i+1] = Pd[i] + tau*(Pd[i]*(d*Pr[i]-g))
    t[i+1] = t[i] + tau
    
plt.figure()
 #, loc="lower right", title="Legend Title")
plt.plot(t, Pr)
plt.plot(t, Pd)
plt.colorbar()
plt.show()
