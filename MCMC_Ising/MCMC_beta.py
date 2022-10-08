import numpy as np
from pylab import *

J=2
kB=1.38065e-23

def Initialize(L):
    spin = np.random.rand(L)
    spin[spin>0.5]=1
    spin[spin<=0.5]=-1
    return spin

def Acceptance(n,spin,b):
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
    return min(1.,exp(-dE*b))

def Moveforth(n,acpt,spin):
    p=np.random.rand(1)
    if p<acpt:
        spin[n]=-spin[n]
    return spin

def IntEnergy(L,spin):
    E=0
    for i in range(0,L-1):
        E=E-J*spin[i]*spin[i+1]
    return E-J*spin[L-1]*spin[0]

L=100
bin_contain=L
step=200000
abondon=1000

b_num=20
b_step=0.1
b_l=0
b_h=b_l+b_step*b_num
b=linspace(b_l,b_h,b_num)


E=zeros(b_num)
C=zeros(b_num-1)
G=zeros((b_num,L))

for k in range(0,b_num):
    print("b_num=",k)
    Elist=zeros(step)
    Glist=zeros((step,L))
    spin=Initialize(L)
    for i in range(-abondon,step):
        for j in range(0,bin_contain):
            n=np.random.randint(1,L)
            spin=Moveforth(n,Acceptance(n,spin,b[k]),spin)
        if i>=0:
            Elist[i]=IntEnergy(L,spin)
            Glist[i,:]=spin[0]*spin
    E[k]=sum(Elist)/step
    G[k,:]=sum(Glist,axis=0)/step
    if k!=0:
        C[k-1]=-(E[k]-E[k-1])/b_step*kB*b[k-1]**2
open('E.txt')
np.savetxt(fname="D:\外来文件\收\复旦\课程相关\大三上\热统2\作业\E.txt", X=E, fmt="%f",delimiter=",")
np.savetxt(fname="D:\外来文件\收\复旦\课程相关\大三上\热统2\作业\G.txt", X=G, fmt="%f",delimiter=",")
np.savetxt(fname="D:\外来文件\收\复旦\课程相关\大三上\热统2\作业\C.txt", X=C, fmt="%f",delimiter=",")
plt.subplot(1,3,1)
plt.plot(b,E)
plt.subplot(1,3,2)
plt.plot(b[0:-1],C)
# for i in range(0,b_num):
#     plt.plot(range(0,L),G[i,:])
plt.subplot(1,3,3)
plt.plot(range(0,L),G[0,:])
plt.plot(range(0,L),G[3,:])
plt.plot(range(0,L),G[b_num-1,:])
plt.show()