---
title: "Rascal 0.4 with Arduinos and shields"
slug: rascal-0-4-with-arduinos-and-shields
author: Brandon Stafford
lastmod: 2014-03-01T15:45:29.000Z
date: 2010-11-01T00:00:00.000Z
source: rascalmicro.com
---

I just received the next revision of the Rascal (0.4); the boards should be assembled by next week.

Like the previous versions, the new Rascal can mate with most Arduino shields. I haven't tested them all, and they're not all supported in software yet, but mechanically, they fit together. Unlike the older boards, the new Rascal can also talk to an Arduino, which itself can connect to a shield of its own.

The idea here is to let the Arduino and the Rascal each play to their strengths. The Arduino is cheap and easy to program, but not powerful enough to run a full operating system. It's great for reading sensors and controlling motors, but lousy for serving web pages or running a filesystem. The Rascal, on the other hand, can do all of that more advanced stuff. Unfortunately, this makes the Rascal bad for tasks where instantaneous responses are needed, like controlling a motor. For example, a Rascal would do a lousy job of running a CNC machine-- the machine would jitter every time someone requested a page from the webserver.

The combination of the two is powerful-- the Rascal acts as the interface to the outside world, the datalogger, the supervisor of the Arduino. The Arduino runs in a tight loop, receiving instructions from the Rascal over a serial port, and then driving the motors with precision. There's some overlap, of course. The Arduino, with the right shield, can serve simple webpages or store data to an SD card. Similarly, the Rascal can toggle digital outputs and read sensors as well.

That's the concept for how the devices work together. The mechanical interaction is shown below. The Arduino plugs in underneath the Rascal. Shields can attach in two places-- in the left position, they connect to the Rascal; in the right, they connect to the Arduino.

<img src="http://test.rascalmicro.com/img/rascal-0-4-arduino-shield-diagram.png">
