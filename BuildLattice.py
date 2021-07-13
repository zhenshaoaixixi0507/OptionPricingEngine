from numpy import array,zeros
def buildLattice(NumOfTimeSteps:int, StrBinTrin:str):
    #Parameters:
    #    NumOfTimeSteps (int): Number of time steps.
    #    StrBinTrin (str): String to indicate type of trees.
    DataStructure={}
    DataStructure[0]=[0.0]
    if StrBinTrin=="trin" or StrBinTrin=="Trin":
        for i in range(NumOfTimeSteps-1):
            x=zeros(2*(i+2)-1)
            DataStructure[i+1]=x
            del x
    else:
        for i in range(NumOfTimeSteps-1):
            x=zeros(i+2)
            DataStructure[i+1]=x
            del x
    return DataStructure
