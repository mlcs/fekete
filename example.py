#!/usr/bin/env python
# coding: utf-8

# ### Example usage of the Fekete points estimation algorithm
# 
# 
# Here, we first generate 100 points at random locations on the surface of the sphere and then use the algorithm from [Bendito et al.](https://doi.org/10.1016/j.jcp.2007.03.017) to estimate the Fekete points. We run the iterative algorithm for 10000 iterations and compare the final configuration to the initial one and also look at the error (proportional to the energy) of each configuration.
# 

# In[3]:


import numba
import fekete
import matplotlib.pyplot as pl

# Generate 100 points at random locations on surface of a sphere of unit radius
X = fekete.points_on_sphere(N=100)

# estimate the Fekete points using the algorithm from Bendito et al. (2007) (up to 10000 iterations)
Xeq, E = fekete.bendito(X=X, maxiter=10000)


# In[ ]:


fig1 = pl.figure(figsize=[10., 6.])
   ax11 = fig1.add_axes([0.01, 0.01, 0.50, 0.90], projection='3d')
   ax12 = fig1.add_axes([0.45, 0.01, 0.50, 0.90], projection='3d')
   plot_voronoi_3d(X, ax11)
   plot_voronoi_3d(Xeq, ax12)
   for ax in fig1.axes:
       ax.grid(False)
       ax.set_axis_off()
   pl.savefig("fekete_sphereplots.png")

   E = E[1:]
   fig2 = pl.figure(figsize=[12., 6])
   ax21 = fig2.add_subplot(1, 2, 1)
   ax21.plot(E, c="steelblue")
   ax21.plot(uniform_filter1d(E, size=10), c="indianred", ls="--")
   ax22 = fig2.add_subplot(1, 2, 2)
   ax22.plot(np.abs(np.diff(E)), c="steelblue")
   for ax in fig2.axes:
       ax.set_yscale("log")


# In[ ]:




