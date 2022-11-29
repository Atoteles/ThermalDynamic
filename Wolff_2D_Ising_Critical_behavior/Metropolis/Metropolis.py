from TempScanMetro import *
Evolve_Num=500000
ThermalizeTime=500000
Trange=append(append(arange(1.5,2.1,0.05),arange(2.11,2.3,0.01)),arange(2.31,4,0.05))#T_c附近采样点增多
Krange=1/Trange
LatticeRange=[10,12,15]
#MCMC演化
m_samples1=TempScan(Krange,Evolve_Num,ThermalizeTime,LatticeRange[0]**2,LatticeRange[0])
m_samples2=TempScan(Krange,Evolve_Num,ThermalizeTime,LatticeRange[1]**2,LatticeRange[1])
m_samples3=TempScan(Krange,Evolve_Num,ThermalizeTime,LatticeRange[2]**2,LatticeRange[2])
#计算BinderRatio
U1=BinderRatio(m_samples1)
U2=BinderRatio(m_samples2)
U3=BinderRatio(m_samples3)
#计算数据跌落
Kc=1/2.2
eta=0.25
nu=1
Col1=DataCollapse(Krange,m_samples1,LatticeRange[0],eta,nu,Kc)
Col2=DataCollapse(Krange,m_samples1,LatticeRange[1],eta,nu,Kc)
Col3=DataCollapse(Krange,m_samples1,LatticeRange[2],eta,nu,Kc)
#保存BinderRatio数据
BinderSave=[]
BinderSave.append(Trange)
BinderSave.append(U1)
BinderSave.append(U2)
BinderSave.append(U3)
savetxt('./BinderRatioMetro.csv',BinderSave,delimiter=',')
#保存数据跌落数据
CollapseSave=[]
CollapseSave.append(Col1[0])
CollapseSave.append(Col1[1])
CollapseSave.append(Col2[0])
CollapseSave.append(Col2[1])
CollapseSave.append(Col3[0])
CollapseSave.append(Col3[1])
savetxt('./DataCollapseMetro.csv',CollapseSave,delimiter=',')
#初步绘图
figure
subplot(121)
plot(Trange,U1,'bo-',color='red')
plot(Trange,U2,'bo-',color='blue')
plot(Trange,U3,'bo-',color='green')

subplot(122)
plot(Col1[0],Col1[1],'bo-',color='red')
plot(Col2[0],Col2[1],'bo-',color='blue')
plot(Col3[0],Col3[1],'bo-',color='green')
show()