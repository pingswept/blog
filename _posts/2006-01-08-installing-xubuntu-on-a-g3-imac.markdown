--- 
wordpress_id: 103
layout: post
title: Installing Xubuntu on a G3 iMac
wordpress_url: http://pingswept.org/2006/01/08/installing-xubuntu-on-a-g3-imac/
---
I work in a school where we have lots of old iMacs that are barely usable under OS 9.2. The newest browser we can get for OS 9 is Netscape 7.0, which crashes a lot (repeatably on Gmail, for example).

[Xubuntu][1] is a derivative of <a href="http://www.ubuntulinux.org/">Ubuntu Linux</a> designed for low-end machines. It uses the <a href="http://www.xfce.org/">XFCE desktop</a>. I've just finished installing Xubuntu on a 400 Mhz iMac. It went reasonably smoothly, and now that I know the few tricks listed below, doing it again should be quite easy.
The steps:

1. Put the Breezy Badger for PowerPC install disk in the CD drive.

2. Reboot.

3. At the first prompt, type "server" and hit return. This will install everything in normal Ubuntu install except the GNOME desktop.

4. Install the Xubuntu desktop and the GNU display manager using apt-get:

> sudo apt-get install xubuntu-desktop gdm

5. To get the graphical interface working, I had to tweak /etc/X11/xorg.conf a little. The first change was to alter the HorizSync and VertRefresh settings. I also switched from the fbdev driver to the ati driver. The snippet below shows the original settings commented out and the new settings added. (Link to <a href="http://pingswept.org/xorgconf-for-xubuntu-on-g3-imac/">full xorg.conf</a>.)
> Section "Device"
> Identifier      "Generic Video Card"
> #       Driver          "fbdev"
> Driver          "ati"
> Option          "UseFBDev"              "true"
> EndSectionSection "Monitor"
> Identifier      "Generic Monitor"
> Option          "DPMS"
> #       HorizSync       28-51
> #       VertRefresh     43-60
> HorizSync       60-60
> VertRefresh     43-117
> EndSection

6. The last tweak was to add a printer to CUPS manually. To enable the web administration for CUPS, I added a root password:
> sudo -s

> passwd

In /etc/cups/cupsd.conf, I changed RunAsUser to No, so that CUPS would run as root, and not switch to run as the user cupsys, as I believe this is what disables the web interface:
> RunAsUser No
Then restart CUPS:
> /etc/init.d/cupsys restart
Here is what ended up in /etc/cups/printers.conf: (Yes, I live in a farmhouse, and I work on Sunday nights)
> # Printer configuration file for CUPS v1.1.23
> # Written by cupsd on Sun 08 Jan 2006 07:34:40 PM EST

> Info Farmhouse
> DeviceURI socket://192.168.1.131
> State Idle
> Accepting Yes
> JobSheets none none
> QuotaPeriod 0
> PageLimit 0
> KLimit 0

Overall, Xubuntu is working really well-- much better than OS 9.2. It's only got 64 MB of RAM, but Firefox runs surprisingly well. I plan on maxing out the memory when I get the chance.

The Xubuntu people have been planning on releasing a CD version of Xubuntu coincident with the release of the Dapper Drake in April. I found the XFCE file manager, xffm, to be a little squirrely, and I couldn't get it to connect to our file server through Samba; maybe that will work in the next release, or maybe I will have figured out how to configure Samba. The Dapper release of Xubuntu will likely be based on XFCE 4.4, which <a href="http://thunar.xfce.org/index.xhtml">will allegedly include the first release of Thunar</a>, XFCE's new file manager.

Hmm. If Thunar is good, I might switch to Xubuntu entirely. So far, XFCE seems like a fast version of GNOME to me, and I spend most of my time in Firefox and a terminal window anyway.

[1]: https://wiki.ubuntu.com/Xubuntu
