---
layout: post
title: Building a web-accessible thermostat
---
As a proof of concept for the idea of using web frameworks like Django in embedded applications, a few weeks ago I built a thermostat that you can monitor through the web. Various people have asked me for more details, so here they are.

### First, the hardware.

The thermostat in place

<a href="http://www.flickr.com/photos/pingswept/4361956125/"><img src="http://farm5.static.flickr.com/4014/4361956125_b8c6d6bb58.jpg" width="375" height="500" alt="The web thermostat in place" /></a>

Close-up of the hardware

<a href="http://www.flickr.com/photos/pingswept/4361956323/"><img src="http://farm3.static.flickr.com/2695/4361956323_9b99e8aedb.jpg" width="500" height="375" alt="Close-up of the hardware" /></a>

The heart of the hardware is a Technologic Systems TS-7500, which is a small PCB with an ARM processor, an SD card, and some RAM. The 2 GB SD card holds a copy of Debian Linux, to which I added a few software packages, most notably the Apache webserver, SQLite, and Django 1.1. The TS-7500 also comes with a shell script that can call a few short C programs to toggle specific output pins on the ARM processor.

The TS-7500 is plugged into a carrier board called the TS-752. Among other peripherals, the carrier board has a few relays and a temperature sensor. Both boards are enclosed in a TS-ENC750 enclosure.

### The software

When you request http://thermo.pingswept.org:8080/thermolog/, the webserver matches the string "thermolog" against a list of pages in [urls.py][1]. The first pattern (below) matches and directs us to the function called index in [thermo/thermolog/views.py][2].

<pre class='brush: ruby'>
(r'^thermolog/$', 'thermo.thermolog.views.index')
</pre>

[1]: http://github.com/pingswept/thermopyla/blob/master/thermo/urls.py
[2]: http://github.com/pingswept/thermopyla/blob/master/thermo/thermolog/views.py