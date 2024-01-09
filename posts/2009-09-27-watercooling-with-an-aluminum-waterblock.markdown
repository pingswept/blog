---
categories: engineering, projects
date: 2009-09-27T00:00:00.000Z
format: markdown
title: Watercooling with an aluminum waterblock
---

Last night, I finished assembling the waterblock for the new server in my basement. Since I'm new to this watercooling stuff, I decided that a design where the fluid path through the server has no potentially leaky fittings along it would be a good starting place. I made the waterblock from two chunks of 6061 aluminum, with a loop of copper tube sandwiched in the middle. I milled a semi-cylindrical groove in each plate of aluminum with a ball-end mill, and added relief on one side to allow space for a 180 bend in the tube. The plates are clamped together with 1/4-20 socket head cap screws. As I tightened the bolts, I could see the gaps around the tubes disappear, so thermal contact between the tube and the plates is at least decent. Unfortunately, the upper plate doesn't make good contact with the lower one. By design, there's a nominal 0.010 in gap between the two plates before the tubes are compressed. I tried adding shim stock between the two, but I couldn't easily balance the contact force between the tubes and the plates, so I left out the shims.

**Half the waterblock**

<a title="Half the waterblock by Brandon Stafford, on Flickr" href="http://www.flickr.com/photos/pingswept/3959515718/"><img src="http://farm4.static.flickr.com/3443/3959515718_c32a112b26.jpg" alt="Half the waterblock" width="500" height="375" /></a>

**Disassembled view**

<a title="The waterblock disassembled by Brandon Stafford, on Flickr" href="http://www.flickr.com/photos/pingswept/3959510858/"><img src="http://farm3.static.flickr.com/2536/3959510858_907144d9f9.jpg" alt="The waterblock disassembled" width="500" height="375" /></a>

I fired up the server, and it looks like watercooling is a lot more effective than I expected. The blue line is for the CPU that was air-cooled, and the purple line is for the watercooler. The blue line dives after 10 minutes or so because that's when I realized one of the fans aimed at CPU1 had stopped. If the fans all worked, I bet the watercooler would still win on absolute temperature, but the fans might win on efficiency.

<a href="/img/watercool_chart_2009-09-26.png"><img src="/img/watercool_chart_2009-09-26-300x267.png" alt="watercool_chart_2009-09-26" width="300" height="267" /></a>

The circulation pump, a Laing SM-909-NT-14 designed for hot tubs, I think, is rated for either 15 or 65 W, depending on which part of the label you believe. (I'll have to measure it to find out for sure.) It maxes out at a volumetric flow rate of 8 L/min, but with the small diameter copper tube attached, it drops to 2.4 L/min (40 cm<sup>3</sup>/s). The ID of the tube is 0.48 cm, which puts the mean velocity at 2.25 m/s. The Reynolds number for this flow is around 1000, which is below the transition to turbulent flow, which occurs around 2300. Looking at the jet coming out the end of the tube, it looks laminar.

**Overview of the full setup**

<a title="The watercooling mad scientist lair by Brandon Stafford, on Flickr" href="http://www.flickr.com/photos/pingswept/3955041346/"><img src="http://farm3.static.flickr.com/2455/3955041346_e57793b378.jpg" alt="The watercooling mad scientist lair" width="500" height="375" /></a>

<a title="Aluminum waterblock with copper piping in place by Brandon Stafford, on Flickr" href="http://www.flickr.com/photos/pingswept/3954283747/"><img src="http://farm3.static.flickr.com/2495/3954283747_d1e35593fc.jpg" alt="Aluminum waterblock with copper piping in place" width="500" height="375" /></a>

You'll notice that the tube is wearing a beautiful brass fitting. This is a fitting that I clamped on during the bending process to keep the tube from sliding into the pipe bender and crimping, rather than bending in a nice radius. Unfortunately, I failed to realize that the section of tube with the fitting would be trapped between bends.

<a title="Close up of waterblock by Brandon Stafford, on Flickr" href="http://www.flickr.com/photos/pingswept/3955064222/"><img src="http://farm3.static.flickr.com/2518/3955064222_2014cdc7fd.jpg" alt="Close up of waterblock" width="500" height="375" /></a>

So, I call this a success. The next iteration of the waterblock will be made from copper, and I'm hoping to make two of them so I can actually run the server. I thought about trying to press tubes through reamed holes in a block, maybe with the help of a heater to expand the block, but I think I'll try a two-piece soldered design instead. My plan is to create a vaned cavity that guides a sheet of fluid across the processor, but I haven't figured out the details yet. Onward!
