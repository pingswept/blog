---
title: "Rascal 0.3 in the works"
slug: rascal-0-3-in-the-works
author: Brandon Stafford
lastmod: 2014-03-01T15:44:26.000Z
date: 2010-09-28T00:00:00.000Z
source: rascalmicro.com
---
The circuit boards for the next revision of the Rascal arrived from Illinois while I was in New York for [the Open Hardware Summit][1].

The new board has a few changes that I hope will be improvements. On the bottom of the board, the programming connector is replaced with just a set of flat pads. The goal is to allow the boards to be programmed without soldering a connector to the board.

<img src="/img/secret-jtag-port.jpg">

I made an adapter that converts the 20-pin programming connector to a smaller Samtec connector with spring-loaded pins. Instead of straight, stiff pins, the Samtec part ([FSI-110-06-L-D-E-AD-TR][2], if you're interested) has pins that bend into a loop at the end. As you press the connector against the board, the loops flex, making a low-resistance connection between the pin and the pad. In theory, the scrubbing of the pin loop across the pad is supposed to clean oxidation off the contact. I measured the contact resistance at 0.2 ohms.

The connector also has locating pins to insure that the pins are lined up correctly and can be held in place with #2-56 bolts.

<img src="/img/jtag-adapter.jpg">

<img src="/img/jtag-adapter-on-board.jpg">

One experiment that turned out reasonably well is the logo I added to the board. The Rascal circuit board is a 4-layer board, meaning that the board consists of 4 layers of copper interleaved with 3 layers of fiberglass. As is common with 4 layer boards, the two inner layers are power planes, meaning that they're mostly solid copper sheets connected to +5 V or ground. Because many chips have multiple power and ground connections, this makes routing those connections very easy-- next to each pin that needs a power or ground connection, you just drop a via to the correct power plane, and you're done. Also, the large ground plane act as low-inductance return paths for the currents flowing in traces, thereby minimizing the noise that high-speed signals in one trace induce in nearby traces.

Looking at the last revision of the Rascal, I noticed that the edges of the board were translucent, because the power planes are pulled back from the edge by 1 mm or so. I thought I might be able to use the translucency to make a cool effect. To embed the logo, I made a gap in the outer copper layers and added the text to the internal layers. At first glance, the logo is invisible, but when you hold it up to the light, the fiberglass is translucent, but the copper is not. The logo font is not correct, because the Rascal logo is actually slightly tweaked from a commercial font, but I'll fix that later.

<img src="/img/rascal-micro-translucent-logo.jpg">

The next Rascal should be ready on Wednesday, October 6, 2010. In addition to the logo and the secret JTAG port, the new rev will also have a serial flash for the bootloader and the Ethernet port correctly terminated, biased, and decoupled. If all goes as planned, it won't spontaneously switch to half-duplex mode any more, and it will be able to boot Linux without any human intervention.

[1]: http://www.openhardwaresummit.org/
[2]: http://www.samtec.com/ProductInformation/TechnicalSpecifications/Overview.aspx?series=FSI
