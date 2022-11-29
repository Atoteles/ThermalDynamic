from EnsembleMetro import *

Lattice_Num=100
bin_contain=Lattice_Num**2
Evolve_Num=2000
ThermalizeTime=2000

Trange=append(append(arange(1.5,2,0.05),arange(2.01,2.5,0.01)),arange(2.51,4,0.05))
Krange=1/Trange

def TempScan(Krange,Evolve_Num,ThermalizeTime,bin_contain,Lattice_Num):#对于给定温度范围进行演化，返回样本数组
    K_Num=size(Krange)
    m_samples=zeros((K_Num,Evolve_Num))
    for k in range(0,K_Num):
        m_samples[k,:]=Ensemble(Krange[k],Evolve_Num,ThermalizeTime,bin_contain,Lattice_Num)#m[i,:]是第i个温度系综采样的数组,温度行演化列
    return m_samples

def BinderRatio(m_samples):
    m4=Average(m_samples,4)
    m2=Average(m_samples,2)
    return 1.5*(1-divide(m4,3*np.power(m2,2)))

def DataCollapse(Krange,m_samples,Lattice_Num,eta,nu,Kc):
    D=2
    m=Average(m_samples,1)
    y=m*np.power(Lattice_Num,(D-2+eta)/2)
    x=(divide(Kc,Krange)-1)*np.power(Lattice_Num,1/nu)
    return [x,y]