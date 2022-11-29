from EnsembleMetro import *

Evolve_Num=2000
ThermalizeTime=2000
Lattice_Num=10
Ensemble_Num=1000
MM=zeros((Ensemble_Num,Evolve_Num))
for i in range(0,Ensemble_Num):
    m_samples1=EnsembleSingle(1/3,Evolve_Num,ThermalizeTime,Lattice_Num)
    M2=np.average(m_samples1)**2
    MM[i,:]=multiply(m_samples1[0],m_samples1)-M2#计算自关联函数
AutoCor=np.average(MM,0)#对于多条MarkovChain求平均
savetxt('./AutoCorMetro.csv',AutoCor,delimiter=',')
plot(range(0,size(AutoCor,0)),AutoCor)
show()