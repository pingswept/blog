---
date: 2007/08/13 00:00:00
format: markdown
title: Tidal turbines in the East River facing fundamental limits
excerpt: After <a href="http://www.nytimes.com/2007/08/13/nyregion/13power.html">a New York Times article this morning</a>, <a href="http://fiveislandsorchard.wordpress.com/">Ben</a> and I were hashing over the potential for successful tidal turbines (well, he was ranting; I was hashing).
---
After <a href="http://www.nytimes.com/2007/08/13/nyregion/13power.html">a New York Times article this morning</a>, <a href="http://fiveislandsorchard.wordpress.com/">Ben</a> and I were hashing over the potential for successful tidal turbines (well, he was ranting; I was hashing).

Ben pointed out quite astutely that the requirements for a tidal turbine are actually surprisingly similar to a requirements for a wind turbine. The power density of both situations are similar. Wind velocity at a prime turbine location is in the low 10's of mph, while tides are in the low single digits of mph. However, the power density scales with the cube of the velocity, to wind gains a factor of 1000 over water. This is roughly canceled by the ~800x difference in density between water and air.

Additionally, the <a href="http://en.wikipedia.org/wiki/Reynolds_number">Reynolds numbers</a> for both situations are similar . The Reynolds number is Re = density * velocity * characteristic length / viscosity. Water is about 100 times more viscous than air, but that gets canceled by water's ~800x higher density and 10x lower velocity.

This means that you want roughly the same blade geometry and <a href="http://www.daviddarling.info/encyclopedia/T/AE_tip_speed_ratio.html">tip speed ratio</a> for a wind turbine as for a tidal turbine. The problem is that to get the same tip speed ratio in a medium that's moving 10x slower, you have to reduce the angular velocity by a factor of 10 as well.

The folks at Verdant, featured in the New York Times article, have figured this out; <a href="http://www.verdantpower.com/2000/01/25/how-fast-turbine/">they say that their turbines peak at 32 rpm</a>. According to <a href="http://www.wnyc.org/news/articles/76686">an interview with one of Verdant's engineers</a>, the turbines are about 5 m in diameter.

In the wind turbine world, Paul Gipe cites a 7 m wind turbine as having a peak speed of 310 rpm in his 2003 book <em>Wind Power</em> (p. 102), and Southwest Windpower's new Skystream turbine, with a diameter of 3.7 m, nominally peaks at 325 rpm. So, Verdant has the right tip speed ratio-- what's the problem?

The problem is that the power density is the same, the size is the same, the angular velocity is 10x lower, and wind turbine blades are already made of composite materials to withstand high torques. Power is torque * angular velocity, so for a constant power, if the angular velocity drops by X, the torque goes up by X. It's no wonder that Verdant's turbines are getting ripped apart. Their plan now is to use cast aluminum, which has a yield strength around 150 MPa; composite materials are an order of magnitude higher (and remember, they need to beat wind turbines by 10x, not just match them).

The New York Times quotes the founder of Verdant: "'The only way for us to learn is to get the turbines into the water and start breaking them,” said Trey Taylor, the habitually optimistic founder of Verdant Power."

Just to be clear, while I do <a href="http://greenmountainengineering.com">work in the renewable energy field</a>, I'm not a friend or enemy of Verdant; I had not heard of them before today. I don't have any investments in Verdant or any of their competitors.

Related links:
<a href="http://reddit.com/info/2evoc/comments/c2evph">Some guy's comment on Reddit</a>
