---
date: 2008/07/20 00:00:00
format: markdown
title: Tower of epic fail in Dubai
---
A gentleman by the name of David Fisher has been getting some attention (examples: <a href="http://online.wsj.com/public/article/SB117625795099465923-WFaTx4FSsy1oW4x8lS4eK1518io_20070418.html">WSJ</a>, <a href="http://www.newyorker.com/talk/2008/07/21/080721ta_talk_goldberger/">New Yorker</a>, <a href="http://www.inhabitat.com/2007/05/16/david-fishers-twirling-wind-power-tower/">Inhabitat</a>)  by describing his design for a new building in Dubai. It would be best for the world if bad ideas like these were ignored and forgotten, but without some knowledge of engineering, it's not obvious that his ideas are bad.

Fisher's tower is like a shish-kebab on a vertical skewer, where the skewer is an elevator shaft and the food are the apartments. Each apartment can rotate around the elevator shaft. This alone is perhaps impractical, or ugly, or dumb, but not impossible. If you could find a wealthy fool who wanted to build this, you could probably pull it off.

Where Fisher crosses the line into territory that I defend is with his claims about renewable energy. He says that there will be a wind turbine between each apartment, and solar panels on the roof of each apartment. According to <a href="http://www.dynamicarchitecture.net/home.html">his website</a>, the building will "generate electricity for itself as well as other nearby buildings, making it the first skyscraper designed to be self powered." As Walter says in The Big Lebowski, "OVER THE LINE!"

Before we even look at the available energy closely, we can be certain that it won't work. One of the central problems of renewable energy is its low power density. According to the ever trusty Vaclav Smil, wind and solar typically yield 1-10 W/m^2; skyscrapers require in excess of 1000 W/m^2, (<a href="http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=11363">Energy in Nature and Society</a>, pp. 311, 317). But perhaps Mr. Smil is wrong. Let's take a closer look.

Judging by <a href="http://www.dynamicarchitecture.net/schema/schema_big.htm">the drawings</a> of Fisher's tower (since removed), it would be about 300 x 50 m. Ignoring the narrowing of the tower as it rises, roughly 20% of the area is devoted to wind turbines. That's around 15000 x 0.2 = 3000 m^2. (Fisher has described two versions of the tower, one at ~300 m with 60 floors, another at 420 m with 80 floors. Here, I analyze the shorter of the two.)

Fisher claims that the average wind speed in Dubai is 16 km/h, or 4.4 m/s.

Assuming a Rayleigh distribution for the wind speed, the average power available as kinetic energy in the wind is (6/pi) * 0.5 * (density of air) * area * (average velocity)^3.

The density of air is 1.2 kg/m^3.

That's (6/3.14) * 0.5 * 1.2 * 3000 * (4.4^3) = 290 kW. If the wind turbines were 30% efficient, which would be pretty good for a vertical axis turbine stuck in a building, the yield would be 100 kW.

This ignores the narrowing of the building, the lack of wind near the ground, and obstruction from other buildings.

The building has around 50 m * 50 m * 60 floors = 150000 m^2 of floor space, so the areal power density is about 0.67 W/m^2. Say a room is 5 m in a side, so it has area of 25 m^2. That gives you 17 W per room.

But let's not leave out the solar power! Fisher claims that 20% of each roof will be exposed to sunlight. On average, then, if photovoltaics yield around 1 W/m^2, we should expect a power density based on floor area of 0.2 W/m^2, which is another 5 W per room, 22 W total. **That might be enough to light a single compact fluorescent light bulb in each room.**

Oh, and the average temperature in Dubai is 27 C. I guess they can run the air conditioning when all the lights are off.

I should end by saying that I share Mr. Fisher's enthusiasm for renewable energy. My concern is that his tower of epic fail gives the work that I spend all day on a bad name. We should be building wind turbines and installing solar panels as fast as we can, but we should do it in ways that optimize their performance. Put the solar panels where they will never be shaded by the floor above them, and put the wind turbines on ridgelines where the wind is strongest. **Integrating turbines and panels into buildings with the expectation that they will produce energy to spare is moronic.**

(And all you energy reporters should be ashamed of yourselves for repeating Fisher's void claims without any skepticism. That means you, Paul Goldberger and Evelyn Lee!)
