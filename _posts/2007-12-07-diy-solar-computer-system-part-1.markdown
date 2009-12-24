--- 
wordpress_id: 151
layout: post
title: DIY solar computer system, part 1
wordpress_url: http://pingswept.org/2007/12/07/diy-solar-computer-system-part-1/
---
Like a lot of semi-urban computer enthusiasts who plan on living for a few decades after the onset of global warming, I have a few computers that are always on, and I wish that I could find an economically viable way of reducing the emissions generated as a side effect of the power they require. Also, when the hard times come and grid power gets flaky or drops out entirely, it would make the local warlord happy if I could use a computer to calculate optimal irrigation ditch depths, or the like. (Note to self: learn to use abacus while leisure time still exists.)

Typically, solar arrays in urban or suburban areas are tied by an inverter to the local power grid. Such inverters cost a few thousand dollars; they both allow excess power to be released to other consumers and enable the use of AC appliances without any modifications. I live in a rented property, so installing a large solar array on the roof with an inverter in the basement is not an option. But, maybe I could run a smaller array without an inverter for DC loads only.

**DC vs. AC**
Computers, generally designed to connect to AC power, have as their first component a switching power supply that turns AC from the wall into DC. If I had a solar array, it would output DC, which would be converted to AC by the inverter, and then back to DC by each computer’s power supply, losing energy at each step. I call this "dumb"– why not just run the computers off of the DC directly?

The problem is that if you run the computers just off DC from the solar panel, the computers die when the sun is occluded by a cloud or a planet (at night, for example).

**An alternative architecture**
The system I'm building has a 24 V DC power supply fed from the grid at its core. This will run in parallel with whatever solar panel I eventually set up. For starters, I have replaced the ATX power supply that came with <a href="http://pingswept.org/2007/06/03/finally-booting-pre-installed-linux-on-an-oem-pc/">my desktop</a> with a DC/DC converter from Ituner.com. I then power that from a beautiful DIN-mount Sola SDN 10-24-100P supply that I got off Ebay for $33.00 ($45.82 with shipping).

<a href="http://www.flickr.com/photos/pingswept/2081081733/" title="Sola SDN 10-24-100P power supply by Ping Swept, on Flickr"><img src="http://farm3.static.flickr.com/2313/2081081733_116bbb2f97_m.jpg" width="180" height="240" alt="Sola SDN 10-24-100P power supply" /></a>

For the DC/DC converter, I looked at the pico-PSU, but rejected it in favor of the slightly larger M2-ATX-HV.

<a href="http://www.flickr.com/photos/pingswept/2057881038/" title="The DC-DC converter strapped in place by Ping Swept, on Flickr"><img src="http://farm3.static.flickr.com/2379/2057881038_98231f3cdd_m.jpg" width="240" height="180" alt="The DC-DC converter strapped in place" /></a>

The M2-ATX-HV had a few advantages:
<li>My PC has an ATX12V power supply; I wasn't sure that it would run with a standard ATX supply. ATX12V has a second connector with 4 pins, which the M2-ATX-HV provides.</li>
<li>The HV version allows a wider input voltage. The Sola supply is nominally a 24 V supply, but I want to be able to run off both 12 V and 24 V supplies, plus a few volts on either side.</li>
<li>Slightly higher power-- with its original supply, my PC idled around 85 W, and I could get it to draw 150 W by ripping a CD while keeping both cores busy, one transcoding a variable bit rate mp3 to constant bit rate, the other compiling the Python interpreter. For reference, the CD drive used around 35 W. The DC/DC converter I got is rated for 140 W. As a pleasant surprise, the new supply is substantially more efficient, and the system, including the loss in the Sola supply, now draws only 65 W at idle.</li>

The M2-ATX-HV is a bit bigger, but my PC case is pretty large, so that wasn't a concern. Including all the cables and shipping, I paid $96.40 for the M2-ATX-HV-- about $30 for the advantages listed above.

<a href="http://www.flickr.com/photos/pingswept/2057100393/" title="Side view, case open, 24 V DC supply by Ping Swept, on Flickr"><img src="http://farm3.static.flickr.com/2180/2057100393_eb82525bc3_m.jpg" width="180" height="240" alt="Side view, case open, 24 V DC supply" /></a>

**Stage 1 complete**
The DC system has been working reasonably well for a few weeks now. Next, I have to find a cheap way to test current sharing with a solar panel, as I don't want to commit the full $700 or whatever for a 180 W panel until I have more evidence that it will work. I'm off to the beach to start collecting sand for a little homebrewed Czochralski action.
