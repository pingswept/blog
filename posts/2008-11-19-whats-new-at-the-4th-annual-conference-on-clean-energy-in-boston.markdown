---
date: 2008-11-19T00:00:00.000Z
format: markdown
title: What's new at the 4th Annual Conference on Clean Energy in Boston
---

I'm taking notes at the 4th Annual Conference on Clean Energy in Boston today; I figured I might as well share what I learn with the world.

The Massachusetts Technology Collaborative has funded <a href="http://www.mtpvcorp.com/">MTPV</a>, a start-up in the Boston University Photonics Center, with $500k. (I think this is actually not news to the world, but it was news to me.) MTPV has an interesting technology. Their scheme is a variation on thermophotovoltaics (TPV). In conventional TPV, you put a very hot plate next to a solar cell. The cell absorbs the radiation coming off the plate, allowing you to get electricity from heat. Unfortunately, the efficiency is quite low. MTPV does the same thing, but with the hot plate ridiculously close to the solar cell. Their claim is that when the gap between the cell and the hot plate reaches the micron level (the M in MTPV is for micron), the efficiency increases dramatically, and they have some test data to prove it.

Maintaining a consistent micron-scale gap is a mechanical challenge. They do it by putting small bumps on the surface of their hot plate and then clamping the plate to the cell. They have some clever geometry that minimizes the heat transferred through the bumps, as that is also an efficiency loss.

**Investment pitch #1**
Srikanth Gopalan from Boston University described a "solid oxide membrane" which takes in waste and steam and emits syn-gas and 7 cc/min of hydrogen gas per cm^2 of membrane. Dr. Gopalan and his colleague Dr. Pal have three year plan that requires $500k per year for device testing and scale-up by 2011.

**Investment pitch #2**
Scott Faris, CEO of <a href="http://www.planarenergy.com/">Planar Energy Devices</a>, says that Planar is making metallic lithium batteries. 4x capacity and 10x lifetime, 80% cost reduction. Doesn't catch on fire like metallic lithium batteries used in cellphones in the past. There are no liquids in their batteries. They bury the lithium anodes under solid glass electrolyte. Faris says that Planar is using <a href="http://www.google.com/search?q=miley+cyrus+best+of+both+worlds">"the Miley Cyrus strategy,"</a>-- the best of both worlds-- using thin film technologies, but scaling up to the size of prismatic batteries.

Planar has two products in development at present: a small battery called the PowerPlane: 25 x 29 mm, 12 mAh, and the larger PowerBlade, 100 mm by 100 mm, 4.8 Ah, 520 Wh/L. The PowerBlade is being tested by the military at present. Planar is pursuing Series B funding for pilot production.

**Side note:** Faris followed the irritating standard of the battery industry and quoted capacity in amp-hours rather than watt-hours. Amp-hours is not a measure of energy capacity, but of the number of electrons that can be induced to flow out of the battery. For example, a 1200 mAh NiMH battery contains around 20% less energy than a 1200 mAh alkaline battery because the NiMH battery runs at ~1.2 V, while the alkaline runs at ~1.5 V.

I suspect that this amp-hours habit developed because lead-acid battery manufacturers wanted to hide the fact that their voltage dropped as the battery discharged, making the amps that come out near the end of a discharge cycle less powerful than the amps near the beginning. If you speak in terms of amp-hours, you can avoid this embarrassing truth. Generally, modern batteries have a much flatter discharge curve, so watt-hours ends up being a linear multiple of amp-hours. Modern batteries have much less to hide in this regard, though there is still the variation across chemistries to account for. Nonetheless, the habit persists throughout the battery industry.

**Investment pitch #3**
Andrew Dillon, CEO of <a href="http://varentec.com/">Varentec</a>, described their solid-state electronic transformer that operates at 20-50 kHz. Dillon claimed that their transformer is 10x smaller and lighter than those of competitors that operate at 1 kHz, and costs 25-40% less. Undersea transmission, as required of offshore wind turbines, requires DC for efficient operation; photovoltaics also produce DC, so making transformers will be a lucrative business in the next few years. They want $1M for their first 1 MW high-voltage DC system, which they hope to build in 8 months of 2009.

**Investment pitch #4**
John Thomson, President and CEO of <a href="http://yieldenergy.com/">Yield Energy</a>. They are a biogas developer. There are already 5000 biogas plants in operation in Europe, but no utility scale plants in the US. They use expired food products from grocery stores and waste from restaurants as their feedstock. Negotiated exclusive rights to proprietary pre-processing technology from Fitec in Germany. They have 6 sites currently under development; the first is near Toronto, Canada.

**Investment pitch #5**
Chris Sauer of <a href="http://www.oceanrenewablepower.com/home.htm">ORPC</a> started with a bold statement: "We have saved the best for last today." They've raised $2M and have recently tested their kinetic tidal generator in the Bay of Fundy. The systems are "horizontally-mounted cross-flow turbines" that look like helical Darrieus windturbines or <a href="http://www.gcktechnology.com/GCK/pg2.html">Gorlov turbines</a> on their sides. The turbines are made of composites and foam so they float. They tie the turbines down to the sea floor for operation and release for service. Unlike their competitors in New York, <a href="http://pingswept.org/2007/08/13/tidal-turbines-in-the-east-river-facing-fundamental-limits/">Verdant Power</a>, they have no cantilevered blades. Sauer says they can get 250 kW per bladeset in a 6 knot current; 1 MW in a module of 4. He claimed their costs are 6-7.5 cents/kWh for a location with a peak current of 6 knots.

If all goes according to plan, their first module of 4 bladesets will be installed in Q4 2010. Their first commercial installation will be in Q4 2011 in Western Passage up near Lubec. ORPC has raised $4.5M so far; they're hoping to close Series A funding $10M in Q1 of 2009.

One of their competitors, <a href="http://naturalcurrents.com/">Natural Currents</a>, also had a table in the expo hall.

Somerville locals <a href="http://www.secondwind.com/">Second Wind</a> also had a booth in the expo hall. (Disclosure: my employer has worked for Second Wind.) They make various tools for measuring how much wind is available in different places. Their latest product, <a href="http://www.secondwind.com/PDFdocs/WindTech9-2008.pdf">the Triton</a> (540 kB PDF), looks like a megaphone the size of a dumpster, pointed at the sky, with a solar panel bolted to the side of it. The thing is absolutely amazing. It emits sound waves at a slight angle from the vertical. The reflections that come back are Doppler shifted, and staggered in time. The frequency shift is proportional to the air velocity and the delay is proportional to the height. They can change the direction of the signal, so they can tell wind direction too. Their range is around 160 meters. This is so much better than setting up a tower with a bunch of wind vanes and anemometers. I predict that these guys will own the market in a few years.

So that's how I spent my morning. The rest of the day was debugging a PLC in a warehouse.
