from math import exp,pow,sqrt
from BuildLattice import buildLattice
from CalcPayOff import calcPayOff
def priceOptionBinCRR(Underlying:float,Strike:float,Rate:float,T:float,NumOfTimeSteps:int,Sigma:float,StrCallPut:str):
    """
    The function calculates a standard European option price by using
    the Cox-Ross-Rubinstein (CRR) model
    Ref: Cox, J. C.; Ross, S. A.; Rubinstein, M. (1979).
    "Option pricing: A simplified approach". Journal of Financial Economics,
    7 (3): 229. doi:10.1016/0304-405X(79)90015-1. 
    """
    dt=T/NumOfTimeSteps
    r=exp(Rate*dt)
    u=exp(Sigma*sqrt(dt))
    d=1/u
    q=(r-d)/(u-d)
    BinLatticeUnderlying=buildLattice(NumOfTimeSteps+1,"bin")
    BinLatticeUnderlying[0][0]=Underlying
    for Idx in range(NumOfTimeSteps):
        BinLatticeUnderlying[Idx+1][0]=BinLatticeUnderlying[Idx][0]*u
        BinLatticeUnderlying[Idx+1][1]=BinLatticeUnderlying[Idx][0]*d
        x=len(BinLatticeUnderlying[Idx+1])
        if x>2:
            for k in range(2,x+1):
                BinLatticeUnderlying[Idx+1][k-1]=BinLatticeUnderlying[Idx][k-2]*d

        del x
    BinLatticeOption=buildLattice(NumOfTimeSteps+1,"bin")
    for k in range(len(BinLatticeOption[NumOfTimeSteps])):
        BinLatticeOption[NumOfTimeSteps][k]=calcPayOff(BinLatticeUnderlying[NumOfTimeSteps][k],Strike,StrCallPut)
    for i in range(NumOfTimeSteps-1):
        Idx=NumOfTimeSteps-1-i
        for k in range(len(BinLatticeOption[Idx])):
            BinLatticeOption[Idx][k]=(1/r)*(q*BinLatticeOption[Idx+1][k]+(1-q)*BinLatticeOption[Idx+1][k+1])
        if Idx==1:
            BinLatticeOption[0][0]=(1/r)*(q*BinLatticeOption[1][0]+(1-q)*BinLatticeOption[1][1])
    OptionPrice=BinLatticeOption[0][0]
    return OptionPrice
