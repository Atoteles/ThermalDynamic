from OneEnsemble import *

def TempScan(Krange,Evolve_Num,ThermalizeTime,Lattice_Num):#对于给定温度范围进行演化，返回样本数组
    K_Num=size(Krange)
    m_samples=zeros((K_Num,Evolve_Num))
    for i in range(0,K_Num):
        m_samples[i,:]=Ensemble(Lattice_Num,Evolve_Num,ThermalizeTime,Krange[i])#m[i,:]是第i个温度系综采样的数组,温度行演化列
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