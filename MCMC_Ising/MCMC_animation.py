import numpy as np
from pylab import *

def Initialize(L):
    spin = np.random.rand(L)
    spin[spin>0.5]=1
    spin[spin<=0.5]=-1
    return spin

def RandChoose(L):
    return np.random.randint(1,L)

def Acceptance(n,spin,J):
    if n==0:
        forth=spin[n+1]
        back=spin[L-1]
    elif n==L-1:
        forth=spin[0]
        back=spin[n-1]
    else:
        forth=spin[n+1]
        back=spin[n-1]
    dE=2*J*spin[n]*(forth+back)
    if dE<=0:
        return 1.
    else:
        return exp(-dE)

def Moveforth(n,acpt,spin):
    p=np.random.rand(1)
    if p<acpt:
        spin[n]=-spin[n]
        return spin
    else:
        return spin

def IntEnergy(L,spin,J):
    E=0
    for i in range(0,L-1):
        E=E-J*spin[i]*spin[i+1]
    return E-J*spin[L-1]*spin[0]

L=30
J=10
bin_contain=10
step=10
spin=Initialize(L)
print(spin)
Elist=zeros(step)

plt.ion()
for i in range(0,step):
    for j in range(0,bin_contain):
        n=RandChoose(L)
        print(n)
        spin=Moveforth(n,Acceptance(n,spin,J),spin)

        plt.cla()
        plt.title("Ising Model")
        plt.scatter(range(0,L),spin)
        plt.pause(0.1)

    Elist[i]=IntEnergy(L,spin,J)
    plt.pause(0.2)

E=sum(Elist)/step