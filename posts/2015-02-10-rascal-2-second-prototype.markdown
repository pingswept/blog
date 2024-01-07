---
title: "Rascal 2: second prototype"
slug: rascal-2-second-prototype
author: Brandon Stafford
lastmod: 2015-02-10T20:34:42.000Z
date: 2015-02-10T20:32:35.000Z
source: rascalmicro.com
---
Most of my time in the last few months has been devoted to developing the radiation monitoring system mentioned in the last post, but in the gaps, I've made some progress on the Rascal 2. The image below shows what is mostly a mechanical prototype. The bottom PCB is nearly identical to the first prototype, but with the accidentally rotated connectors fixed. The top PCB is really just a copy of the first PCB cut down with a jump shear so I could check the mechanical fit of various components.

![A handsome black and yellow striped circuit board](/img/rascal2-prototype-2015-01-19-820px.jpg)

It's proving surprisingly difficult to join two stacked PCBs mechanically and electrically in a reliable, cheap, and compact fashion.

![hand drawing of a stack of PCBs with various electrical connectors between them](/img/pcb-stack-calculations-2015-02-10.jpg)

The specific problem that I ran into is that the male pins and threaded inserts that I want to use step 0.125" between sizes, but to seat the pins reliably in their sockets, I want their tips positioned vertically within a range of a 0.050" or so. The best match I could find raises the top PCB up quite far (0.375") and then uses long pins to reach back down to the lower PCB. The positioning is great, but it makes the whole system huge.

Here's the mechanical prototype. The aluminum hex standoff is the part marked "M" in the drawing above. The exposed metal pins are marked "C".

![photo of the stack of PCBs sketched in the previous drawing](/img/pcb-stack-prototype-2015-02-10.jpg)

Overall, this is good progress-- the connectors look like they'll work, even if the whole stack is taller than I would like.