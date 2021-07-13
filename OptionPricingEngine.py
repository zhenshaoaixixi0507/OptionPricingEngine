from PriceOptionTrinKR import PriceOptionTrinKRClass
Rate = 0.05;
NumOfTimeSteps = 31;
T = NumOfTimeSteps/365;
Sigma = 0.75;
Underlying = 20;
Strike = 19.5;
Lam=1.3
TrinKR=PriceOptionTrinKRClass(Underlying,Strike,Rate,T,NumOfTimeSteps,Sigma,Lam,'call')
optionPrice=TrinKR.priceOptionTrinKR()
print(optionPrice)
