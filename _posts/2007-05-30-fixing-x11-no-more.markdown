---
date: 2007/05/30 00:00:00
format: markdown
title: Fixing X11 no more
---
Last week, after building my own computers to run Linux for about 10 years, I ordered a computer from <a href="http://direct2dell.com/one2one/archive/2007/05/24/15994.aspx">Dell with Ubuntu Linux pre-installed</a>. Don't get me wrong-- I have enjoyed at least 80% of the hacking, crashing X11 repeatedly, trying to disable X11, giving up and using the terminal window at 640 x 480, crashing X11 repeatedly, and so on. In the last 2 or 3 years, Linux has become solid enough that I rarely need to perform tasks akin to surgery. With tested hardware from Dell, instead of hardware randomly selected from different (<a href="http://lwn.net/Articles/57847/">non-Belkin</a>) vendors, I'm betting that **I may not need to edit xorg.conf at all!**

As I prepare to enter the realm of normal people, the realm of adults who buy computers to get work done, who don't know about lolcats or frist psot, HTTP redirection or ARP cache poisoning, SSH or even RSS, it's time for me to pass on what I sincerely hope will become useless tips.

When your GUI goes crazy, the screen starts cycling on and off, or just searching for inputs eternally:

1.  Use Ctrl-Alt-Backspace to stop the X server and drop to a command prompt. Then you can try looking at /etc/X11/xorg.conf to see what's wrong and restart X using the command startx.

2. Enable sshd as soon as you can, so that something goes horribly wrong, you can still ssh into the machine and execute commands.

3. Use Ctrl-Alt-F2 (or higher F-keys) to cycle to additional terminal windows if, as was generally the case, X is screwed up.

Those three tricks have kept me going for tens, or maybe even hundreds, of hours of debugging.

So, maybe I'll need these skills again when the hard times come and production of new computers grinds to a halt, but until then, I'm turning my attention to higher level tasks, like implementing a <a href="http://pysolar.sourceforge.net/">sun-tracking algorithm in Python</a>.
