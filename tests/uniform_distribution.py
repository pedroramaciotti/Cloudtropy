import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

from scipy.stats import entropy


import sys
sys.path.append('..')
import cloudtropy


# data

N_points = 5000
W = 1
d = 0.05
delta_c = 0.2


theorical_entropy = 2.0*np.log2((W/d+1))


dist = (-W*0.5,W*0.5)
X = np.random.uniform(low=dist[0],high=dist[1],size=(N_points,2)) # background



lims = [(-2,2),(-2,2)]

grid,pmf = cloudtropy.pmf(X,d=d,delta_c=delta_c,lims=lims)
entropy = cloudtropy.entropy(X,base=2,d=d,delta_c=delta_c,lims=lims)

print('benchmark entropy = %.4f / empirical entropy = %.4f'%(theorical_entropy,entropy))


fig = plt.figure(figsize=(14,3))
#
ax1 = fig.add_subplot(1,4,1)
# levels = np.linspace(0,flat_pmf.max(),40)
ax1.scatter(X[:,0], X[:,1],s=1,alpha=0.1,color='k')
ax1.set_xlabel('x'),ax1.set_ylabel('y')
ax1.set_xlim(lims[0]),ax1.set_ylim(lims[0])
# ax1.axis('equal')
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
ax3.set_xlim(lims[0]),ax3.set_xlim(lims[0]),
ax3.axis('equal')
cbar = fig.colorbar(cs)
#
plt.tight_layout()
# plt.savefig('all.pdf')
plt.savefig('all.png',dpi=400)