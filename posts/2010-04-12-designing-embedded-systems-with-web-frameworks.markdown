---
categories: django, embedded electronics, engineering, geekery, linux, python, rascalmicro
date: 2010-04-12T00:00:00.000Z
format: markdown
title: Designing embedded systems with web frameworks
---

I have a prediction.

We're about to see a shift in embedded systems development. Around 2008 or 2009, embedded microprocessors like the one in your cellphone, reached a threshold where they can perform as decent webservers without special tuning. Even with a slow database query or some inefficient templates, they've got the speed to handle real web serving. This means that suddenly the most efficient development pattern for embedded systems is not the proprietary hardware and software tools that have dominated the industry for the last 30 years, but the open source web development tools that have arisen in the last decade. 

The transition will be painfully slow, and of course there are some niches where specialized hardware and real-time control will preclude the use of generic web tools-- motion control springs to mind. But I think that the combination of cheap hardware and modern web frameworks will crush the industrial controller market, like digital cameras did to film cameras.

**First, some background on tiny computers**

There are millions of tiny computers used for monitoring and control systems around the world. Let's break them into two categories: small (microcontrollers like the Arduino or a PIC development board, which runs $10-500) and large (embedded controllers like National Instruments hardware, which cost $500-5000).

To use the small ones, you write code from scratch, perhaps with some pre-written libraries to talk to certain peripherals and a bootloader to run your code on power-up. The vast majority cannot be connected to the internet without substantial effort, and when connected to the internet, they aren't powerful enough to work like most servers on the internet. For example, a webserver built on a small microcontroller would be overwhelmed by the background noise on the internet, i.e. traffic from bots and viruses. This kind of system is perfect if you want to log temperature in your basement, or turn on a light whenever the garage door is open. They're no good for running an inventory management system in a warehouse with 20 workers.

*Below: an Arduino*

<img src="http://upload.wikimedia.org/wikipedia/en/thumb/0/05/Arduino_Duemilanove_2009b.jpg/800px-Arduino_Duemilanove_2009b.jpg" width="600" />

The large ones come with an operating system, like Windows CE, Linux, or VxWorks. Most of the devices are reworked versions of hardware from the pre-internet days that have had Ethernet ports added to them. They can handle real internet traffic, but they usually use proprietary software to do it. They're shaped like a long, skinny shoebox.

*Below: a larger controller*

![A programmable logic controller](http://upload.wikimedia.org/wikipedia/commons/4/42/PLC_Control_Panel.png)

The change is that something equivalent to the iPhone, which uses a 600 MHz ARM processor, can store years of data and serve it up to anyone with a web browser in seconds with hardware cost of a few hundred dollars. Industrial controllers lose on cost of both hardware and programming time, and performance. The hardware has to be expensive to support the R&D costs, which are borne entirely by each manufacturer. There's just no way that even a large industrial control company, which might have a dozen dedicated programmers at best, can compete with the thousands of developers working on open source web software worldwide.

**How web software development has changed**

In the 90's, software development for the internet meant either writing server software or designing static web pages. Starting around 2000 (give or take a few years), websites started incorporating dynamic data, which was stored in databases. Around 2005, a new kind of web software gained popularity-- the web framework-- with the release of Ruby on Rails.

With old-style web development, a web programmer would write code that inserted data into a database, more code that updated the database with new data, and more code that retrieved and sorted the data for presentation in a web page. With a web framework, the programmer writes out a template for how the data should be presented on a webpage, and the framework figures out what to request from the database. Web frameworks can't scale to the level of a big website like Amazon, but for low traffic systems, they work fine and reduce the programming time needed dramatically.

Most of the time, what people want to do with microcontrollers is log some data from sensors and maybe trigger some actuators in response. After they log the data, people want to analyze the data, make graphs with it, and then do it again, maybe with a different sensor. This matches well with the typical database-backed website. The only substantial additions are code to interact with hardware-- read sensors and trigger actuators. I think this is the least developed part of the systems I expect we'll see in the next few years.

**Proof of concept**

It's definitely possible that I'm just some blowhard on the internet. I mean, I'm *at least* some blowhard on the internet, but I might still be right in predicting this change. To that end, I've done some testing to see whether I'm going in the right direction.

Using an off-the-shelf microcontroller kit that cost $339 plus shipping, I installed a Python web framework called Django and wrote code to make it act like a thermostat to replace the one in our house. It took about 2.5 weekends to write the code, which is much faster than I could write a similar application for something like an Arduino with an Ethernet carrier board, and this was my first try. I had played around with Django a few times previously, but this was my largest effort by far.

*Below: the proof of concept*

<a href="http://www.flickr.com/photos/pingswept/4361956125/"><img src="http://farm5.static.flickr.com/4014/4361956125_b8c6d6bb58.jpg" width="375" height="500" alt="The web thermostat in place" /></a>

The hardware interface is just a cron job that runs once per minute. It queries a temperature sensor on the PCB using a short C program called by a Python script, which also logs the data to a SQLite database. Retrieval of a webpage that queries the database for the last 300 datapoints (5 hours worth) and generates a chart of the data using Javascript takes around 1.5 seconds. That's with a processor running at 250 MHz (relatively slow) and the database stored on an SD card. Most of the time is spent converting Python datetimes to Javascript timestamps.

I could have written a similar application even faster using a GUI tool like LabView, but that requires specialized hardware that cost 3-10 times more-- either a dedicated PC with a USB device for sensors, or a industrial controller with a sensor module. With Django, I got an administrative interface, allowing different users and groups different levels of access, for free. If I want a central repository of users with LabView, I'm looking at another $800 for the "Datalogging and Supervisory Control Module." If I want to talk to a SQL database, I'll need the "Database Connectivity Toolkit" for another $1000. This is on top of the $1500 I would have paid for LabView already, plus the hardware.

Embedded control systems running web services are still an immature technology at best, but I think they'll grow up quickly in the next few years.

**Why are you writing this?**

I've been thinking about this change for a year or two now. I'm working on developing something like the Arduino, but a little heavier duty, so it can run a web framework, but with the hardware drivers pre-integrated. Send me an email at brandon at pingswept.org or post a comment if you want to know when it exists for real.
