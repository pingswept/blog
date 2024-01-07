---
title: "Stenciling PCBs on my desk"
slug: stenciling-pcbs-on-my-desk
author: Brandon Stafford
lastmod: 2014-04-16T22:01:57.000Z
date: 2014-04-16T22:01:57.000Z
source: rascalmicro.com
---
I try to assemble as many Rascal Micro products as I can myself here in Somerville. The Rascal itself has a ball-grid array processor, which is really hard to assemble reliably by hand, but simpler stuff I can handle.

For my Precision Voltage Shield, I assembled the first one by hand with a fine-tipped soldering iron and a microscope. The board worked great, but the process was stressful because I feared accidentally bridging the fine-pitch pins on the A/D converter. On the first board, I did actually bridge a few, but I was able to fix it up with solder braid. It was nerve-wracking.

Once I validated the shield's design by testing the first board, I ordered a laser-cut Kapton stencil from [Ohara Rapid Prototyping](http://ohararp.com/stencils/). This let me run a typical surface-mount solder process: squeegee solder paste onto each shield, place the components on the shield with tweezers, and run them the shields through an oven to melt and then resolidify the solder.

The Kapton stencil worked well, but the setup was fiddly. I found it hard to keep the stencil aligned as I swapped in multiple PCBs. Part of this was because Kapton and tape are flexible materials. The way I aligned the PCBs referenced the edge of the PCB, which wasn't very repeatable as some of my PCBs have fuzzy edges from where they were snapped out of panels.

The standard industrial solution to this is a big machine called a [stencil printer](http://www.manncorp.com/smt/cat-210-1/smt-stencil-printers.html). A used one off Ebay would cost around $5000, or maybe $15,000 new. The next step down is a manual jig that costs around $1300. There are also [cheaper versions](http://www.madelltech.com/m2-4.html) in the neighborhood of $400, but those use the same "taped-down PCBs" mounting method that was giving me trouble before. The description of the positioning method sounds like it's just pairs of opposing clamps, which also put me off. If I didn't love building precision jigs, I would probably buy the $1375 [STP-350](http://www.madelltech.com/stp350.html).

### Building an open source hardware stencil printer ###

Instead, I'm building a manual, open source hardware stencil printer. My hope is that I'll be able to sufficiently document a design that someone with access to a 3D printer, a tablesaw, and a drill press, plus some pre-made parts from a couple industrial suppliers, will be able to build a functioning printer. I've built the beginning of my printer, and while I can already imagine things that I would change in a subsequent revision, I think that it will work. The picture below shows an overview of the current design.

![](https://farm6.staticflickr.com/5493/13785451135_a17327d35c_c.jpg)

The thumbscrews in the back will clamp a stencil that can pivot up and down on the shaft that you can see poking out from behind the aluminum U-channel. The shaft is precision ground and slips into bearings that are pressed into pre-made pillow blocks. It's essentially a hinge that will force the stencil to return to the same place every time it is lowered. (I got my first stencil from [Stencils Unlimited](https://www.stencilsunlimited.com/), but it's too early to tell whether it will work. It sure looks good.)

The black optical breadboard will be mounted on top of a two-layer stage for positioning. The bottom layer positions the PCB in one direction; the upper layer takes care of the other direction plus rotation.

The key requirement of the printer is that it positions the PCB with no detectable backlash, *i.e.* if you try to wiggle the PCB gently with your finger, it should not move.

The two pictures below show pre-made locating pins embedded in 3D printed parts. The locating pins are designed to fit snugly in a 1/8" hole, which is convenient because that size hole also accommodates both #4-40 and M3 bolts. The 3D printed parts are reasonably precise, but it doesn't matter if they're off a little bit, because you can just loosen the cap screws that hold them in place and reposition them. This is also designed to be adjustable for PCBs of various different sizes.

![](https://farm8.staticflickr.com/7270/13785844204_4d453b6000_c.jpg)

![](https://farm8.staticflickr.com/7081/13785504755_d73c408f34_c.jpg)

So now we have the PCB held rigidly; we just need to position it under the stencil with an adjustable mechanism that doesn't introduce backlash. You can see the beginning of the Y-axis positioning in the three springs in the first picture above. My plan is to oppose those springs with a fine-pitch bolt so that cranking the bolt in and out moves the platform in and out, with the spring taking out all the backlash.

In the long run, the documentation for the project will live on [the OSHW stencil printer page](http://rascalmicro.com/docs-oshw-stencil-printer/).

(And yes, I should be working on the Rascal 2, but people keep ordering Precision Voltage Shields, so I have to keep building them, and the fiddly stencilling is killing me!)