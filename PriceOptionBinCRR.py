from math import exp,pow,sqrt
from BuildLattice import buildLattice
from CalcPayOff import calcPayOff
class PriceOptionBinCRRClass:
    def __init__(self, Underlying, Strike,Rate,T,NumOfTimeSteps,Sigma,StrCallPut,OptionType):
        self.Underlying = Underlying
        self.Strike = Strike
        self.Rate=Rate
        self.T=T
        self.NumOfTimeSteps=NumOfTimeSteps
        self.Sigma=Sigma
        self.StrCallPut=StrCallPut
        self.OptionType=OptionType
    
    def priceOptionBinCRR(self):     
        dt=self.T/self.NumOfTimeSteps
        r=exp(self.Rate*dt)
        u=exp(self.Sigma*sqrt(dt))
        d=1/u
        q=(r-d)/(u-d)
        BinLatticeUnderlying=buildLattice(self.NumOfTimeSteps+1,"bin")
        BinLatticeUnderlying[0][0]=self.Underlying
        for Idx in range(self.NumOfTimeSteps):
            BinLatticeUnderlying[Idx+1][0]=BinLatticeUnderlying[Idx][0]*u
            BinLatticeUnderlying[Idx+1][1]=BinLatticeUnderlying[Idx][0]*d
            x=len(BinLatticeUnderlying[Idx+1])
            if x>2:
                for k in range(2,x+1):
                    BinLatticeUnderlying[Idx+1][k-1]=BinLatticeUnderlying[Idx][k-2]*d

            del x
        BinLatticeOption=buildLattice(self.NumOfTimeSteps+1,"bin")
        for k in range(len(BinLatticeOption[self.NumOfTimeSteps])):
            BinLatticeOption[self.NumOfTimeSteps][k]=calcPayOff(BinLatticeUnderlying[self.NumOfTimeSteps][k],self.Strike,self.StrCallPut)
        for i in range(self.NumOfTimeSteps-1):
            Idx=self.NumOfTimeSteps-1-i
            for k in range(len(BinLatticeOption[Idx])):
                if self.OptionType=="American":
                    BinLatticeOption[Idx][k]=(1/r)*(q*BinLatticeOption[Idx+1][k]+(1-q)*BinLatticeOption[Idx+1][k+1])
                    I=calcPayOff(BinLatticeUnderlying[Idx][k],self.Strike,self.StrCallPut)
                    BinLatticeOption[Idx][k]=max(I,BinLatticeOption[Idx][k])
                else:
                    BinLatticeOption[Idx][k]=(1/r)*(q*BinLatticeOption[Idx+1][k]+(1-q)*BinLatticeOption[Idx+1][k+1])
            if Idx==1:
                BinLatticeOption[0][0]=(1/r)*(q*BinLatticeOption[1][0]+(1-q)*BinLatticeOption[1][1])
        OptionPrice=BinLatticeOption[0][0]
        return OptionPrice

