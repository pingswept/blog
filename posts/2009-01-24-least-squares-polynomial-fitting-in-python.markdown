---
categories: estimation, mathematics, python
date: 2009-01-24T00:00:00.000Z
format: markdown
title: Least squares polynomial fitting in Python
---

A few weeks ago at [work][1], in the course of reverse engineering a dissolved oxygen sensor calibration routine, [Jon][2] needed to fit a curve to measured data so he could calculate calibration values from sensor readings, or something like that. I don’t know how he did the fitting, but it got me thinking about least squares and mathematical modeling.

The tools I’ve used for modeling (Matlab, Excel and the like) and the programming languages I’ve used for embedded systems (C and Python, mostly) are disjoint sets. Who wants to use Matlab for network programming, when you could use Python instead? Who wants to use C for calculating eigenvalues, when you could use Matlab instead? Generally, nobody.

Unfortunately, sometimes you need to do both in the same system. I’m not sure that I’m making a wise investment, but I think that [Python’s numerical libraries][3] have matured enough that Python can straddle the divide.

So, here’s what I’ve figured out about least squares in Python. My apologies to most of you regular readers, as you will find this boring as hell. This one’s for me and the internet.

**Least squares estimation**

Generally, least squares estimation is useful when you have a set of unknown parameters in a mathematical model. You want to estimate parameters that minimize the errors between the model and your data. The canonical form is:

Ax=y
where:

    * A is an M \times N full rank matrix with M > N (skinny)
    * x is a vector of length N
    * y is a vector of length M

As matrices, this looks like
![Ax = y](http://pingswept.org/images/equations/ax_equals_y.png)

You want to minimize the L2-norm, ||Ax-y||. To be explicit, this means that if you define the residuals r = Ax - y, you want to choose the ![x](http://pingswept.org/images/equations/x.png) that minimizes \sqrt{r_1^2 + ... r_M^2}. This is where the “least squares” name comes from– you’re going to choose the ![x](http://pingswept.org/images/equations/x.png) that results in the squares of r being least.

Once you know A and y, actually finding the best x (assuming you have a computer at your disposal) is quick. The derivation sets the gradient of ||r||^2 with respect to x to zero and then solves for x. Mathematicians call the solution the Moore-Penrose pseudo-inverse. I call it “what the least squares function returned.” In any case, here it is:

![x_{ls} = (A^TA)^{-1}A^Ty](http://pingswept.org/images/equations/moore_penrose_pseudo_inverse.png)

Fortunately, one need not know the correct name and derivation of a thing for it to be useful.

So now, how do you go about using this technique to fit a polynomial to some data?

**Polynomial fitting**

In the case of polynomial fitting, let’s say you have a series of data points, (t_i, y_i) that you got from an experiment. The t_i are the times at which you made your observations. Each y_i is the reading from your sensor that you noted at the time with the same i.

Now you want to find a polynomial y = f(t) that approximates your data as closely as possible. The final output will look something like

![y = x_Nt^N + . . . + x_2 t^2 + x_1t + x_0](http://pingswept.org/images/equations/polynomial_in_x.png)

where you have cleverly chosen the x_i for the best fit to your data. You’ll be able to plug in whatever value of t you want and get an estimate of y in return.

In the conventional form, we are trying to find an approximate solution to
Ax=y

In this case, A is called the Vandermonde matrix; it takes the form:

![Vandermonde matrix](http://pingswept.org/images/equations/vandermonde_matrix.png)

(This presumes that you want to use powers of t as your basis functions– not a good idea for all modeling tasks, but this blog post is about polynomial fitting. Another popular choice is sinusoidal functions; perhaps Google can tell you more on that topic.)

(Also, the Vandermonde matrix is sometimes defined with the powers ascending from left to right, rather than descending. Descending works better with Python because of the coefficient order that numpy.poly1d() expects, but mathematically either way works.)

(Back to polynomial fitting.)

Each observation in your experiment corresponds to a row of A; A_i * x = y_i. Presumably, since every experiment has some noise in it, there is no x that fits every observation exactly. You know all the t_i, so you know A.

As a reminder, our model looks like this:

![Ax = y](http://pingswept.org/images/equations/ax_equals_y.png)

You can check that A makes sense by imagining the matrix multiplication of each row of A with x to equal the corresponding entry in y. For the second row of A, we have
y_2 = x_Nt_2 + . . . + x_2t_2^2 + x_1t_2^1 + x_0

which is just the polynomial we’re looking to fit to the data.

Now, how can we actually do this in Python?

Python code

Let’s suppose that we have some data that looks like a noisy parabola, and we want to fit a polynomial of degree 5 to it. (I chose 5 randomly; it’s a stupid choice. More on selection of polynomial degree in another post.)

$$code(lang=python)
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

degree = 5

# generate a noisy parabola
t = np.linspace(0,100,200)
parabola = t**2
noise = np.random.normal(0,300,200)
y = parabola + noise
$$/code

So now we have some fake data– an array of times and an array of noisy sensor readings. Next, we form the Vandermonde matrix and find an approximate solution for x. Note that numpy.linalg.lstsq() returns a tuple; we’re really only interested in the first element, which is the array of coefficients.

$$code(lang=python)
# form the Vandermonde matrix
A = np.vander(t, degree)
 
# find the x that minimizes the norm of Ax-y
(coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, y)
 
# create a polynomial using coefficients
f = np.poly1d(coeffs)
$$/code

Three lines of code later, we have a solution!

I could have also used numpy.polyfit() in place of numpy.linalg.lstsq(), but then I wouldn’t be able to write a blog post about regularized least squares later.

Now we’ll plot the data and the fitted curve to see if the function actually works!

$$code(lang=python)
# for plot, estimate y for each observation time
y_est = f(t)
 
# create plot
plt.plot(t, y, '.', label = 'original data', markersize=5)
plt.plot(t, y_est, 'o-', label = 'estimate', markersize=1)
plt.xlabel('time')
plt.ylabel('sensor readings')
plt.title('least squares fit of degree 5')
plt.savefig('sample.png')
$$/code

![Least squares fit of a noisy parabola](http://pingswept.org/img/sample.png)

This post took two-thirds of eternity to write. Feel free to ask questions or point out how confused I am below.

Next: regularized least squares! Or maybe selection of polynomial degree! Or maybe forgetting the blog and melting brain with TV!

[1]: http://www.greenmountainengineering.com/
[2]: http://eatthepath.com
[3]: http://scipy.org/
