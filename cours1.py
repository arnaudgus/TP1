import numpy as np
import matplotlib.pyplot as plt

# Parameters
a0 = 0.1    #growth rate
tau = 0.1   #time interval
nt = 1000   #nb of timepoints
N0 = 10     #initial nb of individuals

# Initialization
N = np.zeros(nt)
t = np.zeros(nt)
print(N, N.shape)

N[0] = N0
#print(N)

# Algorithm
for i in range(999):
    N[i+1] = N[i] + tau*a0*N[i]
    t[i+1] = t[i] + tau

#print(N)

#Visualization
plt.figure()
plt.plot(t,N)
plt.show()