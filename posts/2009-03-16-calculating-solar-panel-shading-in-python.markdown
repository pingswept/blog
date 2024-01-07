---
categories: mathematics, python, solar
date: 2009-03-16T00:00:00.000Z
format: markdown
title: Calculating solar panel shading in Python
---

Eventually, I'd like to install solar panels on our house, but I want to know that it will be worth it before I commit the money. Back in 2007, I wrote a <a href="http://pysolar.org/">library</a> for calculating the path of the sun given the time and your location on the earth. Since then, I've been thinking about the next step, which is calculating how much neighboring houses and trees would obstruct the sun at different times of the day. In a nutshell, I wanted to replicate the calculations performed by devices like the Solmetric <a href="http://www.solmetric.com/">Suneye</a> without paying $1500 for the device. To do the job right, I still need a quality circular fisheye lens ($680 new), but I've got a first approximation working with a <a href="http://www.mcmaster.com/#8406a12">$13 door peephole</a> from McMaster.

(I do realize that I could just get a solar contractor to do all the site evaluation for me for free. That misses the point. If all I wanted was some sort of fiscal efficiency, I'd get a job as a financial executive or maybe something different from that, like a bank robber.)

Back to the task at hand.

Below is the image I started with, which I took back in the fall, before the leaves fell off the trees. This was using a <a href="http://www.usa.canon.com/consumer/controller?act=ModelInfoAct&fcategoryid=145&modelid=11939">Canon SD450</a> camera and the aforementioned peephole. I didn't take particular care to level the camera or center the peephole.

<a href="http://pingswept.org/img/spherical.jpg"><img src="http://pingswept.org/img/spherical-300x225.jpg" alt="Original peephole image" title="Original peephole image" width="300" height="225" class="aligncenter size-medium" /></a>

Using the Python Imaging Library, I cropped the photo to be square and switched to black and white mode. Then I mapped concentric rings in the image below to the subsequent straightened image.

<a href="http://pingswept.org/img/linearized.jpg"><img src="http://pingswept.org/img/linearized-300x150.jpg" alt="Peephole image after mapping to rectilinear coordinate system" title="Peephole image after mapping to rectilinear coordinate system" width="300" height="150" class="aligncenter size-medium" /></a>

Here's the straightening code. The guts are in the nested for loops near the end. (If there are any Pythonistas out there who know how to iterate over concentric rings using a list comprehension or map(), please let me know. The code below is functional and reasonable clear, but a little slow.)

'''(lang=python)
# Code under GPLv3; see pysolar.org for complete version.
def despherifyImage(im):
    (width, height) = im.size
    half_width = im.size[0]/2
    half_height = im.size[1]/2
    inpix = im.load()
    out = Image.new("L", (width, half_height))
    outpix = out.load()
    full_circle = 1000.0 * 2 * pi
    for r in range(half_width):
        for theta in range(int(full_circle)):
            (inx, iny) = (round(r * cos(theta/1000.0)) + half_width, round(r * sin(theta/1000.0)) + half_width)
            (outx, outy) = (width - width * (theta/full_circle) - 1, r)
            outpix[outx, outy] = inpix[inx, iny]
    return out

'''

The straightening works pretty well, but there is a little distortion that I think is caused by the peephole not being a perfectly spherical lens. Also, because the peephole is not centered on the camera lens, my concentric ring transformation isn't centered either.

From here, I needed to figure out where the sky ends and the buildings or trees start. Unfortunately, the buildings and trees are both lighter *and* darker than the sky in different places, so I can't just look for one type of transition. To detect the edge, I scan down each column of pixels and calculate the difference in darkness between consecutive pixels, ignoring whether the change was from light to dark or the reverse. The image below shows those differences, amplified by 10x to increase the contrast. The mathematicians call this calculation a finite forward difference.

<a href="http://pingswept.org/img/differentiated.jpg"><img src="http://pingswept.org/img/differentiated-300x150.jpg" alt="The derivative of each column of pixels" title="The derivative of each column of pixels" width="300" height="150" class="aligncenter size-medium" /></a>

Here's the finite difference code.

'''
(lang=python)
# Code under GPLv3; see pysolar.org for complete version.
def differentiateImageColumns(im):
    (width, height) = im.size
    pix = im.load()
    for x in range(width):
        for y in range(height - 1):
            pix[x, y] = min(10 * abs(pix[x, y] - pix[x, y + 1]), 255)
    return im

'''

The last step is to scan down each column looking for the first large value. The first change that crosses a threshold is recorded. The final output is an array of values that measure the angle of the highest obstruction as a function of direction. As a sanity check, I drop a red dot on each value. It's hard to make out in the thumbnail below, but if you click on the image below, you'll get a larger version where you can see the red dots work pretty well.

<a href="http://pingswept.org/img/redlined.jpg"><img src="http://pingswept.org/img/redlined-300x150.jpg" alt="Red dots highlighting the first large change in each column" title="Red dots highlighting the first large change in each column" width="300" height="150" class="aligncenter size-medium" /></a>

I think the next step will be to calculate the total energy delivered per year using <a href="http://pysolar.org">Pysolar</a>.

Here's the full code.

'''
(lang=python)
# Code under GPLv3; see pysolar.org for complete version.
from PIL import Image
from math import *
import numpy as np

def squareImage(im):
    (width, height) = im.size
    box = ((width - height)/2, 0, (width + height)/2, height)
    return im.crop(box)

def despherifyImage(im):
    (width, height) = im.size
    half_width = im.size[0]/2
    half_height = im.size[1]/2
    inpix = im.load()
    out = Image.new("L", (width, half_height))
    outpix = out.load()
    full_circle = 1000.0 * 2 * pi
    for r in range(half_width):
        for theta in range(int(full_circle)):
            (inx, iny) = (round(r * cos(theta/1000.0)) + half_width, round(r * sin(theta/1000.0)) + half_width)
            (outx, outy) = (width - width * (theta/full_circle) - 1, r)
            outpix[outx, outy] = inpix[inx, iny]
    return out

def differentiateImageColumns(im):
    (width, height) = im.size
    pix = im.load()
    for x in range(width):
        for y in range(height - 1):
            pix[x, y] = min(10 * abs(pix[x, y] - pix[x, y + 1]), 255)
    return im

def redlineImage(im):
    (width, height) = im.size
    pix = im.load()
    threshold = 300
    for x in range(width):
        for y in range(height - 1):
            (R, G, B) = pix[x, y]
            if R + G + B > threshold:
                pix[x, y] = (255, 0, 0)
                break
    return im

im = Image.open('spherical.jpg').convert("L")
im = squareImage(im)

lin = despherifyImage(im)
d = differentiateImageColumns(lin).convert("RGB")
r = redlineImage(d)

r.show()

'''
