import numpy as np
import matplotlib.pyplot as plt 

archivo=np.genfromtxt("CircuitoRC.txt",delimiter=" ",skip_header=0)
N=np.shape(archivo)
print N
C=0
v0=10
RCal=np.ones(N[0])

def Chi(calculado,original):
	chin=0
	#nuevo=0
	for i in range(N[0]):
		nuevo=(calculado[i]-original[i])**2
		chin=nuevo+chin
	return chin/10000
def El(chin1):
	L=0
	L=np.exp(-0.5*chin1)
	return L
def nuevoModelo(tiempo,R,C):
	y=0
	y=(v0*C)-(v0*C)*(-np.exp(-tiempo/(R*C)))
	#print -tiempo/(R*C)
	return y


itera=1000
R1=np.ones(itera)
C1=np.ones(itera)
L1=np.ones(itera)
j=0
while(j<itera):
	R1[j]=np.random.rand(1)*20
	C1[j]=np.random.rand(1)*20
	j+=1
j=0

yinicial=np.ones(N[0])
for i in range(N[0]):
	yinicial[i]=nuevoModelo(archivo[i,0],R1[0],C1[0])

chi1=Chi(yinicial,archivo[:,1])
L1[0]=El(chi1)

for i in range(itera):
	Rprim=np.random.normal(R1[i],0.1)
	Cprim=np.random.normal(C1[i],0.1)
	
	yprimo1=np.ones(N[0])
	yinicial=np.ones(N[0])
	for k in range(N[0]):
		yinicial[k]=nuevoModelo(archivo[k,0],R1[k],C1[k])
		yprimo1[k]=nuevoModelo(archivo[k,0],Rprim,Cprim)
	chiI=Chi(yinicial,archivo[:,1])
	chiprim=Chi(yprimo1,archivo[:,1])
	lini=El(chiI)
	lprim=El(chiprim)
	alfa=lprim/lini
	if (alfa>=1.0):
		R1[i]=Rprim
		C1[i]=Cprim
		L1[i]=lprim
	else:
		b=np.random.rand(1)
		if (b<=alfa):
			R1[i]=Rprim
			C1[i]=Cprim
			L1[i]=lprim
		else:
			R1[i]=R1[i]
			C1[i]=C1[i]
			L1[i]=lini



plt.figure()
plt.scatter(R1,C1)
#plt.scatter(archivo[:,0],archivo[:,1])
plt.figure()
plt.scatter(R1,-np.log(L1))
plt.figure()
plt.scatter(C1,-np.log(L1))
plt.show()

#plt.savefig("CargaRC.pdf")




























