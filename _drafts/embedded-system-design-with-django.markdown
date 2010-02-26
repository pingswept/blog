---
layout: post
title: Designing embedded systems with Django
---
I've built a few embedded systems recently using Linux and MVC frameworks. I made a controller for Eerik's drinkbot (unfinished, sorry Eerik) and a thermostat that can be monitored through the web.

*Background on tiny computers*

There are thousands of tiny computers for monitoring and control systems for sale around the world. Generally, they fall into two categories: small (microcontrollers like the Arduino, which run $10-500) and large (embedded controllers like National Instruments hardware, which cost $500-5000).

To use the small ones, you write code from scratch, perhaps with some pre-written libraries to talk to certain peripherals and a bootloader to run your code on power-up. The vast majority cannot be connected to the internet without substantial effort, and when connected to the internet, they aren't powerful enough to work like most servers on the internet. For example, a webserver built on a microcontroller would be overwhelmed by the background noise on the internet, i.e. traffic from bots and viruses. This kind of system is perfect if you want to log temperature in your basement, or turn on a light whenever the garage door is open.

The large ones come with an operating system, like Windows CE, Linux, or VxWorks. Most of the devices are reworked versions of hardware from the pre-internet days that have had Ethernet ports added to them. They can handle real internet traffic, but they usually use proprietary software to do it.

To my knowledge, there are no tiny computers that can handle real internet traffic that also allow the low price and ease of use of systems like the Arduino.

*How web software development has changed*

In the 90's, software development for the internet meant either writing server software or designing static web pages. Starting around 2000 (give or take a few years), websites started incorporating dynamic data, which was stored in databases. Around 2005, a new kind of web software gained popularity-- the Model-View-Controller framework-- with the release of Ruby on Rails.

(skipping some details)

With old-style web development, a web programmer would write code that inserted data into the database, more code that updated the database with new data, and more code that retrieved and sorted the data for presentation in a web page. With an MVC framework, the programmer writes out a template for how the data should be presented on a webpage, and the framework figures out what to request from the database. MVC frameworks can't scale to the level of a big website like Amazon, but for a personal blog or a small business, they work fine and reduce the programming time needed dramatically.

*Merging modern web development and microcontrollers*

Most of the time, what people want to do with microcontrollers is log some data from sensors and maybe trigger some actuators in response. After they log the data, people want to analyze the data, make graphs with it, and then do it again, maybe with a different sensor. This matches well with the typical database-backed website. The only substantial additions are code to interact with hardware-- read sensors and trigger actuators.

*Proof of concept*

Using an off-the-shelf microcontroller kit that cost $339 plus shipping, I installed a Python MVC framework called Django and wrote code to make it act like a thermostat to replace the one in our kitchen. It took about 2.5 weekends to write the code, which is much faster than I could write a similar application for something like an Arduino, and this was my first try. (I had played around with Django a few times previously, but this was my largest effort by far. It's worth noting that I could write a similar application even faster using a GUI tool like LabView, but that requires specialized hardware that cost 3-10 times more-- either a dedicated PC with a USB device for sensors, or a industrial controller with a sensor module.)
