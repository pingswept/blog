---
format: markdown 
date: 2010/01/03 00:00:00
title: Sizing a gas boiler
categories: heating, engineering, estimation, energy
---

When you own a house, you are forced into bizarre contortions to reduce the cost of maintenance. For example, our roof needs to be replaced, but part of that is repairing the chimney. We don't *really* even need the chimney, because we don't have any fireplaces left-- they were all removed decades ago, well before we owned the house. But, until late this fall, when we installed a new boiler and water tank, we still needed a way to vent our ancient and inefficient gas boiler and water heater, or the basement would fill up with carbon dioxide and soot. We realized that if we replace those first, we can buy efficient systems that need only a plastic pipe through a basement wall to vent, rather than a chimney. Our heating cost would drop, and we could just toss the chimney in a dumpster, which is cheaper than repairing it, and need only be done once. Also, when we do replace the roof, we don't have to worry about finding someone with the skills to make a reliable flashing around the chimney.

As a result, we decided to replace our gas boiler and water heater. (The water heater actually had some life left in it, but we just wanted to do this once and be done with it.) An added advantage is that we could tear out the matrix of steel pipes that undergirds our first floor and replace them with PEX tubing, so I no longer have to wear a helmet when I walk around the basement.

Knowing that we're going to replace the boiler and water heater, someone had to figure out how big the replacements should be. The water heater is fairly easy-- we had a 40 gallon tank, which was plenty for the two of us, given that our shower uses around 6 L (1.5 gallons) per minute. Given that we were replacing the boiler and the water heater at the same time, it made sense to install an indirect storage tank, rather than a separate water heater. With an indirect setup, the super-efficient boiler heats water to warm the radiators in the house, but it also has a second loop that runs through a heat exchanger in a water storage tank. The heat exchanger is necessary so you don't end up drinking water filled with radiator rust. The boiler manufacturer we considered most seriously, [Viessmann][1], doesn't make a water storage tank smaller than 42 gallons, so that's what we chose. We also considered getting a boiler with an integral on-demand system (the [WB2 6-24C][2]), but the output looked a little shy of what we wanted. (She-who-takes-hot-showers overruled he-who-takes-long-showers on this one.)

Sizing the gas boiler is more difficult. Our old boiler was rated at 48 kW (164,000 BTU/h or 164 MBH). Our old boiler didn't modulate-- it either burned at full power or turned off. Using our gas meter and a stopwatch, I measured the full-power consumption at 3.0 ft<sup>3</sup> per minute, which is 53.5 kW for natural gas, slightly above the nominal rating of the boiler. On a cold evening recently, when the temperature was holding constant for several hours around 33° F outside and 66° F inside, and there was no sun and little wind, I measured the duty cycle of our old boiler. Over a 133-minute period, it was burning 26 minutes, which is about 20%. This means that average power going into the boiler with a temperature difference of 33° F between inside and outside was 11 kW. Maybe 8 or 9 kW of that actually makes it into the house, while the rest goes up the chimney.

**The choices**

I was trying to choose between the Viessmann WB2 6-24 and the larger 8-32. (The parts of the names of the models after the hyphens are close to, but not equal to, their peak output in kW-- perhaps they were the design targets.) Both models are extremely efficient condensing boilers; depending on how they're loaded, they operate in the 90-98% efficient range. As they're loaded closer to peak power, their efficiency drops. It also drops with the returning water temperature-- if the water comes back from the radiators cold, it's draws in heat from the burner more efficiently than if it comes back warm. The radiators in our house were installed before insulation and storm windows were standard, so they're quite effective at distributing heat.

This suggested to me that our new boiler would probably be operating near the high end of its efficiency range; the real danger was that in the fall and spring, when just a little heat was needed, it would inefficiently cycle on and off, because its lowest level of modulation would be too high. The larger of the two models I was choosing between cut off at 11 kW, which, you'll recall, was what we were using at 33° F with a much less efficient boiler, so that made the smaller one seem like a better fit. (For those of you unfamiliar with the weather in Boston, the [average daily high temperature in the coldest month][3] is 36° F in January.) My estimation was that on a really cold night, we might have a temperatures outside in the single digits, and we'd keep the house in the upper 50's or low 60's, so call that a delta of 50 degrees, about 1.5 times the 8-9 kW we needed at 33 F-- call it 14 kW to be safe.

