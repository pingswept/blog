---
title: "Announcing Rascal 2"
slug: announcing-rascal-2
author: Brandon Stafford
lastmod: 2014-03-31T17:37:34.000Z
date: 2014-03-31T15:35:02.000Z
source: rascalmicro.com
---
The Rascal has been a steady seller over the last 2 years, but it's time for a hardware upgrade!

### Same philosophy, more reach ###

When I designed the original Rascal in 2010-11, the explosion of small ARM Linux boards (Raspberry Pi, Beaglebone, and the like) hadn't happened yet, and there were no Linux boards available with Arduino headers (except, briefly, a version of the late Chumby Hacker Board). To make an Arduino-compatible Linux board with a Python web interface out of the box, I had to build my own hardware. As a bootstrapped company, I couldn't afford to add any hardware capabilities beyond the most basic functionality.

Now, with small ARM Linux boards widely available, I can take the next step, which is to expand the capabilities of the Rascal by integrating sensors and motor driver circuitry. The goal, as has always been the case, is to make a small computer that makes an artist or scientist productive within a few minutes of taking the Rascal out of the box.

With the original Rascal, you got to skip the painful part where you wrestle with the Linux kernel and try to figure out how to cross-compile software for an ARM processor. With the Rascal 2, you will also get to skip the step where making the board talk to simple sensors drives you insane.

The Rascal 2 will probably run on top of one of the small ARM Linux platforms (probably the Beaglebone Black), which will mean better performance (2x the speed and 5-10x the RAM) at a lower price. The new Rascal will run the same software as the original with minimal changes under the hood to accommodate the new hardware.

![](/imgs/2014/Mar/rascal_2_artist_conception.png)

### New hardware features ###

The biggest change is that the Rascal 2 will come with a suite of sensors and motor drivers out of the box, so that you don't have to worry about figuring out how to make basic circuits work with the Rascal. The first prototypes of Rascal 2 will have four sensors: temperature, light, sound, and motion.

I might also add a few other hardware goodies to the Rascal: maybe an RS-485 transceiver or a connector for the [Adafruit Neopixel LED strips][2]. There may also be a higher-end version that will have an Arduino onboard to act as a real-time coprocessor, but that definitely won't be in the first release.

### New software features ###

The first step is to get the current software working on new hardware (well, first I need to *design* the new hardware). After that, the next big upgrade to the software will be to get websockets working with the onboard sensors out of the box, so that you can see a real-time graph of all the sensors' output in your web browser without writing any code at all.

### $50 off original Rascals until they're gone ###

The original Rascal is still [available in the Rascal store][1], now **$50 off**, for the next month or until the current batch is gone. There *might* be another batch if Rascal 2 takes me a while to build, but don't risk missing out forever on the original Rascal!

[1]: http://store.rascalmicro.com/products/rascal
[2]: http://www.adafruit.com/products/1138