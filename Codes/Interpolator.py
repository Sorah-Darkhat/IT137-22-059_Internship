import numpy as np
import pandas as pd

File = str(input("File = "))+"_Generated"
data = pd.read_csv(File+".csv")


def SI(p1, p2, x):
    x1 = p1[0]
    x2 = p2[0]

    y1 = p1[1]
    y2 = p2[1]

    yi = y2-y1
    xi = x2-x1
    m = yi/xi

    xt = x-x1
    y = xt*m+y1

    return y


def MkIp(CSVFile, X, Y, Z):
    x = np.array(CSVFile[X])
    FP = data.loc[data["rho"] <= 0.32]
    FPoint_data = data.loc[data["rho"] >= FP["rho"].iat[-1]]
    IntPoints = []
    Xs = np.arange(0.32, 12*0.16, step=0.01)
    for ids in range(int(max(data["id"]))+1):
        print(round((ids+1)/(max(data["id"])+1)*100,3),"%", end="\r")
        FPoints = list(np.array(FPoint_data.loc[FPoint_data["id"] == ids]["rho"]))
        for i in range(len(x)):
            if data["rho"][i] <= 0.32 and data["id"][i] == ids:
                IntPoints.append( [data["rho"][i], data["e"][i], data["p"][i], data["id"][i]])
        
        DF = FPoint_data.loc[FPoint_data["id"]==ids]
        for j in range(len(Xs)):
            if Xs[j] > FPoints[1]:
                FPoints.pop(0)
            Int_Y = SI([FPoints[0],np.array(DF.loc[DF["rho"]==FPoints[0]][Y])[0]],[FPoints[1],np.array(DF.loc[DF["rho"]==FPoints[1]][Y])[0]],Xs[j])
            Int_Z = SI([FPoints[0],np.array(DF.loc[DF["rho"]==FPoints[0]][Z])[0]],[FPoints[1],np.array(DF.loc[DF["rho"]==FPoints[1]][Z])[0]],Xs[j])
            IntPoints.append( [Xs[j], Int_Y, Int_Z, ids])
        IntPoints.append( [FPoints[-1], DF.loc[DF["rho"]==FPoints[-1]][Y], DF.loc[DF["rho"]==FPoints[-1]][Z], ids])
    
    return IntPoints

New_Points = np.array(MkIp(data,"rho","e", "p"), dtype="float64")
np.savetxt("Inted_"+File+".csv",New_Points,delimiter=",", header='rho,e,p,id', fmt='%1.12e')
