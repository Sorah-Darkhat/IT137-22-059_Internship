import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colour import Color
import os

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


def Mk_Plot(y,y_l,x,x_l,ids_lim=1,log=False,Single_Random_Id=False, VLines=True, divs=1):
    SC = Color("blue")
    col = list(SC.range_to(Color("red"),ids_lim+1))
    
    plt.figure(figsize = (20,16))
    #FileNames = ["Inted_DDBI_1_Single_2"]
    FileNames = ["Inted_DDBI_1_Generated"]
    #FileNames = ["Interpolation_data_100_test"]
    for FileName in FileNames:
        data = pd.read_csv(FileName+".csv")
        if not Single_Random_Id:
            for ids in range(int(ids_lim/divs)):
                data_ = data.loc[data["id"] == int(ids*divs)]
                if x == 'n':
                    X  = np.array(data_['# rho'])
                    Y  = np.array(data_[y])
                elif y == 'n':
                    X  = np.array(data_[x])
                    Y  = np.array(data_['# rho'])
                else:
                    X  = np.array(data_[x])
                    Y  = np.array(data_[y])
                
                print(f"{FileName} {y} VS {x} = {round((ids+1)/(int(ids_lim/divs))*100,2):.2f}%", end="\r")
                color = col[ids*divs]
                color = str(color)
                
                if ids*divs % (ids_lim/5) == 0 or ids*divs == (ids_lim-1):
                    plt.scatter(X,Y,label=f"id = {ids*divs}",s=1,c=color)
                else:
                    plt.scatter(X,Y,s=1,c=color)
            
            plt.xlabel(x_l, fontsize=12)
            plt.ylabel(y_l,fontsize=12)
            
        elif Single_Random_Id:
            ids = 1996
            data_ = data.loc[data["id"] == ids]
            if x == 'n':
                X  = np.array(data_['# rho'])
                Y  = np.array(data_[y])
            elif y == 'n':
                X  = np.array(data_[x])
                Y  = np.array(data_['# rho'])
            else:
                X  = np.array(data_[x])
                Y  = np.array(data_[y])
        
            print(f"{FileName} {y} VS {x} = Saving  ", end="\r")
            color = col[ids]
            color = str(color)
            
            #if ids % 400 == 0 or ids == 1999:
            plt.scatter(X,Y,label=f"id = {ids}",s=1,c=color)
            #else:
            #    plt.scatter(X,Y,s=1,c=color)
            
            plt.xlabel(x_l, fontsize=12)
            plt.ylabel(y_l,fontsize=12)


        print(f"{FileName} {y} VS {x} = Saving  ", end="\r")
        path = f"Plots/{ids_lim}s/div = {divs}"
        if not os.path.exists(path):
            os.makedirs(path)
        
        
        if VLines:
            xs = np.arange(0.32, 1.92, 0.01)
            for line in xs:
                plt.axvline(line, alpha=0.4, linewidth=2)
        if log:
            plt.xscale("log")
            plt.yscale("log")
            plt.legend()
            if not Single_Random_Id:
                plt.savefig(f"Plots/{ids_lim}s/div = {divs}/"+FileName+"_"+y+"_"+x+".png", dpi=400)
            elif Single_Random_Id:
                plt.savefig(f"Plots/{ids_lim}s/div = {divs}/"+FileName+"_"+y+"_"+x+"_Single"+".png", dpi=400)
        else:
            plt.legend()
            if not Single_Random_Id:
                plt.savefig(f"Plots/{ids_lim}s/div = {divs}/"+FileName+"_"+y+"_"+x+".png", dpi=400)
            elif Single_Random_Id:
                plt.savefig(f"Plots/{ids_lim}s/div = {divs}/"+FileName+"_"+y+"_"+x+"_Single"+".png", dpi=400)
            
        print(f"{FileName} {y} VS {x} = Completed", end="\r")
        print("\n")
        plt.clf()
    
e_label = "e [MeV fm−3]"
p_label = "P [MeV fm−3]"
n_label = "n [fm−3]"
vs_label= "Sound Velocity"

D = [1,2,4,8,10,16,20,50,100,200,400]

for di in D:
    print(f"\ndivs = {di}\n")
    Mk_Plot("p", p_label,"e", e_label,ids_lim=2000,log=True, Single_Random_Id=True, VLines = False, divs=di)
    Mk_Plot("p", p_label,"n", n_label, ids_lim=2000, Single_Random_Id=True, VLines = False, divs=di)
    Mk_Plot("e", e_label,"n", n_label, ids_lim=2000, Single_Random_Id=True, VLines = False, divs=di)
    
    Mk_Plot("p", p_label,"e", e_label,ids_lim=2000,log=True, Single_Random_Id=False, VLines = False, divs=di)
    Mk_Plot("p", p_label,"n", n_label, ids_lim=2000, Single_Random_Id=False, VLines = False, divs=di)
    Mk_Plot("e", e_label,"n", n_label, ids_lim=2000, Single_Random_Id=False, VLines = False, divs=di)
    #Mk_Plot("VS", vs_label, "n", n_label, ids_lim=1, Single_Random_Id=False, VLines = False)

    
