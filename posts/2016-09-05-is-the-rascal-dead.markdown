---
title: "Is the Rascal dead?"
slug: is-the-rascal-dead
author: Brandon Stafford
lastmod: 2016-09-05T21:22:38.000Z
date: 2016-09-05T21:22:38.000Z
source: rascalmicro.com
---
**Short answer:** At least until 2017, maybe forever. I'm teaching freshman engineering at Tufts University this fall. In conjunction with my efforts at raising a 3-year-old, this means the Rascal is on hold.

**Long answer:** First, a quick summary of the history. I started the design of the original Rascal in April of 2010 and sold the first run of 15 production units in January of 2012. After a few hardware tweaks in small batches of ~20 units in 2012, I made larger runs of ~100 units in late 2012 and 2013 while I worked on the software. I also [designed the Precision Voltage Shield](http://rascalmicro.com/2013/03/21/bringing-an-analog-voltage-arduino-shield-to-life/), started manufacturing it here in Somerville, and selling it alongside the Rascal.

Around the same time, I worked on a couple of interactive public art projects with public artists Dan Sternof Beyer and Bevan Weissmann. In the winter of 2012-2013, Dan and I made the [giant lightblades on Boston's Greenway controllable by text messages](http://www.newamericanpublicart.com/colorcommons/). In the summer, I built the electronic guts of the [Culture Tap kiosks](http://www.newamericanpublicart.com/culturetap/) that Dan and Bevan installed on Tremont Street in Boston.

In late 2013, my daughter was born, which shifted my view of life tremendously. I went from wanting to build my own Rascal Micro embedded systems empire to just wanting to do satisfying engineering work with a schedule flexible enough to raise my daughter well. As Chris Rogers, my colleague at Tufts, said to me, "Yeah, when you have kids, that's when you start thinking."

I [announced the Rascal 2 in 2014](http://rascalmicro.com/2014/03/31/announcing-rascal-2/) and made a batch of 10 prototypes. At the same time, I also founded a second company with Dan, Bevan, and 2 other friends of mine: [New American Public Art](http://newamericanpublicart.com).

I also worked on a number of short consulting projects with friends of mine:

* a new, lighter version of the TD-1B chain tensioner for holding aircraft onto carriers for the US Navy
* an analytics dashboard for a wind turbine company
* a wireless data acquisition system for recording data from inside tank treads for the US Army
* Built in mid 2014: Blue Hour in Camden, New Jersey

At some point in 2015, I discovered that someone in China was selling [lousy A/D boards under my product's name, "Precision Voltage Shield"](http://www.geekbuying.com/item/Arduino-Precision-Voltage-Shield-PVS--AD7298-12-bit-8-channel-ADC-for-UNO-Mega-2560---DT-studio-343180.html). The unfortunate part is that they used a lamer chip, so it only gives 12 bits of precision, which is the same as the Arduino Due and the Arduino Zero. They also used bare male pins for the input lines, which is a step down from the screw terminals I used, but whatever. Have fun shorting out your board anyway.

That was exciting for me-- someone thought my product was good enough to want to take the name! (If I had to name the board again, I think I'd pick something different; I'd probably call it an Analog Input Shield, because that's the term the Arduino folks use.)

In parallel, sales of the Rascal started to flag. I had already announced the Rascal 2, and compared to all the other cheaper, faster boards available now, the original Rascal is slow and underpowered (though still easier to use, I would argue).

In 2015 and 2016, New American Public Art really started taking off. In the winter, we rebuilt [Blue Hour for a light festival in Baltimore](http://www.newamericanpublicart.com/blue-hour-lc) in March. This was followed by one of most ambitious installations, [Ourself in Camden, New Jersey](http://www.newamericanpublicart.com/ourself).

Finally, in 2016, I was offered a job at Tufts teaching freshman [how to make stuff](http://hwtmkstff.com). I had intended to keep selling Rascals and Precision Voltage Shields, but as I was preparing to teach the class this summer, I started getting support emails about a board that is electrically quite similar to the Precision Voltage Shield, but cheaper. (Maybe it's not electrically identical, as the Precision Voltage Shield works, and, at least from the emails I got, this one seems not to. On the other hand, their satisfied customers would not be emailing support.) This left me with a dilemma-- do I want to try to compete with the folks undercutting me or not?

![](/img/Screen-Shot-2016-09-05-at-5-17-36-PM.png)

[Ian MacKaye](https://en.wikipedia.org/wiki/Ian_MacKaye), a founder of Dischord Records, talks about how he wants to make the number of records that people want to buy. If 1000 people want a record, he wants to press 1000 copies, not 10,000 or 100. I feel the same way about my business. If the world demand for Precision Voltage Shields is sopped up by these boards from China, great. I have no interest in trying to flog the universe with advertising to get people to buy something from me. I'd rather find a new problem worth solving.

So that's where I stand. I'm going to teach this class at Tufts; after that, I'll probably build a new Rascal, if no more compelling problem needs solving.

Also, hello to all you Tufts students. I see you googling me.