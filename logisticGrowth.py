import numpy as np
import matplotlib.pyplot as plt

a0 = 0.01
tau = 0.1 
N0 = 100
K = 50
nt = 1000

N = np.zeros(nt)
t = np.zeros(nt)
N[0] = N0

for i in range(999):
    N[i+1] = N[i] + tau*a0*N[i]*(K-N[i])
    t[i+1] = t[i] + tau
    
plt.figure()
plt.plot(t, N)
plt.show()


