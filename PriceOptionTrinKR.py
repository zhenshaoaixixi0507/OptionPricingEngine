from math import exp,pow,sqrt
from BuildLattice import buildLattice
from CalcPayOff import calcPayOff

class PriceOptionTrinKRClass:
    def __init__(self, Underlying, Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,StrCallPut,OptionType):
        self.Underlying = Underlying
        self.Strike = Strike
        self.Rate=Rate
        self.T=T
        self.NumOfTimeSteps=NumOfTimeSteps
        self.Sigma=Sigma
        self.Lam=Lam
        self.StrCallPut=StrCallPut
        self.OptionType=OptionType

    def priceOptionTrinKR(self):

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
                if self.OptionType=="American":
                    TrinLatticeOption[Idx][k]=(1/r)*(q1*TrinLatticeOption[Idx+1][k]+q2*TrinLatticeOption[Idx+1][k+1]+q3*TrinLatticeOption[Idx+1][k+2])
                    I=calcPayOff(TrinLatticeUnderlying[Idx][k],self.Strike,self.StrCallPut)
                    TrinLatticeOption[Idx][k]=max(I,TrinLatticeOption[Idx][k])
                else:
                    TrinLatticeOption[Idx][k]=(1/r)*(q1*TrinLatticeOption[Idx+1][k]+q2*TrinLatticeOption[Idx+1][k+1]+q3*TrinLatticeOption[Idx+1][k+2])
            if Idx==1:
                TrinLatticeOption[0][0]=(1/r)*(q1*TrinLatticeOption[1][0]+q2*TrinLatticeOption[1][1]+q3*TrinLatticeOption[1][2])
        OptionPrice=TrinLatticeOption[0][0]
        Delta=(TrinLatticeOption[1][0]-TrinLatticeOption[1][2])/(TrinLatticeUnderlying[1][0]-TrinLatticeUnderlying[1][2])
        deltaS=(TrinLatticeUnderlying[1][0]-TrinLatticeUnderlying[1][2])/2
        Gamma=(TrinLatticeOption[1][0]+TrinLatticeOption[1][2]-2*TrinLatticeOption[1][1])/(deltaS*deltaS)
        return OptionPrice,Delta,Gamma
    def vegaCalculation(self,epsilon):
        sigmaOld=self.Sigma
        self.Sigma=sigmaOld+epsilon
        v1,d1,g1=self.priceOptionTrinKR()
        self.Sigma=sigmaOld-epsilon
        v2,d2,g2=self.priceOptionTrinKR()
        vega=(v1-v2)/(2*epsilon)
        self.Sigma=sigmaOld
        return vega
    def rhoCalculation(self,epsilon):
        rOld=self.Rate
        self.Rate=rOld+epsilon
        v1,d1,g1=self.priceOptionTrinKR()
        self.Rate=rOld-epsilon
        v2,d2,g2=self.priceOptionTrinKR()
        rho=(v1-v2)/(2*epsilon)
        self.Rate=rOld
        return rho

