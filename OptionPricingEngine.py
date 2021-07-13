from PriceOptionTrinKR import PriceOptionTrinKRClass
from PriceOptionBinCRR import PriceOptionBinCRRClass
Rate = 0.05;
NumOfTimeSteps = 100;
T = NumOfTimeSteps/365;
Sigma = 0.75;
Underlying = 25;
Strike = 20;
Lam=1.3
TrinKRAmerican=PriceOptionTrinKRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,'put','American')
TrinKREuro=PriceOptionTrinKRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,'put','Euro')
BinCRRAmerican=PriceOptionBinCRRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,'put','American')
BinCRREuro=PriceOptionBinCRRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,'put','Euro')
optionPriceAmerican=TrinKRAmerican.priceOptionTrinKR()
optionPriceEuro=TrinKREuro.priceOptionTrinKR()
print('American option price: '+str(optionPriceAmerican))
print('European option price: '+str(optionPriceEuro))
print(BinCRRAmerican.priceOptionBinCRR())
print(BinCRREuro.priceOptionBinCRR())
