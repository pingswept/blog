---
layout: post
title: Estimating air changes per hour with a blower door
---
When I was trying to [figure out how big a gas boiler we needed] [1] for our house a few months ago, I tried to account for both the insulation in our walls as well as the air leaks that let warm air escape as cold air sneaks in. I had read that an old, drafty house turns over its volume in air once per hour. That seemed high to me, but I was looking for a conservative estimate, so that's what I used in my calculations. Since then, I've been hoping to find a way to make a better estimate.

A friend of mine from Stanford, Colin Fay, runs a company with his dad, David Fay, called [Energy Metrics] [2]. Last weekend, Colin and his nearly homonymic associate Cullen were kind enough to bring Colin's blower door over to our house to run a test to see how drafty our house is.

The basic idea of a blower door is this: you fill your front door with a massive fan that forces air out of the house. While it's doing that, a small sensor measures the air pressure difference between the inside and outside of the house. There are a few different tests you can run, but the standard test that the fan controller runs is to automatically adjust the fan speed until the pressure difference is 50 Pa. This pressure is roughly equivalent to the pressure from a windspeed of 20 mph, but blowing at your house uniformly from all directions. Atmospheric pressure is around 100,000 Pa.

Colin's blower door, a Retrotec 2000 with a DM-2 Mark II controller, pulled air through our house at 3900-4000 ft<sup>3</sup> per minute to generate a pressure difference of 50 Pa. Our house has a volume of around 18000 ft<sup>3</sup>, so we were replacing all the air in our house every 4.5 minutes, or 13.3 times per hour.

[1]: http://pingswept.org/2010/01/03/sizing-a-new-gas-boiler/
[2]: http://energymetricsne.com
