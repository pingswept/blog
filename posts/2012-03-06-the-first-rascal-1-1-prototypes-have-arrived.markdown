---
title: "The first Rascal 1.1 prototypes have arrived"
slug: the-first-rascal-1-1-prototypes-have-arrived
author: Brandon Stafford
lastmod: 2014-03-01T15:42:19.000Z
date: 2012-03-06T00:00:00.000Z
source: rascalmicro.com
---
After a lot of ordering parts, tweaking of PCB layouts, and optimizing the bill of materials, the new Rascals have arrived from the assembler in Colorado. 
<img src="/img/rascal-1.1.jpg" width="820px">

Whenever I build a new version of the Rascal, the big question is, "Have I made some horribly stupid error that has turned all of the parts I sent away to the assembler into landfill stuffing?" So far, I haven't found any landfill-worthy errors.

Here's the list of changes.

1. Added second USB host port and stacked USB connector
2. Put in a new Ethernet controller (Micrel KSZ8051RNL)
3. Moved the I<sup>2</sup>C/TWI pins to the Arduino-compatible location
4. Added I<sup>2</sup>S port for streaming audio
5. Changed JTAG footprint to work with pogo pins more easily
6. Switched to black Samtec headers rather than the blue ones, which were chintzy

### What works and what doesn't? ###
The new Rascal has two USB host ports. (Earlier Rascals have only one, and with a worse connector.) I plugged in an old Logitech webcam I picked up at the MIT flea market a few months ago and it was correctly identified by the kernel, as you can see in the command line snippet below.

```language-bash
[root@rascal1.1$:~]: lsusb
Bus 001 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 002: ID 046d:08b0 Logitech, Inc. QuickCam 3000 Pro [pwc]
```

Both USB ports are at least wired correctly, but I haven't tested them more thoroughly yet.

The hairiest change in this rev of the Rascal was the change to a new ethernet PHY chip, the Micrel KSZ8051. The new chip costs less, uses less power, requires fewer external caps and resistors to make it work, and, most importantly, won't be obsolete any time soon. The macb driver in the Linux kernel correctly identifies the controller, as you can see in the snippet of boot spew below, but the link doesn't come up. I'm not sure where the problem is yet.

```language-bash
MACB_mii_bus: probed
eth0: Atmel MACB at 0xfffc4000 irq 21 (02:71:82:06:00:14)
eth0: attached PHY driver [Micrel KS8051] (mii_bus:phy_addr=ffffffff:00, irq=-1)
```

I haven't tested the I<sup>2</sup>S or I<sup>2</sup>C ports yet.

The new JTAG interface worked for programming the kernel and bootloaders into the serial flash on the Rascal. I had to make a new programming fixture, pictured below. The beige part was printed on the Uprint 3D printer at Artisan's Asylum. The brass pins are pogopins, i.e. their tips are spring-loaded like (upside-down) pogosticks. The 20-pin black connector at lower right will connect to an Atmel JTAG pod, which then connects via USB to a PC.

Having access to high-quality 3D printing on the cheap (that part cost around $10) is definitely changing the way I design stuff. For low volume plastic parts like this, it's a huge improvement over sending stuff out to be machined out of Delrin with a 5 day turn for $500. 

<img src="/img/jtag-fixture-2012-03-05.jpg" width="820px">

Here's one last photo, which shows the Rascal in the fixture. The pogopins are under the PCB under the clamp.

<img src="/img/jtag-fixture-with-rascal-1.1-2012-03-05.jpg" width="820px">

If I can get the ethernet port working under Linux and no other problems emerge, I'll send the 20 remaining PCBs out for assembly, and they'll be available in the store for sale when I get them back. After that will come the first batch of 100 Rascals, which will be a *huge* milestone.

So far, so good!