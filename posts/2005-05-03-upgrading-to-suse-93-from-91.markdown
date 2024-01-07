---
date: 2005-05-03T00:00:00.000Z
format: markdown
title: Upgrading to SuSE 9.3 from 9.1
---

I just upgraded my desktop machine from SuSE Linux 9.1 Pro to 9.3 Pro.<br />
It took a little over an hour, and nothing particularly horrible<br />
happened, so far as I can tell.
I did run into two problems:
1. The Shuttle SS51G that I have uses the Intel 8×0 sound driver.<br />
Since 9.1, the driver has dropped support for the “joystick”<br />
parameter, but /etc/modprobe.d/sound still tried to set it to zero,<br />
which gave me an error about no volume controls being present, as well<br />
as a huge pile of errors in dmesg. A German website had the answer:<br />
http://suse-linux-faq.koehntopp.de/q/q-suse93-snd_intel8×0.html
For those of us who don’t know German, the answer can be summarized<br />
as “delete joystick=0 from /etc/modprobe.d/sound.”
2. The second problem I ran into is that like Red Hat, SuSE is worried<br />
about getting sued by Fraunhofer, a German company that owns several<br />
patents involved in mp3 encoding and decoding (licensed through Thomson<br />
Multimedia in the US). As a result, they do not include software that<br />
decodes mp3s in SuSE 9.3 Pro. However, SuSE does allow you to download<br />
packages from their FTP site that add the ability to decode mp3s. I<br />
don’t know whether they changed their minds after the CDs were<br />
pressed or whether there is some legal difference between me downloading<br />
the files from them directly instead of from a CD that they made.<br />
Unfortunately, I was a coward when I started ripping my CDs a few years<br />
ago, so I didn’t rip them to .ogg, which is similar in quality and<br />
compression to mp3, but not encumbered by patents. On the other hand,<br />
the ipod does not and may never support .ogg. On the third hand, at<br />
least one of the mp3 patents expires in 2015.
SuSE 9.3 is pretty slick. An SVG icon theme is included, which is fun to<br />
play with, even if the icons look like bitmaps once you stop stretching<br />
them. Beagle, the new desktop search program is reasonably functional,<br />
at least at first glance, although I have not figured out how to make it<br />
index cached chats in Chatzilla (possibly because Chatzilla may not<br />
cache chats).
So, with that done, I’m going back to counting down the days until<br />
Firefox 1.1 is released with native SVG support sometime in June. Since<br />
I don’t actually know when it will be released, I’ve decided to<br />
count up instead.
