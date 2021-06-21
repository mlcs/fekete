#!/usr/bin/env python

"""
Example usage of the Fekete points estimation algorithm
=======================================================

Here, we do the following:
    1. First generate 100 points at random locations on the surface of the
    sphere
    2. Use the algorithm from [Bendito et
    al.](https://doi.org/10.1016/j.jcp.2007.03.017) to estimate the Fekete
    points.

We run the iterative algorithm for 10000 iterations and compare the final
configuration to the initial one and also look at the disequilibrium
(proportional to the energy) of each configuration. The example takes around
350 secs on a Intel® Core™ i9-9880H CPU @ 2.30GHz.


"""
# Created: Sat Jun 19, 2021  06:21pm Last modified: Sat Jun 19, 2021  06:21pm
#
# Copyright (C) 2021  Bedartha Goswami <bedartha.goswami@uni-tuebingen.de> This
# program is free software: you can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------


import fekete
import matplotlib.pyplot as pl
import numpy as np

# Generate 100 points at random locations on surface of a sphere of unit radius
X = fekete.points_on_sphere(N=1000)

# estimate the Fekete points using the algorithm from Bendito et al. (2007)
# (up to 10000 iterations)
Xeq, dq = fekete.bendito(X=X, maxiter=10000, verbose=True)

# plot the results
# for this, there is a convenient helper plotting function in the `fekete.py`
# module, called `plot_spherical_voronoi()`

# set up the first figure and two axes:
#   1. ax11: original configuration             (subplot top-left)
#   2. ax12: final configuration                (subplot top-right)
#   3. ax21: disequilibrium per iteration       (subplot bottom-left)
#   4. ax22: Rate of change of disequilibrium   (subplot bottom-right)
AXLABFS, TIKLABFS = 12, 10
fig = pl.figure(figsize=[12., 9.])
ax11 = fig.add_axes([-0.01, 0.45, 0.60, 0.55], projection='3d')
ax12 = fig.add_axes([0.40, 0.45, 0.60, 0.55], projection='3d')
ax21 = fig.add_axes([0.10, 0.10, 0.35, 0.35])
ax22 = fig.add_axes([0.55, 0.10, 0.35, 0.35])

# plot the top row using the helper plotting function
fekete.plot_spherical_voronoi(X, ax11)
fekete.plot_spherical_voronoi(Xeq, ax12)
# a little beautification
for ax in [ax11, ax12]:
   ax.grid(False)
   ax.set_axis_off()
ax11.text(-0.2, 0.5, 1.1, "Initial configuration",
          ha="center", fontsize=AXLABFS+2, 
          )
ax12.text(-0.2, 0.5, 1.1, "Final configuration",
          ha="center", fontsize=AXLABFS+2, 
          )

# plot the bottom row
ax21.plot(dq, c="steelblue")
ax22.plot(np.abs(np.diff(dq)), c="steelblue")
# beautification
for ax in [ax21, ax22]:
   ax.set_yscale("log")
   ax.set_xlabel("Iteration number", fontsize=AXLABFS)
ax21.set_title("Disequilibrium", fontsize=AXLABFS+2)
ax22.set_title("Rate of change of disequilibrium", fontsize=AXLABFS+2)
for ax in fig.axes:
   ax.tick_params(labelsize=TIKLABFS)

pl.show()
