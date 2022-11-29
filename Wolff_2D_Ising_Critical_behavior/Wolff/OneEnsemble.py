from OneStepDynamics import *

def Ensemble(Lattice_Num,Evolve_Num,ThermalizeTime,K):
    Lattice=InitializeLattice(Lattice_Num)
    Lattice_Copy=Lattice[:,:,0].copy()
    m=[]

    therm_print=0
    Evolve_print=0
    for i in range(0,Evolve_Num+ThermalizeTime):#固定一个温度，不断进行演化
        Lattice=Onestep(Lattice,Lattice_Copy,K,Draw=False)
        if i>=ThermalizeTime:#采样点个数就等于EvolveNum
            m.append(abs(sum(Lattice[:,:,0])))#计算总磁矩，加入存储样本的数组
            if Evolve_print==0:
                print('(T,L)=(',1/K,',',Lattice_Num,') Evolving')
                Evolve_print=1
        elif therm_print==0:
            print('(T,L)=(',1/K,',',Lattice_Num,') Thermalizing')
            therm_print=1
    return m

def Average(m_sample,Power):#工具函数，用来求M的几次方的平均值
    K_Num=size(m_sample,0)
    ave=zeros(K_Num)
    for i in range(0,K_Num):
        ave[i]=np.average(np.power(m_sample[i,:],Power))
    return ave