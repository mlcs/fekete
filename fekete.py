#! /usr/bin/env python3
"""
fekete -  Estimation of Fekete points on a unit sphere

          This module implements the core algorithm put forward in [1],
          allowing users to estimate the locations of N equidistant points on a
          unit sphere.

[1] Bendito, E., Carmona, A., Encinas, A. M., & Gesto, J. M. Estimation of
    Fekete points (2007), J Comp. Phys. 225, pp 2354--2376  
    https://doi.org/10.1016/j.jcp.2007.03.017

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


import numpy as np
from scipy.spatial.distance import pdist
from tqdm import tqdm
from numba import jit

G = 6.67408 * 1E-11         # m^3 / kg / s^2


def bendito(N=100, a=1., X=None, maxiter=100, tol=1E-20, neq=100):
    err = [1E-1]
    k = 0
    if len(X) == 0:
        print("Initial configuration not provided. Generating random one ...")
        X = points_on_sphere(N)         # initial random configuration
    else:
        N = X.shape[0]
    equilibriated = False
    pbar = tqdm(total=maxiter,
                bar_format='{desc:<5.5}{percentage:3.0f}%|{bar:30}{r_bar}'
                )
    w = np.zeros(X.shape)
    while (not equilibriated) and (k < maxiter):
        # Core algorithm steps from Bendito et al. (2007)
        ## 1.a. Advance direction
        # w = advance_direction(X)
        for i in range(len(X)):
            w[i] = disequilibrium_i(X, i)
        # 1.b. Error as max_i |w_i|
        mod_w = np.sqrt((w ** 2).sum(axis=1))
        err.append(np.max(mod_w))
        ## 2.a. Minimum distance between all points
        d = np.min(pdist(X))
        ## 2.b. Calculate x^k_hat = x^k + a * d^{k-1} w^{k-1}
        Xhat = X + a * d * w
        ## 3. New configuration
        X_new = (Xhat.T / np.sqrt((Xhat ** 2).sum(axis=1))).T
        X = X_new
        # check if algorithm has converged
        if k > (10 * neq):
            # running mean for the last neq time steps
            nfilt = int(neq / 10)
            del_err_avg = np.convolve(err[-neq:], np.ones((nfilt,))/nfilt)[(nfilt-1):]
            if np.all(del_err_avg < tol) * np.all(del_err_avg > (tol / 10.)):
                equilibriated = True
        k += 1
        pbar.update(1)
    pbar.close()
    return X_new, err


@jit(nopython=True)
def disequilibrium_i(X, i):
    xi = X[i]
    # total force at i
    xi_arr = xi.repeat(X.shape[0]).reshape(xi.shape[0], X.shape[0]).T
    diff = xi_arr - X
    j = np.where(np.sum(diff, axis=1) != 0)[0]
    diff_j = diff[j]
    denom = (np.sqrt(np.square(diff_j).sum(axis=1))) ** 3
    numer = (G * diff_j)
    Fi_tot = np.sum((numer.T / denom).T, axis=0)    # gives 3D net force vector
    # disequilibrium
    xi_n = xi / np.sqrt(np.square(xi).sum())
    Fi_n = (Fi_tot * xi_n).sum() * xi_n
    Fi_T = Fi_tot - Fi_n
    wi = Fi_T / np.sqrt(np.square(Fi_tot).sum())
    return wi


def points_on_sphere(N, r=1.):
    phi = np.arccos(1. - 2. * np.random.rand(N))
    theta = 2. * np.pi * np.random.rand(N)
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np. sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return np.c_[x, y, z]


