def calcPayOff(Underlying:float, Strike:float,StrCallPut:str):
    # The function calculates a standard European option payoff 
    # Input: 
    # Underlying
    # Strike
    # StrCallPut: 'Call' or 'Put' (default is 'Call')
    #
    # Output:
    # PayoffValue = max(Underlying - Strike, 0)
    #
    # Note: the function can be easily modified for other exotic options
    if StrCallPut=="put" or StrCallPut=="Put":
        PayOffValue=max(Strike-Underlying,0)
    else:
        PayOffValue=max(Underlying-Strike,0)

    return PayOffValue
