---
categories: energy, projects
date: 2009-09-13T00:00:00.000Z
format: markdown
title: Building a green server
---

Ever since a brief stint as a network administrator in 2005, I've admired the discipline of data backup with undeserved zeal. A little more than three years ago, I <a href="http://pingswept.org/2006/03/29/building-my-own-secure-mail-file-and-web-server/">decided</a> that I should probably build my own server as a data repository; it could also serve this blog, store my email, and so forth. At the behest of <a href="http://www.mwgaa.com/blog/">my friend Mike</a>, who once claimed that the massive data breach that Google will eventually suffer will be worse than September 11th, I also kicked my Gmail habit. (Mike has not kept up his end of the bargain, and still uses Yahoo Messenger. Also, he owes me a comic book about penguins.)

Last spring, as we were getting ready to move to Somerville, I had accumulated most of a server, but I didn't really have a good place to put it. Now that we've moved, I have an insulated attic, a moderately dry basement, and most importantly a killer garage. If the house burns down, the data is safe in the garage!

While I am definitely a sucker for an attractive rackmount server with hot-swap drives, I'm even more of a sucker for energy efficiency. I did some research and built what was, at the time, the greenest server I could build with consumer-level components. With the recent release of solid state hard drives, I don't think I can claim to be setting any records, but I think I'm doing pretty well in terms of required cooling power per processor cycle.

The rig:

* Dual Xeon L5410 quad core processors
* 1U rackmount case, RM1002T
* Sparkle 80plus power supply, FSP400-601UG
* Western Digital low power drive, WD5000AACS
* Asus DSBV-DX motherboard
* Two Corsair 1 GB DDR2 667 MHz FB-DIMM
* Quiet, low power fans (Antec 40mm Ball Bearing Case Fan from ANTOnline through Amazon.com)

Total power consumption started at 131 W with the processors idle, but I was able to reduce it to 102 W by replacing the stock fans with the quieter Antec fans. I haven't actually measured the peak power consumption yet judging by the processor specs, I expect it to be at least 200 W, but probably not more than 250 W.

I tried the server in the poorly-insulated garage this summer, and it overheated pretty quickly. The revised plan is to try the aforementioned moderately dry basement, which affords the additional interesting opportunity of building a geothermal cooling system for it. (Yes, it's a ridiculous idea-- ridiculous and awesome.)

I don't know if I'll ever get around to that, but I'm starting with a water cooling system, which I think is a necessary precursor to a geothermal system. If the water cooling works, I might turn it into a water pre-heater for our domestic hot water heater. I <a href="http://pingswept.org/2009/07/10/drain-heat-recovery/">previously calculated</a> our hot water load at around 2 kWh per day, which is an average power of 83 W, less than the average power of the server. We'd certainly lose a lot of the heat along the way, but if I'm going to dump waste heat somewhere, it might as well be into water I want to heat anyway.

(Before you go rushing off to Treehugger.com, note that this "heat your water with your PC" plan is not an economically sound proposition-- heat from electricity is about 4 times more expensive than heat from natural gas.)
