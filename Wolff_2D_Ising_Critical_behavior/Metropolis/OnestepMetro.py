import numpy as np
from pylab import *

def InitializeLattice(Lattice_Num):#初始化晶格
    spin = np.random.rand(Lattice_Num,Lattice_Num)
    spin[spin>0.5]=1
    spin[spin<=0.5]=-1
    return spin

def Acceptance(Prex,Prey,spin,K,Lattice_Num):#判断是否接受翻转的提议
    if Prex==0:#上下左右周期性边条
        right=spin[Prex+1,Prey]
        left=spin[Lattice_Num-1,Prey]
    elif Prex==Lattice_Num-1:
        right=spin[0,Prey]
        left=spin[Prex-1,Prey]
    else:
        right=spin[Prex+1,Prey]
        left=spin[Prex-1,Prey]

    if Prey==0:
        bottom=spin[Prex,Prey+1]
        top=spin[Prex,Lattice_Num-1]
    elif Prey==Lattice_Num-1:
        bottom=spin[Prex,0]
        top=spin[Prex,Prey-1]
    else:
        bottom=spin[Prex,Prey+1]
        top=spin[Prex,Prey-1]
    dE=2*spin[Prex,Prey]*(right+left+bottom+top)#计算邻域能量改变
    return min(1.,exp(-dE*K))

def Moveforth(Prex,Prey,acpt,spin):#若接受则翻转
    p=np.random.rand(1)
    if p<acpt:
        spin[Prex,Prey]=-spin[Prex,Prey]
    return spin

def OneBin(bin_contain,Lattice_Num,K,spin):#根据自关联时间，L^2步划为1bin作为一个样本
    for j in range(0,bin_contain):
        Prex=np.random.randint(1,Lattice_Num)
        Prey=np.random.randint(1,Lattice_Num)
        spin=Moveforth(Prex,Prey,Acceptance(Prex,Prey,spin,K,Lattice_Num),spin)
        return spin

def Onestep(Lattice_Num,K,spin):#为了得到自关联函数而设置的每步演化函数
    Prex=np.random.randint(1,Lattice_Num)
    Prey=np.random.randint(1,Lattice_Num)
    spin=Moveforth(Prex,Prey,Acceptance(Prex,Prey,spin,K,Lattice_Num),spin)
    return spin