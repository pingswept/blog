--- 
wordpress_id: 469
layout: post
title: Buildroot on the Gumstix Verdex XL6P
wordpress_url: http://pingswept.org/?p=469
---
Hello internet,

Should you attempt to compile the <a href="http://buildroot.uclibc.org/">Buildroot toolchain</a> so you can build a new filesystem image for your <a href="http://gumstix.com">Gumstix</a> Verdex board, you will find that as of mid-2009, <a href="http://files.gumstix.com">files.gumstix.com</a> no longer hosts several of the files that you will need. However, you can find them elsewhere on the web.

A handy shortcut is to replace the files.gumstix.com URL in gumstix-buildroot/toolchain/getter_script.sh with a different URL where most of the files appear:
<a href="http://www.daimi.au.dk/~spider/gumstix/gumstix-buildroot/dl/">www.daimi.au.dk/~spider/gumstix/gumstix-buildroot/dl/</a>. Thanks are due to the wise and honorable <a href="http://www.daimi.au.dk/~spider/">Martin Mogensen</a> at the University of Aarhus for hosting the files. You'll also need this file in your gumstix-buildroot/dl folder: <a href="http://xmlsoft.org/sources/old/libxml2-sources-2.6.29.tar.gz">xmlsoft.org/sources/old/libxml2-sources-2.6.29.tar.gz</a>

Lastly, you'll want to add to the file gumstix-buildroot/build_arm_nofpu/linux-2.6.21gum/scripts/mod/sumversion.c the line:

<pre lang="c">
#include &lt;limits.h&gt;
</pre>

or you'll get the error "error: ‘PATH_MAX’ undeclared (first use in this function)."

**Fixed version of gumstix-buildroot/toolchain/getter_script.sh:**

<pre lang="bash">
#!/bin/bash
wget -nd --passive-ftp $@ || (
echo Retrying from gumstix alternate site...
index=$#-1
# Copy all params into an array
for (( i=0; $?==0; i++ ));do a[$i]=$1; shift; done
# Chop all but filename from last param and prepend out URL
a[$index]=${a[index]/*\//http:\/\/www.daimi.au.dk/~spider/gumstix/gumstix-buildroot/dl/}
# Now wget that from out server
wget -nd ${a[@]}
)
</pre>

Just a few other notes, since I finally got the Ethernet port working with Gumstix SVN r1642:

**/etc/network/interfaces**

<pre lang="bash">
auto lo
iface lo inet loopback

iface usb0 inet dhcp

auto eth0
iface eth0 inet dhcp
</pre>

**/etc/modules, with correct Ethernet driver selected (smc91x, not smc911x)**

<pre lang="bash">
# MMC support -- comment the next two lines to enable using CF
mmc_block
pxamci

# Compact Flash support -- Must load smc91x or smc911x first!!
smc91x
#smc911x
pcmcia

# Load USB host driver
ohci-hcd
</pre>

**Output of lsmod**

<pre lang="bash">
Module                  Size  Used by
ipv6                  248416  10
af_packet              16872  2
proc_gpio               9412  0
gumstix_bluetooth       1408  0
ohci_hcd               19620  0
usbcore               113340  2 ohci_hcd
pxa2xx_cs               3336  1
pxa2xx_core            10368  1 pxa2xx_cs
pcmcia                 25064  0
pcmcia_core            30576  2 pxa2xx_core,pcmcia
firmware_class          7520  1 pcmcia
smc91x                 16104  0
mii                     4736  1 smc91x
gumstix_smc91x          2816  1 smc91x
pxamci                  6240  0
mmc_block               6568  0
mmc_core               22100  2 pxamci,mmc_block
unix                   22292  18
</pre>

