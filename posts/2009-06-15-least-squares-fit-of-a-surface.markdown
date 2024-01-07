---
categories: estimation, mathematics, python
date: 2009-06-15T00:00:00.000Z
format: markdown
title: Least squares fit of a surface to a 3D cloud of points in Python (with ridiculous
  application)
---

The floor in the room above the kitchen in our house has a floor that slopes almost 1 inch per foot for half of the room. Experimentally, we have found that this is steep enough to make a desk chair roll– kind of irritating, particularly to my special ladyfriend who happens to occupy such a chair in that zone.

To compensate for the slope, I decided to fit a stack of masonite sheets to the curve of the floor. Unfortunately, the floor slopes nonlinearly in two directions, like the rounded corner of a swimming pool. After making a series of measurements of the floor, I decided to fit a polynomial in two variables to the cloud of points using a least squares estimate.

(In retrospect, the floor was close enough to singly-curved that I could have gotten away with a linear fit.) The blue thing in the picture is a level. I shimmed the level until it was worthy of its name, and then measured the distance to the floor with calipers.

<a href="http://www.flickr.com/photos/pingswept/3453390885/"><img src="http://farm4.static.flickr.com/3603/3453390885_4727c27c5f.jpg" width="500" height="375" alt="Estimating the flatness of the floor" /></a>

**Estimating the flatness of the floor**

I’ll recount the basics from my [earlier post](http://pingswept.org/2009/01/24/least-squares-polynomial-fitting-in-python/) about least squares fitting in Python. Skip ahead to the next section if you read that already.

As before, the first step is to arrange the equations in canonical form:
Ax=y
where:

    * A is an M x N full rank matrix with M > N (skinny)
    * x is a vector of length N
    * y is a vector of length M

As matrices, this looks like
![Ax = y](http://pingswept.org/images/equations/ax_equals_y.png)

In polynomial fitting, A is called the Vandermonde matrix and takes the form:
![Vandermonde matrix](http://pingswept.org/images/equations/vandermonde_matrix.png)

**The 3D case**

In the 2D case, we’re trying to find polynomial in x such that f(x) approximates y. In the 3D case at hand, we have two independent variables, so we’re looking for a polynomial in x and y such that f(x, y) approximates z. Rather than the 2D case:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=y = x_Nt^N %2B . . . %2B x_2 t^2 %2B x_1t %2B x_0">

we want the final output to look like this:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=z = a_Nx^N %2B . . . %2B a_2 x^2 %2B a_1x %2B a_0 %2B b_Ny^N %2B . . . %2B b_2 y^2 %2B b_1y %2B b_0">

(Spike Curtis astutely notes in the comments that I am omitting the cross terms, such as xy, and refers us to a Matlab script. Spike is right, but the floor’s already fixed.)

We can use two Vandermonde matrices next to each other.
![Vandermonde ab equals z](http://pingswept.org/images/equations/vandermonde_ab_equals_z.png)

Here’s the Python code that creates the two Vandermonde matrices and joins them into one matrix. x, y, and z are lists of corresponding coordinates, so, for example, x\[5\], y\[5\] and z\[5\] are the coordinates of one point that the surface should approximate. The order of the points is not important.

'''(lang=python)

    import numpy as np
     
    z = [0.0, 0.695, 1.345, 1.865, 2.225, 2.590, 0.0, 0.719, 1.405, 1.978, 2.398, 2.730, 0.0, 0.789, 1.474, 2.064, 2.472, 2.775, 0.0, 0.763, 1.453, 1.968, 2.356, 2.649]
     
    x = [0.0, 12.0, 24.0, 36.0, 48.0, 60.0, 0.0, 12.0, 24.0, 36.0, 48.0, 60.0, 0.0, 12.0, 24.0, 36.0, 48.0, 60.0, 0.0, 12.0, 24.0, 36.0, 48.0, 60.0]
     
    y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 24.0, 24.0, 24.0, 24.0, 24.0, 24.0, 48.0, 48.0, 48.0, 48.0, 48.0, 48.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0]
     
    degree = 3
    thickness = 0.167
     
    # Set up the canonical least squares form
    Ax = np.vander(x, degree)
    Ay = np.vander(y, degree)
    A = np.hstack((Ax, Ay))
     
    # Solve for a least squares estimate
    (coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, z)
     
    # Extract coefficients and create polynomials in x and y
    xcoeffs = coeffs[0:degree]
    ycoeffs = coeffs[degree:2 * degree]
     
    fx = np.poly1d(xcoeffs)
    fy = np.poly1d(ycoeffs)

'''

Once I knew the coefficients of the polynomial approximation, I could calculate the contours of the masonite. From a measurement of the stack of masonite, I knew the average thickness is 0.167 inches. (Thanks to Dr. Alex T. Tung, Ph.D., for helping me get the masonite home from Home Depot.) To find out where the first layer should end, I picked a series of stations spaced every 12 inches along the length of the floor in the y-direction. Along those stations, I solved f(x, y) = 0.167, f(x, y) = 2 * 0.167, f(x, y) = 3 * 0.167 and so forth.

In practice, solving f(x, y) = c, where c is a constant, means finding the roots of the equation f(x, y) - c = 0. (The mathematicians call this solving the homogeneous equation.) In Python, the numpy.roots method solves the homogeneous case. For each contour/section crossing, I generated a polynomial of the form f(x, y) - c and solved it with numpy.roots.

'''
(lang=python)
    ystations = range(0, 84, 12)
    sections = [[np.poly1d(xcoeffs - [0,0,zoffset - fy(ypos)]) for zoffset in np.arange(thickness, max(z), thickness).tolist()] for ypos in ystations]
    pts = [[min(func.roots) for func in list_of_fs] for list_of_fs in sections]

'''

For fabrication, I printed out a list of the locations where the masonite contours crossed the stations.

'''
(lang=python)
    for (pt_list, ystation) in zip(pts, ystations):
        print('\nBoundaries at station y = {0} inches:'.format(ystation))
        print('\t'.join(['{0:.3}'.format(pt) for pt in pt_list]))

'''

Armed with my list of measurements, I headed to the garage and set up some sawhorses with a sheet of plywood to keep the masonite from bowing and flopping around. It took a few hours of marking points and cutting gentle curves with a jigsaw, but the results were delightful.

*The masonite platform (non-impressive view)*

<a href="http://www.flickr.com/photos/pingswept/3627106741/"><img src="http://farm4.static.flickr.com/3401/3627106741_4ec24959d9.jpg" width="375" height="500" alt="The masonite platform (non-impressive view)" /></a>

*Level and gleeful*

<a href="http://www.flickr.com/photos/pingswept/3627929546/"><img src="http://farm4.static.flickr.com/3542/3627929546_c88a341a57.jpg" width="500" height="375" alt="Level and gleeful" /></a>

*Side view of the masonite platform*

<a href="http://www.flickr.com/photos/pingswept/3630614507/"><img src="http://farm4.static.flickr.com/3324/3630614507_79b7731799.jpg" width="500" height="375" alt="Side view of the masonite platform" /></a>

*Another side view of the masonite platform*

<a href="http://www.flickr.com/photos/pingswept/3631431316/"><img src="http://farm4.static.flickr.com/3646/3631431316_9bac95a888.jpg" width="500" height="375" alt="Another side view of the masonite platform" /></a>

As you can see above, I haven’t fastened the layers together yet. They seem to be sticking together reasonably well.

In the end, I think the slope went from about a 2.75″ drop across the 48″ span, to within 1/8″ of flat across the same distance. Sharon was delighted, and I found the whole project both more time-consuming and more satisfying than I expected.