The last factor I thought about was wind. Our house is not particularly exposed, but I suspect a cold wind could double the heat loss, which would definitely max out the smaller boiler, which peaked at about 25 kW, allowing for boiler inefficiency. If that were the end of the story, I would have chosen the larger boiler, but there were three other factors. The first was that the new boiler would zone the radiators, so I could turn off less critical rooms if we were short on heat. The second was that I'd rather invest money in insulation than a bigger furnace. Finally, we were thinking about installing a woodstove (for strictly recreational purposes-- Sundays, crossword puzzles, and so forth).

**The results**, _in which we learn whether Brandon is an idiot_

Against the advice of [the heating contractor][4], we got the smaller boiler. They did a beautiful job installing it in November. Last week, we had a very cold (sub-10° F), very windy night, and the system kept up with demand. We just got our first gas bill covering a month with the new boiler, and our gas usage dropped to 150 therms from around 250 therms for the same time last year, and last year was slightly warmer, so I'm pretty happy. The payback time on the added expense above the cost of an inefficient system will be less than 10 years, which is less than the warranty on the system (except the control electronics). The water storage tank, which is stainless steel, is warranted for the lifetime of the original owner in the original house.

I'd estimate that about half of the savings are from reductions in heated area (spare bedroom, attic) and half are from higher efficiency.

**Shortcomings**

But nothing is perfect. Because we replaced all the large, cast iron pipes in the basement with PEX tubing, the basement hovers in the low 50s in the winter, rather than in the low 60s. This was expected, but I decided I'd rather wear a winter hat than a helmet. Also, because we're not losing heat throughout the system, the boiler runs a little cooler than the old beast, which means that the radiant floor heat in the kitchen has trouble keeping up on the coldest days. I think I can probably fix that by tweaking the boiler target temperature and the circulation pump flow rates.

One other wrinkle is the control scheme used by the new system. Viessmann boilers come with an external temperature sensor, which is mounted outside on the north side of the house. Viessmann's intent (I think) is that the installer calibrates the system to drive the temperature of the hot water supplied to the radiators as a linear function of the outside temperature and the return temperature of the water. The idea is that when the temperature outside changes drastically, the boiler can react earlier than if it had to wait for the effect to be detectable in the radiator water or thermostats. Strangely, our boiler is set up to use the two programmable thermostats we used with the old boiler. The brain of the boiler targets 75° F, but the circulation pumps for the radiators and the floor heat only turn on when the thermostats call for heat. I'm not sure that this is actually worse, but it sure is strange to install an external sensor if you're not planning on using the signal.

**Pictures**

Here are the old system and the new system. If you click on the pictures of the new system, you'll get to Flickr, where I've added a few notes about what the different parts in the picture do.

*Old system with headbanging pipes*

<a href="http://www.flickr.com/photos/pingswept/4023572789/"><img src="http://farm3.static.flickr.com/2727/4023572789_b21316e438.jpg" width="375" height="500" alt="The old gas boiler and the headbanging pipes" /></a>

*New system*

<a href="http://www.flickr.com/photos/pingswept/4235209753/"><img src="http://farm5.static.flickr.com/4046/4235209753_a381527a67.jpg" width="375" height="500" alt="The new boiler" /></a>

*Supporting plumbing for new system*

<a href="http://www.flickr.com/photos/pingswept/4235210985/"><img src="http://farm3.static.flickr.com/2648/4235210985_2bace95e1c.jpg" width="375" height="500" alt="Ancillary plumbing" /></a>

[1]: http://www.viessmann-us.com/
[2]: http://www.viessmann-us.com/en/products/gas-brennwertkessel/vitodens_200.html
[3]: http://www.intellicast.com/Local/History.aspx?location=USMA0380
[4]: http://heatech.com
