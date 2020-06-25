<p float="center">
  <img src="https://github.com/pedroramaciotti/Cloudtropy/blob/master/figures/scatter.png" height="200" />
  <img src="https://github.com/pedroramaciotti/Cloudtropy/blob/master/figures/surf.png" height="200" />
  <img src="https://github.com/pedroramaciotti/Cloudtropy/blob/master/figures/contour.png" height="200" />
</p>

# Cloudtropy


Empirical probability mass functions and entropies of N-dimensional clouds of points.

## Install

Simply

    pip install cloudtropy

## Quick Start

Given an array X of M points in N dimensions (`X.shape`-> M,N)

<p float="left">
  <img src="https://github.com/pedroramaciotti/Cloudtropy/blob/master/figures/scatter.png" width="200" />
</p>


 get the N-dimensional grid object and the probability mass function on the elements of the grid

     import cloudtropy as ctpy
     grid,pmf = ctpy.pmf(X)

which you can then use in graphics, for example if N=2:

     fig = plt.figure(figsize=(4,3))
     ax = fig.add_subplot(1,1,1)
     cs = ax.contourf(grid[0], grid[1], pmf, cmap='Purples_r')
     ax.axis('equal')
     cbar = fig.colorbar(cs)
     plt.show()

<p float="left">
  <img src="https://github.com/pedroramaciotti/Cloudtropy/blob/master/figures/contour_simple.png" width="200" />
</p>

or to compute its entropy:

     ctpy.entropy(X)
     >>> 8.4976

    
