import numpy as np
from sklearn.metrics import pairwise_distances
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
X = np.random.uniform(low=lims[0],high=lims[1],size=(10000,2)) # back
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([0,0])] )
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([4,0])] )
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([0,4])] )
X = np.concatenate([X,scale*np.random.randn(gen_N,gen_dim)+np.array([4,4])] )


# input parameters

N_grid = 80
delta_c = 0.35

grid,pmf = cloudtropy.pmf(X,N=N_grid,delta_c=delta_c)
entropy = cloudtropy.entropy(X,base=2,N=N_grid,delta_c=delta_c)

############## All in one

fig = plt.figure(figsize=(14,3))
#
ax1 = fig.add_subplot(1,4,1)
# levels = np.linspace(0,flat_pmf.max(),40)
ax1.scatter(X[:,0], X[:,1],s=1,alpha=0.1,color='k')
ax1.set_xlabel('x'),ax1.set_ylabel('y')
ax1.set_xlim(lims),ax1.set_xlim(lims)
ax1.axis('equal')
#
ax2 = fig.add_subplot(1,3,2,projection='3d')
ax2.plot_surface(grid[0], grid[1], pmf,cmap='coolwarm', edgecolor='none',shade='interp')
ax2.set_xlabel('x'),ax2.set_ylabel('y')#,ax.set_zlabel('PMF',rotation=90)
ax2.view_init(elev=60, azim=-45)
#
ax3 = fig.add_subplot(1,3,3)
cs = ax3.contourf(grid[0], grid[1], pmf, levels=np.linspace(0,pmf.max(),40), cmap='Purples_r')
ax3.set_xlabel('x'),ax3.set_ylabel('y')
ax3.set_title('Entropy = %.3f'%entropy)
ax3.set_xlim(lims),ax3.set_xlim(lims),
ax3.axis('equal')
cbar = fig.colorbar(cs)
#
plt.tight_layout()
# plt.savefig('all.pdf')
plt.savefig('all.png',dpi=400)

############## Separate

fig = plt.figure(figsize=(4,3))
#
ax1 = fig.add_subplot(1,1,1)
# levels = np.linspace(0,flat_pmf.max(),40)
ax1.scatter(X[:,0], X[:,1],s=1,alpha=0.1,color='k')
ax1.set_xlabel('x'),ax1.set_ylabel('y')
ax1.set_xlim(lims),ax1.set_xlim(lims)
ax1.axis('equal')
plt.savefig('scatter.png',dpi=400)
#
fig = plt.figure(figsize=(4,3))
#
ax2 = fig.add_subplot(1,1,1,projection='3d')
ax2.plot_surface(grid[0], grid[1], pmf,cmap='coolwarm', edgecolor='none',shade='interp')
ax2.set_xlabel('x'),ax2.set_ylabel('y')#,ax.set_zlabel('PMF',rotation=90)
ax2.view_init(elev=60, azim=-45)
plt.savefig('surf.png',dpi=400)
#
fig = plt.figure(figsize=(4,3))
#
ax3 = fig.add_subplot(1,1,1)
cs = ax3.contourf(grid[0], grid[1], pmf, levels=np.linspace(0,pmf.max(),40), cmap='Purples_r')
ax3.set_xlabel('x'),ax3.set_ylabel('y')
ax3.set_title('Entropy = %.3f'%entropy)
ax3.set_xlim(lims),ax3.set_xlim(lims),
ax3.axis('equal')
cbar = fig.colorbar(cs)
#
plt.tight_layout()
# plt.savefig('all.pdf')
plt.savefig('contour.png',dpi=400)



