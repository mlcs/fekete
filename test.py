#!/usr/bin/env python
import fekete
import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from scipy.ndimage.filters import uniform_filter1d
from scipy.spatial import SphericalVoronoi
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial.distance import pdist

import sys

def plot_voronoi_3d(X, ax):
    """Plots 3D Voronoi on surface of unit sphere"""
    vor = SphericalVoronoi(X)
    vor.sort_vertices_of_regions()
    verts = vor.vertices
    regs = vor.regions
    for i in range(X.shape[0]):
        verts_reg = np.array([verts[k] for k in regs[i]])
        verts_reg = [list(zip(verts_reg[:, 0], verts_reg[:, 1], verts_reg[:, 2]))]
        ax.add_collection3d(Poly3DCollection(verts_reg,
                                             facecolors="w",
                                             edgecolors="steelblue"
                                             ),
                            )
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2],
               marker=".", color="indianred", depthshade=True, s=40)
    return None

def plot(X, Xeq, E):
    """plots the final results
    """
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
    pl.savefig("fekete_error.png")

    return None


def main():
    """Runs the main part of the analysis"""
    X = fekete.points_on_sphere(N=1000)
    Xeq, E = fekete.bendito(X=X, maxiter=1000)
    plot(X, Xeq, E)
    return None


if __name__ == "__main__":
    main()


