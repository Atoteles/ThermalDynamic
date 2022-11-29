import numpy as np
from pylab import *

#Metropolis算法结果
BinderSave=loadtxt('./results/BinderRatioMetro.csv',delimiter=',')
CollapseSave=loadtxt('./results/DataCollapseMetro.csv',delimiter=',')

Trange=BinderSave[0,:]
U1=BinderSave[1,:]
U2=BinderSave[2,:]
U3=BinderSave[3,:]

Tc=2.2
TTc1=(divide(Trange,Tc)-1)*np.power(10,1)
C1=CollapseSave[1,:]
TTc2=(divide(Trange,Tc)-1)*np.power(12,1)
C2=CollapseSave[3,:]
TTc3=(divide(Trange,Tc)-1)*np.power(15,1)
C3=CollapseSave[5,:]

figure
subplot(121)
plot(Trange,U1,'bo-',color='#3682be')
plot(Trange,U2,'bo-',color='#45a776')
plot(Trange,U3,'bo-',color='#f05326')
axvline(Tc)
xlabel('$T=\\frac{1}{K}$')
ylabel('U')
legend(['L=10','L=12','L=15'])

subplot(122)
plot(TTc1,C1,'bo-',color='#3682be')
plot(TTc2,C2,'bo-',color='#45a776')
plot(TTc3,C3,'bo-',color='#f05326')
legend(['L=10','L=12','L=15'])
xlabel('$tL^{\\frac{1}{\\nu}}$')
ylabel('$ML^{\\frac{D-2+\\eta}{2}}$')
show()

#Wolff算法结果
BinderSave=loadtxt('./results/BinderRatioWolff.csv',delimiter=',')
CollapseSave=loadtxt('./results/DataCollapseWolff.csv',delimiter=',')

Trange=BinderSave[0,:]
U1=BinderSave[1,:]
U2=BinderSave[2,:]
U3=BinderSave[3,:]

Tc=2.27
TTc1=(divide(Trange,Tc)-1)*np.power(10,1)
C1=CollapseSave[1,:]
TTc2=(divide(Trange,Tc)-1)*np.power(12,1)
C2=CollapseSave[3,:]
TTc3=(divide(Trange,Tc)-1)*np.power(15,1)
C3=CollapseSave[5,:]

figure
subplot(121)
plot(Trange,U1,'bo-',color='#3682be')
plot(Trange,U2,'bo-',color='#45a776')
plot(Trange,U3,'bo-',color='#f05326')
axvline(Tc)
xlabel('$T=\\frac{1}{K}$')
ylabel('U')
legend(['L=10','L=12','L=15'])

subplot(122)
plot(TTc1,C1,'bo-',color='#3682be')
plot(TTc2,C2,'bo-',color='#45a776')
plot(TTc3,C3,'bo-',color='#f05326')
legend(['L=10','L=12','L=15'])
xlabel('$tL^{\\frac{1}{\\nu}}$')
ylabel('$ML^{\\frac{D-2+\\eta}{2}}$')
show()

#两者自关联函数比较结果
Metro=loadtxt('./results/AutoCorMetro.csv',delimiter=',')
Wolff=loadtxt('./results/AutoCorWolff.csv',delimiter=',')
x1=range(0,size(Metro[0:800],0))
x2=range(0,size(Wolff[0:800],0))
figure
plot(x1,Metro[0:800],'bo-',color='#3682be')
plot(x2,Wolff[0:800],'bo-',color='#45a776')
legend(['Metropolis','Wolff'])
xlabel('$\\Delta t$')
ylabel('$\\langle M(t=0)M(t=0+\\Delta t)\\rangle-\\langle M\\rangle^2$')
show()