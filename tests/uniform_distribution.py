import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

# from scipy.stats import entropy


import sys
sys.path.append('..')
import cloudtropy


# data

gen_dim = 2
gen_N = 300
lims = (-2,6)

scale = 0.2
X = np.random.uniform(low=lims[0],high=lims[1],size=(10000,2)) # background
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([0,0])] )
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([4,0])] )
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([0,4])] )
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([4,4])] )


# input parameters

N_grid = 80
delta_c = 0.35

grid,pmf = cloudtropy.pmf(X,N=N_grid,delta_c=delta_c)
entropy = cloudtropy.entropy(X,base=2,N=N_grid,delta_c=delta_c)

entropy_readme = cloudtropy.entropy(X)