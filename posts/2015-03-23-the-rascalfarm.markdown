---
title: "Building the Rascalfarm"
slug: the-rascalfarm
author: Brandon Stafford
lastmod: 2015-03-23T16:39:02.000Z
date: 2015-03-23T16:39:02.000Z
source: rascalmicro.com
---
Working with embedded Linux boards like the Raspberry Pi, or Beaglebone, you will fairly quickly realize that the hardware is far more polished than the software. It's not too surprising-- the boards are sold with the expectation that you will program the board to make it do what you want. Usually, the base software is just a Linux kernel with some hardware-specific drivers and basic Unix utilities added. I've found that some of the Linux kernels released crash as frequently as every couple of hours.

I'm now basing the Rascal on top of the Beaglebone Black hardware, so I needed a way to test the software in a more rigorous way than just, "Hey, this thing doesn't seem to have crashed while I was paying attention to it." To that end, I've been working on a rack of 15 Rascals that report over the network to a syslog server every time they reboot. In the long run, they will also emit a heartbeat signal that is monitored by a simple microcontroller on the rack. If one of the Rascals misses a couple of heatbeats, the microcontroller assumes the Rascal is dead and cycles the power to that board.

### Revision 1: a crappy prototype ###

My first attempt was just a maple 1x6 I scored during a makerspace cleanup a few months back. I sliced the board up into 2 shelves and 14 dividers. I used a pin nailer to attach the dividers to the base.

![10 Rascal prototypes in a wooden rack](/img/rascalfarm-rev1-2015-02-10.jpg)

It's hard to discern on the lower shelf, but the rainbow of Ethernet cables is plugged into a 16 port switch.

Rev 1 was marginally functional, but it had a few problems: it took up a lot of space on my desk, the Ethernet cables I had didn't quite span the slots, and the dividers were really wobbly. But hey, it only took an hour or two to make.

### Revision 2: would you like a biscuit? ###

To stiffen up the dividers, I switched to wooden biscuit joints. I also reshaped the rack into two stacked rows of Rascals with the Ethernet switch in between. This also shortened the average cable span so that all the Ethernet cables reached.

I cut the biscuit slots using a biscuit joiner in my basement. Each biscuit was spaced from the previous one as it was cut with a 1.522" +/- 0.010" spacer block. The picture below shows the first divider and spacer in place. The major weakness of this design is that the errors in position accumulate from slot to slot. One of the levels came out beautifully, but the second one was off by around 0.100" by the last divider. I hadn't done much woodworking with hard maple before, so I didn't realize that this much error would look sloppy in the end. With pine, I could have just clamped the bejesus out of everything, and it would look fine (though not exactly square).

![a biscuit joiner next to a board with slots cut in it](/img/rascalfarm-rev2-biscuit-joiner-2015-02-10.jpg)

(Here are the slots with the biscuits inserted.)

![two boards with biscuits inserted](/img/rascalfarm-rev2-biscuits-2015-02-10.jpg)

The second revision was decent-- it took up less desk space, it was extremely rigid, and all the cables reached their targets. Unfortunately, the gaps in the joints annoyed me every time I looked at the Rascalfarm. The power wiring was also still messy.

The second revision also let me test the Arduino and relay system for power cycling. I wired the relays so that they are normally closed, so if the Arduino hangs, the Rascals can keep running.

![a wooden rack of Rascals](/img/rascalfarm-rev2-2015-02-10.jpg)

### Revision 3: in which lasers are fired at acrylic

For the third revision, I switched to a hybrid wood-acrylic architecture. The dividers are Chemcast GP blue 2069 acrylic, 1/4" thick, from Delvie's Plastics.

To make the slots in the shelves precise, I built a dado sled with a small steel pin pressed through its face. As each slot was cut, the pin fit snugly into the previous slot. This proved highly repeatable, so the slots were finally spaced properly. Here's the sled after I cut all the shelves. You can see the pin near the blade slot.

![](/img/rascalfarm-rev3-dado-sled-2015-02-11.jpg)

Here's the first shelf getting slotted.

![](/img/rascalfarm-rev3-dado-cutting-2015-02-11.jpg)

Here's the final assembly. The socket head cap screws on the ends are threaded into threaded inserts; getting those positioned with their axes perpendicular to the board ends was difficult. Before insertion, I chamfered the holes so that the inserts wouldn't tear up the board surface as the first threads bit in.

I also added a vintage analog current meter, so I could tell at a glance that the Rascals were cranking (each board uses around 0.250 mA).

![](https://farm8.staticflickr.com/7625/16284368324_2e69ff9fcf_b_d.jpg)

### Preliminary kernel test results ###

I haven't gathered good statistical data yet, but with the time I have spent testing Rascals in between Rascalfarm revisions, I figured out one significant fact: there was a significant bug in the Linux kernel that affected the reliability of the Beaglebone Black (and anything based on it, like the Rascal) for several months in 2014.

The problem was that, for some kernels in the 3.9-3.18 range, the USB OTG driver could screw up the board's power management system. The power management system (AKA the PMIC, "power management integrated circuit") watches the USB port to see if 5 V power is available. If it sees 5 V, it switches to that as a power source. Unfortunately, the USB OTG driver periodically pulsed the 5 V USB line high as a means of detecting whether a USB device had been plugged in. Occasionally, if the PMIC checked for 5 V at the same time, this short pulse was enough to fool it. The PMIC tried to switch to USB power just as the pulse ended. This resulted in the board power dropping, which caused a reboot. In my experience, this happened within minutes of booting and sometimes not for 18 hours. 

You can [follow the adventure](https://groups.google.com/d/topic/beagleboard/RMOTnQBgIo8/discussion) as this was unraveled on the Beaglebone mailing list. It was a gentleman in the UK, Terry Barnaby, who finally cracked it, so far as I can tell.

The conclusion of all this is that if you want a reliable Beaglebone Black kernel, use something from:

* the 3.8.x series (currently the default shipping from Adafruit)
* 3.14.23-ti-r33 or later
* 3.18-rc4 or later

OK, back to programming.