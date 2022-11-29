from OnestepMetro import *

def Ensemble(K,Evolve_Num,ThermalizeTime,bin_contain,Lattice_Num):
    spin=InitializeLattice(Lattice_Num)
    m=[]

    therm_print=0
    Evolve_print=0
    for i in range(0,Evolve_Num+ThermalizeTime):#固定一个温度，不断进行演化
        spin=OneBin(bin_contain,Lattice_Num,K,spin)
        if i>=ThermalizeTime:#采样点个数就等于EvolveNum
            m.append(abs(sum(spin)))#计算总磁矩，加入存储样本的数组
            if Evolve_print==0:
                print('(K,L)=(',K,',',Lattice_Num,') Evolving')
                Evolve_print=1
        elif therm_print==0:
            print('(K,L)=(',K,',',Lattice_Num,') Thermalizing')
            therm_print=1
    return m

def EnsembleSingle(K,Evolve_Num,ThermalizeTime,Lattice_Num):#为了计算自关联函数而设置的单步作为1bin的系综采样函数
    spin=InitializeLattice(Lattice_Num)
    m=[]

    therm_print=0
    Evolve_print=0
    for i in range(0,Evolve_Num+ThermalizeTime):
        spin=Onestep(Lattice_Num,K,spin)
        if i>=ThermalizeTime:
            m.append(abs(sum(spin)))
            if Evolve_print==0:
                print('(K,L)=(',K,',',Lattice_Num,') Evolving')
                Evolve_print=1
        elif therm_print==0:
            print('(K,L)=(',K,',',Lattice_Num,') Thermalizing')
            therm_print=1
    return m

def Average(m_sample,Power):#工具函数，用来求M的几次方的平均值
    K_Num=size(m_sample,0)
    ave=zeros(K_Num)
    for i in range(0,K_Num):
        ave[i]=np.average(np.power(m_sample[i,:],Power))
    return ave