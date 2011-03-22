---
format: markdown
date: 2010/04/29 00:00:00
title: Liquid metal batteries
categories: energy, engineering
---
I've recently started a contract at work for Professor Donald Sadoway's lab at MIT working on liquid metal batteries. I can't describe the details of the project I'm working on, but the research going on in the lab is quite interesting. The idea is to solve the problem of energy storage that accompanies all of our promising renewable energy solutions, like wind and solar. When the wind stops blowing or a cloud obscures the sun, the electrical grid still needs to supply energy to the world. If you only have a small amount of renewable power attached to your grid, you can just ignore the problem, but around 20% penetration, you get into trouble. Our best solution right now is either firing up natural gas turbines to cover the peak loads or pumping water up a hill when we have extra capacity so it can run down through a generator when we need it back.

What we really need are massive, cheap, efficient batteries. The idea in the Sadoway lab is to make something like an aluminum refinery, but instead of just sinking huge amounts of electricity to extract aluminum, you set up a reversible reaction so you could get the electricity back later.

Go take a look at this [awesome, enormous picture of one of these furnaces][1] in an aluminum refinery so you know what I'm talking about. Look at the size of the guy in the picture, and then look at how many furnace chambers there are in the row. That's an industrial scale operation.

To make aluminum, you dig bauxite out of the ground and use heat and sodium hydroxide to extract the part that's aluminum. What you get out, unfortunately, is oxidized aluminum, known as alumina. This is because aluminum, in its elemental form, reacts with oxygen, and when it sits in the earth for eternity, there's plenty of air seeping around, so all of the aluminum bonds with oxygen.

Fortunately, we have electrochemistry on our side. The large smelting furnaces in the picture you looked at a moment ago are long steel troughs that are lined with carbon and filled with aluminum oxide. These form the two electrodes in a chemical reaction. When electricity is run through the carbon into the aluminum oxide, the oxygen releases from the aluminum and bonds to the carbon, creating carbon dioxide, which is then vented to the atmosphere to help keep the planet warm. During the reaction, the aluminum oxide in the center heats up and liquefies, while the outer crust remains solid, sort of like the liquid-filled gum of the 70's, Chewels. (You may also recall Freshen-up, "the gum that goes squirt.")

To turn this process into a battery, we need an electrode that doesn't turn into a gas, and we'd like both electrodes to be cheap and lightweight, relative to the amount of energy they can store. Sadoway's lab started with one magnesium electrode and one antimony electrode, with a salt electrolyte in between. (They have since moved on to better combinations that I'm not at liberty to describe.) If you heat the core of the battery up to 700 C, everything becomes liquid, and the resistance drops substantially. Most remarkably, the three materials separate by density — electrode, electrolyte, electrode — all in a stack.

What's so great about a liquid metal battery? They have several advantages, notably extremely low internal resistance and huge current capability. Aluminum refineries run at currents above 100,000 amps. For comparison, most household circuitbreakers blow at 15 amps. The low resistance of liquid metals means that the battery is likely to charge and discharge very efficiently.

At first, the fact that the battery needs to run at high temperature seems like a major disadvantage — if you have to dump a lot of energy into heating, that makes the battery less efficient. This is true, but what's not obvious is what happens to a furnace's thermal behavior as it grows in size. In general, hot objects cool off in proportion to their surface area, which grows proportional to the square of the size of an object, roughly speaking. The capacity of a battery, however, grows with its volume, which is proportional to the cube of its size. This means that as the battery becomes huge, the amount of heat loss per unit of capacity decreases, i.e. the volume overwhelms the surface area. It's this same property that allowed icehouses in pre-industrial times to store ice well into the summer. There's some hope that at the right scale, with the right insulation, the small inefficiency in charging and discharging the battery will suffice to keep the core in the molten state.

So that's what I'm working on recently. (I'm still working on a Linux board on the side, but it's kind of on the back burner for the next month or so.)

[1]: http://www.kitimatworksmodernization.com/media/media%20materials/alm2001_7SHigh.jpg
