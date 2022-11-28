import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def SI(p1,p2,x):
    x1 = p1[0]
    x2 = p2[0]
    
    y1 = p1[1]
    y2 = p2[1]
    
    yi = y2-y1
    xi = x2-x1
    m  = yi/xi
    
    xt = x-x1
    y  = xt*m+y1
    
    return y


def Mk_Plot(y,y_l,x,x_l,log=False):
    plt.figure(figsize = (10,8))
    #FileNames = ["DDBu1","DDBm","DDBI_1"]
    FileNames = ["DDBI_1_2000"]
    for FileName in FileNames:
        data = pd.read_csv(FileName+".csv")
        
        if x == 'n':
            X  = np.array(data['rho'])
            Y  = np.array(data[y])
        elif y == 'n':
            X  = np.array(data[x])
            Y  = np.array(data['rho'])
        else:
            X  = np.array(data[x])
            Y  = np.array(data[y])
            
        plt.scatter(X,Y,label=FileName)
        
        plt.xlabel(x_l, fontsize=12)
        plt.ylabel(y_l,fontsize=12)
        
    if log:
        plt.xscale("log")
        plt.yscale("log")
    plt.legend()
    plt.savefig("Plots/"+x+"_"+y+".png")
    
    
def Run():    
    e_label = "e [MeV fm−3]"
    p_label = "P [MeV fm−3]"
    n_label = "n [fm−3]"
    vs_label= "Sound Velocity"
    
    Mk_Plot("p", p_label,"n", n_label)
    Mk_Plot("e", e_label,"n", n_label)
    Mk_Plot("p", p_label,"e", e_label,log=True)
    Mk_Plot("VS", vs_label, "n", n_label)
    return None

Run()
    
