from PriceOptionTrinKR import PriceOptionTrinKRClass
from PriceOptionBinCRR import PriceOptionBinCRRClass
Rate = 0.05;
NumOfTimeSteps = 100;
T = NumOfTimeSteps/365;
Sigma = 0.75;
Underlying = 25;
Strike = 20;
Lam=1.3
#TrinKRAmerican=PriceOptionTrinKRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,'put','American')
#TrinKREuro=PriceOptionTrinKRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,'put','Euro')
BinCRRAmerican=PriceOptionBinCRRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,'Call','American')
BinCRREuro=PriceOptionBinCRRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,'Call','Euro')
TrinKREuro=PriceOptionTrinKRClass(Underlying, Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,'Call','Euro')
price0,delta0,gamma0=TrinKREuro.priceOptionTrinKR()
price1,delta1,gamma1=BinCRRAmerican.priceOptionBinCRR()
price2,delta2,gamma2=BinCRREuro.priceOptionBinCRR()
vega=BinCRREuro.vegaCalculation(0.0001)
print(vega)
print(delta0)
print(delta1)
print(delta2)
