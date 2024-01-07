---
date: 2007-06-03T00:00:00.000Z
format: markdown
title: Finally booting pre-installed Linux on an OEM PC
---

The Dell XPS 410n that I ordered on May 24th arrived this Saturday. After 10 years of using Linux, I was finally able to order a prebuilt computer from a major OEM without paying anyone for an operating system that I would delete shortly after unboxing. Instead of devoting half of Saturday afternoon to installing Linux, I had a working Linux system 19 minutes after opening the box. I think I probably spent more time picking a desktop background from Flickr than configuring the machine.

<a href="http://www.flickr.com/photos/pingswept/528118691/" title="Booting Ubuntu on a Dell XPS 410n"><img src="http://farm2.static.flickr.com/1186/528118691_1e9ea21829_m.jpg" width="240" height="180" alt="Finally booting pre-installed Linux on an OEM PC" /></a>

I didn't spend any time installing the DVD drive into the case or washing thermal grease off my hands. I opened the case briefly to take a <a href="http://flickr.com/photos/pingswept/528033148/">picture</a>, but I don't even know how many PCI slots I have. I can feel the freedom of blissful ignorance returning.

I half-expected Dell to screw up Ubuntu somehow-- add idiotic icons to the desktop (offers to connect me to the internets, shortcuts to crippled versions of photo editing software, or similar). I'm happy to report that they seem to have gotten it right. The Ubuntu they delivered is difficult for me to distinguish from the Ubuntu I've been installing for the past few years. Synaptic is set up to use the ubuntu.com repositories. Compiz is disabled by default. The boot process seems faster, but that may be the new hardware. The 2.6.20-15 kernel was installed; Synaptic installed 2.6.20-16 during the first update.

Ubuntu wasn't perfect-- it did fail to identify my HP f2105 monitor's maximum resolution of 1680 x 1050, and there was no way that a normal human would have been able to fix it. (I executed <code>sudo dpkg-reconfigure -phigh xserver-xorg</code> and selected the correct resolution to fix it.) Also, the option to enable the restricted Nvidia driver doesn't work, but I haven't gone beyond the normal-human level of effort yet.

(Update: after running a Synaptic update, I could enable the restricted Nvidia driver and turn on Compiz-- no geek-level intervention necessary.)

Overall, I'm delighted with what Dell and the wealthy gentleman from Canonical have done. For me, 2007 is the year of the Linux on the desktop. I offer my sincere congratulations and thanks to the Ubuntu folks at Canonical and Dell.
