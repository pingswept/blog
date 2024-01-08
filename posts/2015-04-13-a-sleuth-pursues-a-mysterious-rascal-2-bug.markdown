---
title: "A sleuth pursues a mysterious Rascal 2 bug"
slug: a-sleuth-pursues-a-mysterious-rascal-2-bug
author: Brandon Stafford
lastmod: 2015-04-13T13:38:49.000Z
date: 2015-04-13T13:35:20.000Z
source: rascalmicro.com
---
The upper deck on the Rascal 2 will have a Freescale Kinetis MK20 processor on it, so it can act like a Arduino, or a [Teensy 3.1](http://www.pjrc.com/teensy/), or a [Fadecandy](https://www.adafruit.com/products/1689). (The Teensy 3.1 uses the same chip, and the Fadecandy is almost identical, but with slightly less memory.) To prototype this, I've been building a demo that involves a Rascal 2 brain (the Beaglebone Black, hereafter BBB) talking to a Fadecandy. The Fadecandy will run an animation of flames on some WS2812 LED strips.

<iframe src="https://player.vimeo.com/video/124675767" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>


I got the Fadecandy working with BBB as a preliminary test a few months ago. Then, a couple days ago, I pull out a new BBB and try plugging in the Fadecandy. Curiously, the board shuts down after around 10 seconds. Since the power LED goes out, it looks like the power management chip is detecting a fault and cutting power. I unplug the Fadecandy and reboot. The BBB *still* shuts down after 10 seconds or so. No matter how many times I reboot the board, even with nothing attached, it shuts down a couple of seconds after reaching a login prompt.

Time to call on un1tz3r0.

![](https://farm4.staticflickr.com/3305/3178893768_c60ae8f519_z_d.jpg)

I head over to un1tz3r0's sublair, inside Blake's secret lair. (Here's Blake's lair during the construction of the [Penrose Triangle](http://penrosetriangle.com/wordpress/) in 2013.)

![](http://penrosetriangle.com/wordpress/wp-content/uploads/2013/07/02.P1010343_edit_1200x-1024x576.jpg)

After I eat one of his jelly doughnuts, Z3r0 pulls out a Fadecandy and BBB that he had from some LED art project. We set them up on his bench with a Samsung phone charger supplying the power. I'm a bit skeptical of the power supply, but I don't say anything because Z3r0 gave me a jelly doughnut and who am I to complain?

Z3r0's setup works immediately. We see, in `dmesg`, something like this:

    [    1.276945] usb 1-1: skipped 1 descriptor after interface
    [    1.277044] usb 1-1: default language 0x0409
    [    1.277357] usb 1-1: udev 2, busnum 1, minor = 1
    [    1.277373] usb 1-1: New USB device found, idVendor=1d50, idProduct=607a
    [    1.277385] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [    1.277396] usb 1-1: Product: Fadecandy
    [    1.277406] usb 1-1: Manufacturer: scanlime
    [    1.277416] usb 1-1: SerialNumber: IAHO-ROTCIV-ONIDNOC
    [    1.277878] usb 1-1: usb_probe_device
    [    1.277895] usb 1-1: configuration #1 chosen from 1 choice
    [    1.278006] usb 1-1: adding 1-1:1.0 (config #1, interface 0)
    [    1.278360] usb 1-1: adding 1-1:1.1 (config #1, interface 1)
    [    1.278811] hub 1-0:1.0: state 7 ports 1 chg 0000 evt 0002
    [    1.278845] hub 1-0:1.0: port 1 enable change, status 00000103

So what's wrong with my setup?

Piece by piece, we replace each element of his system with mine. My Fadecandy works with his BBB. We add my USB cable, and it still works. Finally, all my stuff is working, using just his power supply. That suggests that the problem was my power supply back at the Asylum, but that's unlikely because I was running off the [Rascalfarm](http://rascalmicro.com/2015/03/23/the-rascalfarm/), so at least 4 other Rascals are running on the same power bus, and they've all been working fine for months.

Z3r0 lets me borrow his power supply (OK, be honest, it's just a USB phone charger), just in case, and I head back to the Asylum. I thank him for his assistance and doughnut, and he vanishes into his lair (and sublair). It is 35 and raining. In New England, we call this "spring."

Back at the Asylum, I plug the working system into the Rascalfarm power supply. My understanding of the universe is piped to /dev/null as the system shuts down after 10 seconds. I wonder whether Z3r0's doughnut was laced with something. This is insane. All the other boards in the Rascalfarm are still running off the same 5 V supply.

I switch to Z3r0's power supply, and the damn thing starts working again, so now I know that the problem must be the power supply. When I measure the voltage, the problem is revealed: the supply voltage is sagging 0.5 V between the power supply output and the Rascalfarm power connector. The effect of this is that the first 4 boards work fine, but when the 5th board tries to boot, it can't quite get the juice it needs at the 10 second mark. (I'm not sure exactly what subsystem is being turned on then.)

Here's what's going wrong:

![](/img/rascalfarm-voltage-sag.jpg)

When I boost the power supply up to 5.5 V to compensate for the sagging, everything starts working.

My power supply may be a high-precision beauty, but even it is subject to Ohm's law.

#### Epilogue ###

This morning, I rewired the Rascalfarm with fat, low-resistance wire. Problem solved.

Thanks for the doughnut, Z3r0.
