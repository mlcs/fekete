# Fekete points estimation algorithm

This repo contains an implementation of the Fekete points estimation
algorithm as proposed by Bendito et al. (2007). The goal is to be able
to generate _N_ equidistant points on the surface of a unit sphere. The
algorithm has potential applications in global climate data analysis
where the commonly used Gaussian (rectilinear, latitude-longitude) grid
leads to an increasingly high density of points towards the poles,
resulting in potentially unwanted effects.

![fekete-100-iterations](/fekete.gif)

## About the algorithm

Bendito et al.'s algorithm essentially proposes a _direction of descent_
(in terms of the potential energy of the configuration) which is
guaranteed to minimise the energy of the system and hence push the
particles on the surface of the sphere as far away from each other as
possible. The direction of descent is defined as the _N_ dimensional
vector where the _i_-th entry is the ratio of the tangential force
exerted on the _i_-th particle by the rest to the total force on it. In
simple terms, the direction is the sum of all the little nudges that
need to be given to all of the particles to move the system to a lower
energy state.

In their paper, the authors do not clearly mention the form for the
potential defined by the interaction of the particles, so e simply
assume a gravitational potential between the particles and work out the
forces (tangential, normal, and total) accordingly. 

## Notes on installation & usage

+   **Installation:** The algorithm is implemented as a Python module
    with the idea that    you can simply download
    [`fekete.py`](https://github.com/mlcs/fekete/blob/62778f464e608f001b1bf76c15769f8848ebf2aa/fekete.py)
    in your project directory and import is a Python module with `import
    fekete`.

+   **Prerequisite Python packages**:
    - `numpy`
    - `matplotlib` (spherical Voronoi plotting helper function)
    - `numba` (for speed up)
    - `tqdm` (progress bar display)

+   **Usage**: Call `fekete.bendito()` with the appropriate arguments: 
    - Either specify number of points _N_ you want to be distributed
      evenly on the sphere, or 
    - Provide an initial configuration _X_ of points that need to
      nudged towards equilibrium. In both cases, the results should
      be the same

+   **Coordinates**: The implementation uses Cartesian coordinates, but
    if you have your data in spherical coordinates you can use the
    [`fekete.spherical_to_cartesian()`](https://github.com/mlcs/fekete/blob/3205c742e13cb4115e14a53b05efe1cc2f90b36a/fekete.py#L226)
    function to convert the points to Cartesian coordinates before using
    the implementation.

+   **Plotting results**: The module has a helper function
    [`fekete.plot_spherical_voronoi()`](https://github.com/mlcs/fekete/blob/19f02d5136307d51ac3c73c8e709b4ff9f514064/fekete.py#L226)
    that estimates a [spherical Voronoi
    tessellation](https://www.jasondavies.com/maps/voronoi/) using the
    corresponding function in
    [scipy.spatial](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.SphericalVoronoi.html#scipy.spatial.SphericalVoronoi). 

+   **Example**: A simple example with `N=1000` and a total of 10000
    iterations is given in [`example.py`](/example.py). It takes around
    350 secs on a Intel® Core™ i9-9880H CPU @ 2.30GHz.

## References

Bendito, E., Carmona, A., Encinas, A. M., & Gesto, J. M. Estimation of
Fekete points (2007), _J Comp. Phys._ **225**, pp 2354--2376  
[https://doi.org/10.1016/j.jcp.2007.03.017](https://doi.org/10.1016/j.jcp.2007.03.017)


## TODO

- [x] First working implementation
- [x] Optimize code for faster performance
- [x] Documentation
- [x] Plotting routine for spherical Voronoi tesselation
- [x] Examples
- [x] Improve README (installation, license, usage, etc.)

## License

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg?style=flat-square)](https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3))

- Copyright © [Bedartha Goswami](https://machineclimate.de/people/goswami/).

## Issues?

If you find any issues simply open a bug report, or send an email to
[bedartha.goswami@uni-tuebingen.de](mailto:bedartha.goswami@uni-tuebingen.de)
