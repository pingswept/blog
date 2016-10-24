---
format: markdown
date: 2010/02/24 00:00:00
title: Estimating air changes per hour with a blower door
categories: energy, engineering, estimation, heating
---
When I was trying to [figure out how big a gas boiler we needed] [1] for our house a few months ago, I tried to account for both the insulation in our walls as well as the air leaks that let warm air escape as cold air sneaks in. I had read that an old, drafty house turns over its volume in air once per hour. That seemed high to me, but I was looking for a conservative estimate, so that's what I used in my calculations. Since then, I've been hoping to find a way to make a better estimate.

*Solution: Colin's blower door*

<a href="http://www.flickr.com/photos/pingswept/4360064655/"><img src="http://farm3.static.flickr.com/2751/4360064655_ab3e61ecaf.jpg" width="375" height="500" alt="The blower door in place" /></a>

A friend of mine from Stanford, Colin Fay, runs a company with his dad, David Fay, called [Energy Metrics] [2]. Last weekend, Colin and his nearly homonymic associate Cullen were kind enough to bring Colin's blower door over to our house to run a test to see how drafty our house is.

The basic idea of a blower door is this: you fill your front door with a curtain and a massive fan that forces air out of the house. While it's doing that, a small sensor measures the air pressure difference between the inside and outside of the house. There are a few different tests you can run, but the standard test that the fan controller runs is to automatically adjust the fan speed until the pressure inside is 50 Pa lower than outside. For comparison: 50 Pa is roughly equivalent to the pressure from a windspeed of 20 mph, but blowing at your house uniformly from all directions. Atmospheric pressure is around 100,000 Pa.

When the fan reaches a steady state, air is whistling in through all the gaps around your windows, doors and foundation, and you can tell where the problems are. For us, the largest draft was coming under the basement door. The next worst were the gaps between the sashes in our larger, older double-hung windows. In real life, I suspect that the gap under the basement door is not so bad-- the thermal gradient keeps the colder, denser air sunk down in the basement. I didn't realize it at the time, but most of the draft was probably coming down through our vestigial chimney.

Colin's blower door, a Retrotec 2000 with a DM-2 Mark II controller, pulled air through our house at 3900-4000 ft<sup>3</sup> per minute to generate a pressure difference of 50 Pa. Our house has a volume of around 18000 ft<sup>3</sup>, so with the fan blowing, we were replacing all the air in our house every 4.5 minutes, or 13.3 times per hour.

*Assembling the blower door frame*

<a href="http://www.flickr.com/photos/pingswept/4353799725/"><img src="http://farm3.static.flickr.com/2714/4353799725_a2b863cf1a.jpg" width="500" height="375" alt="Assembling the blower door frame" /></a>

*The blower door from the inside*

<a href="http://www.flickr.com/photos/pingswept/4360806754/"><img src="http://farm5.static.flickr.com/4058/4360806754_e936fcae9c.jpg" width="375" height="500" alt="The blower door from the inside" /></a>

Once you know how drafty your house is with a fan pulling the heavens through it, you need to scale that to match the typical conditions for your house. As a rough rule of thumb: just divide by 20. With the fan, we had 13.3 air changes per hour, so that's about 0.7 air changes per hour without the fan.

But if you want to ascend to the peak of Mount Energygeek, and you're willing to do it unashamedly, you can use the empirical corrections of [Max Sherman of the Energy Performance of Buildings Group at Lawrence Berkeley National Lab] [3], who completed his thesis on modeling building air infiltration in 1980, when oil rolled down like waters and righteousness like acid rain. You [look up] [4] correction factors for climate (~18 for Boston), building height (0.7 for our house), wind shielding (1) and leakiness (1), multiply them together, and you've got a better correction factor than the rough guess of 20. For our house, we end up with 13.3/(18 x 0.7 x 1 x 1) = 1.06 air changes per hour.

With that knowledge, you can calculate the power required to offset the drafts cooling or heating your house. Our house, nominally a 1900 ft<sup>2</sup> Victorian, has an internal volume of 18000 ft<sup>3</sup>, or 510 m<sup>3</sup>, so when it's 0 C outside, we're heating about 1.06 x 510 m<sup>3</sup> of air per hour by around 20 C. The heat capacity of air is around 1200 J/m<sup>3</sup>C. That means we need to pour in 1200 J/m<sup>3</sup>C x 540 m<sup>3</sup> x 20 C every 3600 seconds. By my calculation, that's about 3.6 kW. 

The conductive heat loss model I developed for our house a few months ago when we were installing the boiler predicts that the conductive heat loss at the same temperature will be around 18 kW, so we lose about 1/6th of our heat from air infiltration.

Colin suggested we could reduce our draftiness by around 2x before we'd have to worry about the effects of too little fresh air (farts, basically). He suggested picking up a tube of transparent silicone caulk in the fall to fill the gap between the window sashes, as that's where our worst leaks are. In the spring, when it's time to open the windows again, the silicone peels off.

After seeing fellow energy geek Holly's sexy basement windows last weekend, I think I might look into replacing those as well.

[1]: http://pingswept.org/2010/01/03/sizing-a-new-gas-boiler/
[2]: http://energymetricsne.com
[3]: http://epb.lbl.gov/MHSherman/
[4]: http://www.homeenergy.org/archive/hem.dis.anl.gov/eehem/94/940111.html
