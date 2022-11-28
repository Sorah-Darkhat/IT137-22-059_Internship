import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import random as rd
import time
rc('text.latex', preamble = r'\usepackage[helvet]{sfmath} \usepackage{sansmathfonts}')

#Load TOV class
from tovsolver.tov import *
from tovsolver.constants import *

def Solve_EoS(File = "eos.csv", Id = 0, Ran=True, Random_Seed=0):
    """ Solves the EoS """
    
    I_ = [i for i in range(2000)]
    if Ran:
        rd.Random(Random_Seed).shuffle(I_)
    
    
    #Here we load EoS to be used in calculations
    eos_ = pd.read_csv("eos.csv", sep=",", header=0)
    eos  = eos_.loc[eos_["id"] == I_[Id]]
    
    n_arr, p_arr = np.array(eos["energy_density"]), np.array(eos["pressure"])
    
    #initialization of TOVsolver
    tov_s = TOV(n_arr, p_arr, add_crust=False, plot_eos=True)
    
    
    m_arr = []
    R_arr = []
    
    for dens_c in np.logspace(-8,3,500):
        R, M, prof = tov_s.solve(dens_c, rmax=50e5, dr=100)  #ValueError: A value in x_new is below the interpolation range.
        m_arr.append(M)
        R_arr.append(R)
    
    plt.plot(R_arr, m_arr)
    
    plt.xlim(10,20)
    plt.ylim(0,2.8)
    
    plt.ylabel(r'${\rm M/M_\odot}$')
    plt.xlabel(r'${\rm R~(km)}$')
    
    plt.savefig(f'figures/{Random_Seed}_mr_{I_[Id]}.png')
    plt.show()
        
        
    #Here we calculate tidal propertis of the NS family
    
    m_arr = []
    R_arr = []
    
    L_arr = []
    k2_arr = []
    C_arr = []
    
    for dens_c in np.logspace(-8,3,500):
        NS_prop = tov_s.solve_tidal(dens_c, rmax=50e5, dr=100)
        R, M, C, k2, y, beta, H = NS_prop[0], NS_prop[1], NS_prop[2], NS_prop[3], NS_prop[4], NS_prop[5], NS_prop[6]
        L_arr.append(2/3*k2/C**5)
        k2_arr.append(k2)
        C_arr.append(C)
        R_arr.append(R)
        m_arr.append(M)
        
        
    fig = plt.figure(figsize=(10,8))
    
    ax1 = fig.add_subplot(221)
    
    ax1.plot(m_arr, C_arr)
    ax1.set_xlabel(r'${\rm M/M_\odot}$')
    ax1.set_ylabel(r'${\rm C=M/R}$')
    
    ax2 = fig.add_subplot(222)
    
    ax2.plot(m_arr, k2_arr)
    ax2.set_xlabel(r'${\rm M/M_\odot}$')
    ax2.set_ylabel(r'${\rm k_2}$')
    
    ax3 = fig.add_subplot(223)
    
    ax3.plot(R_arr, L_arr)
    ax3.set_xlabel(r'${\rm R~(km)}$')
    ax3.set_ylabel(r'${\rm \Lambda}$')
    ax3.set_xlim(10,20)
    ax3.set_ylim(0,1000)
    
    ax4 = fig.add_subplot(224)
    
    ax4.plot(m_arr, L_arr)
    ax4.set_xlabel(r'${\rm M/M_\odot}$')
    ax4.set_ylabel(r'${\rm \Lambda}$')
    ax4.set_xlim(0,2.2)
    ax4.set_ylim(0,1000)
    
    plt.tight_layout()
    
    
    plt.savefig(f'figures/{Random_Seed}_tidal_{I_[Id]}.png')
    plt.show()
    
    try:
        Raise(ValueError)
        Solved_df = pd.read_csv("Sdf.csv")
        N_Sdf = pd.DataFrame({"Mass":m_arr, "Radius":R_arr, "Lambda":L_arr, "K2":k2_arr, "C":C_arr, "Id":I_[Id]} )
        Solved_df = Solved_df.append(N_Sdf)
        Solved_df.to_csv("Solved/Sdf.csv", sep=",", index=False)
    except:
        N_Sdf = pd.DataFrame({"Mass":m_arr, "Radius":R_arr, "Lambda":L_arr, "K2":k2_arr, "C":C_arr, "Id":I_[Id]} )
        N_Sdf.to_csv(f"Solved/Sdf_{I_[Id]}.csv", sep=",", index=False)