---
title: "First iteration of OSHW stencil printer complete"
slug: first-iteration-of-oshw-stencil-printer-complete
author: Brandon Stafford
lastmod: 2014-05-01T18:57:13.000Z
date: 2014-05-01T18:57:13.000Z
source: rascalmicro.com
---
(Background: I'm building a manual stencil printer for applying solder paste to circuit boards. The hardware design will be open source. There are more details in [the first post about my stencil printer](/2014/04/16/stenciling-pcbs-on-my-desk/).)

After a couple of failed mechanism designs, the first working iteration of my open source hardware stencil printer is complete. The stage can adjust the PCB position in X, Y and rotation while allowing no detectable backlash. Here's the system with the frame and PCB in place.

![](/img/stencil-printer-prototype.jpg)

Here's a close-up of the stencil lining up with the pads of the PCB. You'll notice that very little of the red PCB is visible, which is a good sign, as it means that when I squeegee solder paste through the stencil, it will land on pads rather than the bordering regions of PCB.

![](/img/stencil-for-stencil-printer.jpg)

### What went right ###

The low-backlash positioning mechanisms I made worked surprisingly well. The basic mechanism was a plate of high-density polyethylene (HDPE) that slid on dowel pins encircled by compression springs. A 1/4-20 socket head cap screw threaded into a PEM insert forces the HDPE plate to slide along the dowel pins, while the springs oppose that motion, eliminating backlash. This is how I built the X and Y stages.

The rotation mechanism was similar, but instead of two sliding dowel pins, it used a spring in tension that pulled a shoulder bolt against a small HDPE plate, which was adjusted by a 1/4-20 bolt like the other stages. Rotation required the different implementation to translate the linear motion of the bolt to rotation.

Here's a diagram of the mechanisms.

![](/img/stencil-printer-mechanisms-800px.jpg)

The hinge that holds the stencil clamp used a ground 3/8" shaft that connected bearings in pillow blocks to shaft mounts. I was not able to detect play between the bearings and the shaft.

The optical plate and locating pillars worked well. The plate was the most expensive single component, but it added a lot of flexibility to the system, and it looks cool.

### What went wrong ###

Plenty went wrong with this iteration. Here's a list, plus a few ideas about what I'll fix when I iterate again. This iteration seems workable, but there are some bits that are a bit finicky. I'll probably use it now, and then rebuild it better when it breaks.

* On the X stage, the dowel pins don't slide smoothly. This is because when I expanded the holes, I used a hand drill rather than a drill press, and I misaligned the holes. In realigning them, I gouged up the sides of the holes. Stupid.

* The 1/4-20 threads are a bit coarse. #10-32 bolts would give 60% better resolution, so I'll probably use those instead. The bolt heads are also hard to turn by hand, so I should add some knobs, like these [thumb screw knobs](http://www.mcmaster.com/#94052a031).

* The shaft collars that I used to keep the stencil clamp from sliding sideways on the hinge shaft were too loose. They were machined pieces of HDPE pressed on the shaft. They provided a little lateral resistance, but not enough. I'll replace them with [split shaft collars](http://www.mcmaster.com/#6436k133) and space them off the bearings with some 3/8" washers. (Vic convinced me to use HDPE collars in the first place. Sorry, Vic!)

* The stencil clamps failed utterly. I designed them to clamp the frame against the U-channel from below. The clamping worked great, but the clamp knobs were hard to reach and banged into everything. C-clamps that pinch the edges of the stencil are cheap, easier to set up, and more adaptable to different stencils. They win in every way.

* The locating pillars worked well, but the design can be simplified. The slotted arms don't work very well for positioning. I'll redesign them so they can work with [Newport's BC-5 base clamps](http://search.newport.com/?x1=sku&q1=BC-5).

* The 3D-printed flexures that guide the stages worked, but I fear they won't be durable. One of them cracked while I was playing with it. Their deflection range is barely adequate, and I suspect they will creep over time. I made a revised version that uses a spring-loaded plunger. The springs are the same as those used on the stage slides. Here's the improved version (also 3D-printed).

![](/img/stencil-printer-plunger.jpg)

### What happens next ###

Next week, I'll use the printer to assemble some [Precision Voltage Shields](http://store.rascalmicro.com/products/precision-voltage-shield). I'll probably also make a few easy upgrades-- the shaft collars and knobs mentioned above. I may also print modified locating pillars.

### If you're interested . . . ###

If you've made it this far and are interested in more details, send me an email: brandon@ the domain of this blog. If I get a few emails, I'll document construction in more detail.
