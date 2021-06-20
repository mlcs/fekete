# Fekete points estimation algorithm

This repo contains an implementation of the Fekete points estimation
algorithm as proposed by Bendito et al. (2007). The goal is to be able
to generate $N$ equidistant points on the surface of a unit sphere. The
algorithm has potential applications in global climate data analysis
where the commonly used Gaussian (rectilinear, latitude-longitude) grid
leads to an increasingly high density of points towards the poles,
resulting in potentially unwanted effects.

![fekete-100-iterations](/examples/fekete.gif)

## References

Bendito, E., Carmona, A., Encinas, A. M., & Gesto, J. M. Estimation of
Fekete points (2007), _J Comp. Phys._ **225**, pp 2354--2376  
[https://doi.org/10.1016/j.jcp.2007.03.017](https://doi.org/10.1016/j.jcp.2007.03.017)


## TODO

- [x] First working implementation
- [x] Optimize code for faster performance
- [ ] Documentation
- [ ] Plotting routine for spherical Voronoi tesselation
- [ ] Examples
