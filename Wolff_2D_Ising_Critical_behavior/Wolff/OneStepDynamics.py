import numpy as np
from pylab import *

def InitializeLattice(Lattice_Num):#初始化晶格，[:,:,0]是自旋取值，[:,:,1]是是否被激活的flag
    spin = np.random.rand(Lattice_Num,Lattice_Num)
    spin[spin>0.5]=1
    spin[spin<=0.5]=-1
    Lattice=zeros((Lattice_Num,Lattice_Num,2))
    Lattice[:,:,0]=spin
    return Lattice

def ChooseStartPoint(Lattice_Num):#选择初始点
    return np.random.randint(Lattice_Num,size=(1,2))

def Activate(sigmax,sigmay,K):#判断是否激活某条bond
    if abs(sigmax)!=1 or abs(sigmay)!=1:
        print("spin value error.")
        return
    p=np.random.rand(1)
    Limit=max(1-exp(-2*K*sigmax*sigmay),0)
    if p<Limit:
        return True
    else:
        return False

def ProceedAround(Prex,Prey,NextLevel,Dirc,Lattice,Lattice_Copy,K):#探索某个点的上下左右四个bond是否激活
    Lattice_Num=size(Lattice,0)
    if Dirc==1:#上 周期性边条
        Nextx=Prex
        if Prey==0:
            Nexty=Lattice_Num-1
        else:
            Nexty=Prey-1
    elif Dirc==2:#下 周期性边条
        Nextx=Prex
        if Prey==Lattice_Num-1:
            Nexty=0
        else:
            Nexty=Prey+1
    elif Dirc==3:#左 周期性边条
        Nexty=Prey
        if Prex==0:
            Nextx=Lattice_Num-1
        else:
            Nextx=Prex-1
    elif Dirc==4:#右 周期性边条
        Nexty=Prey
        if Prex==Lattice_Num-1:
            Nextx=0
        else:
            Nextx=Prex+1
    if Lattice[Nextx,Nexty,1]!=1:
            Next_sigma=Lattice[Nextx,Nexty,0]
            Pre_sigma=Lattice[Prex,Prey,0]
            if Activate(Pre_sigma,Next_sigma,K):#如果激活，加入下一层的数组
                NextLevel[0].append(Nextx)
                NextLevel[1].append(Nexty)
                Lattice_Copy[Nextx,Nexty]=-Lattice_Copy[Nextx,Nexty]
                Lattice[Nextx,Nexty,1]=1

def Proceed(PresentLevel,Lattice,Lattice_Copy,K):#输入现在的待激活列表，输出下一层待激活列表
    #PresentLevel有N行2列，第一列为横坐标，第二列为纵坐标
    N=size(PresentLevel,1)
    NextLevel=[[],[]]
    for i in range(0,N):
        Prex=PresentLevel[0][i]
        Prey=PresentLevel[1][i]
        for Dirc in range(1,5):
            ProceedAround(Prex,Prey,NextLevel,Dirc,Lattice,Lattice_Copy,K)
    return NextLevel

def Onestep(Lattice,Lattice_Copy,K,Draw):#单步演化的封装函数
    if Draw==True:
        ion()
        cla()
        imshow(Lattice[:,:,0])
        pause(10)

    Lattice_Num=size(Lattice,1)
    Start_Point=ChooseStartPoint(Lattice_Num)
    NextLevel=[[Start_Point[0,0]],[Start_Point[0,1]]]
    Lattice_Copy[Start_Point[0,0],Start_Point[0,1]]=-Lattice_Copy[Start_Point[0,0],Start_Point[0,1]]
    Lattice[Start_Point[0,0],Start_Point[0,1],1]=1
    while size(NextLevel,1)!=0:#当待激活列表不为空时
        NextLevel=Proceed(NextLevel,Lattice,Lattice_Copy,K)
    Lattice[:,:,0]=Lattice_Copy
    Lattice[:,:,1]=zeros((Lattice_Num,Lattice_Num))

    return Lattice