from math import exp,pow,sqrt
from BuildLattice import buildLattice
from CalcPayOff import calcPayOff
class PriceOptionTrinKRClass:
    def __init__(self, Underlying, Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,StrCallPut):
        self.Underlying = Underlying
        self.Strike = Strike
        self.Rate=Rate
        self.T=T
        self.NumOfTimeSteps=NumOfTimeSteps
        self.Sigma=Sigma
        self.Lam=Lam
        self.StrCallPut=StrCallPut

    def priceOptionTrinKR(self):
        """
        The function calculates a standard European option price by using
        the Cox-Ross-Rubinstein (CRR) model
        Ref: Cox, J. C.; Ross, S. A.; Rubinstein, M. (1979).
        "Option pricing: A simplified approach". Journal of Financial Economics,
        7 (3): 229. doi:10.1016/0304-405X(79)90015-1. 
        """
        dt=self.T/self.NumOfTimeSteps
        r=exp(self.Rate*dt)
        u=exp(self.Lam*self.Sigma*sqrt(dt))
        m=1
        d=exp(-self.Lam*self.Sigma*sqrt(dt))
        q1=1/(2*self.Lam*self.Lam)+((self.Rate-0.5*self.Sigma*self.Sigma)*sqrt(dt))/(2*self.Lam*self.Sigma)
        q2=1-1/(self.Lam*self.Lam)
        q3=1/(2*self.Lam*self.Lam)-((self.Rate-0.5*self.Sigma*self.Sigma)*sqrt(dt))/(2*self.Lam*self.Sigma)
    
        TrinLatticeUnderlying=buildLattice(self.NumOfTimeSteps+1,"trin")
        TrinLatticeUnderlying[0][0]=self.Underlying
        for Idx in range(self.NumOfTimeSteps):
            TrinLatticeUnderlying[Idx+1][0]=TrinLatticeUnderlying[Idx][0]*u
            TrinLatticeUnderlying[Idx+1][1]=TrinLatticeUnderlying[Idx][0]*m
            TrinLatticeUnderlying[Idx+1][2]=TrinLatticeUnderlying[Idx][0]*d
            x=len(TrinLatticeUnderlying[Idx+1])
            if x>3:
                for k in range(3,x+1):
                    TrinLatticeUnderlying[Idx+1][k-1]=TrinLatticeUnderlying[Idx][k-3]*d

            del x
        TrinLatticeOption=buildLattice(self.NumOfTimeSteps+1,"trin")
        for k in range(len(TrinLatticeOption[self.NumOfTimeSteps])):
            TrinLatticeOption[self.NumOfTimeSteps][k]=calcPayOff(TrinLatticeUnderlying[self.NumOfTimeSteps][k],self.Strike,self.StrCallPut)
        for i in range(self.NumOfTimeSteps-1):
            Idx=self.NumOfTimeSteps-1-i
            for k in range(len(TrinLatticeOption[Idx])):
                TrinLatticeOption[Idx][k]=(1/r)*(q1*TrinLatticeOption[Idx+1][k]+q2*TrinLatticeOption[Idx+1][k+1]+q3*TrinLatticeOption[Idx+1][k+2])
            if Idx==1:
                TrinLatticeOption[0][0]=(1/r)*(q1*TrinLatticeOption[1][0]+q2*TrinLatticeOption[1][1]+q3*TrinLatticeOption[1][2])
        OptionPrice=TrinLatticeOption[0][0]
        return OptionPrice
