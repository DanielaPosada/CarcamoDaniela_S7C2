import numpy as np
import matplotlib.pyplot as plt 

archivo=np.genfromtxt("CircuitoRC.txt",delimiter=" ",skip_header=0)
N=np.shape(archivo)
print N
C=0
v0=10
RCal=np.ones(N[0])
qmax=v0*C
chi=0
nuevo=0
def Chi(calculado,original,chi):
	for i in range(N[0]):
		nuevo=(calculado[i]-original[i,1])**2
		chi=nuevo+chi
	return chi
L=0	
def El(chi):
	np.exp(-0.5*chi)
	return L




plt.figure()
plt.scatter(archivo[:,0],archivo[:,1])
#plt.show()
plt.savefig("CargaRC.pdf")




























