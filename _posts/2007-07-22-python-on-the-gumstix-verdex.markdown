--- 
wordpress_id: 144
layout: post
title: Python on the Gumstix Verdex
wordpress_url: http://pingswept.org/2007/07/22/python-on-the-gumstix-verdex/
---
Being both a <a href="http://en.wikipedia.org/wiki/Python_(programming_language)">Python</a> zealot and an embedded systems zealot, I've been looking for an embedded system that I can program in Python. Most of the embedded code <a href="http://greenmountainengineering.com">I write professionally</a> I write in C. Having learned Python a few years ago, I'm finding C increasingly painful, approximately in proportion to my facility with Python.

Thus far, it seems that the <a href="http://gumstix.com">Gumstix</a> <a href="http://gumstix.com/store/catalog/product_info.php?cPath=27&products_id=178">Verdex</a> may be the answer I've been seeking. The Verdex is an embedded Linux board, about 1 inch by 3 inches, based around Marvell's (previously, Intel's) <a href="http://en.wikipedia.org/wiki/Xscale">XScale</a> PXA270, common in PDAs and cellphones. It uses around 1 W of power in its quiescent state (not suspended, but not at full processor load either).

I was able to <a href="http://docwiki.gumstix.org/Buildroot">compile a new binary image</a> including the Linux kernel, various utilities, and Python 2.4.2 and <a href="http://docwiki.gumstix.org/Replacing_the_filesystem_image">upload it to the Verdex</a> using the Gumstix's <a href="http://gumstix.com/store/catalog/product_info.php?products_id=185">console-vx</a> serial interface board. (I seem to have hosed the ethernet interface at the same time, but I'll worry about that later.)

The ultimate goal (well, for now) was to test on an embedded processor <a href="http://pysolar.sf.net">Pysolar, the Python sun-tracking code I've been writing</a>. The Verdex I have, the XL6P, runs at 600 MHz. The Pysolar test suite executed in around 1.2 seconds. On <a href="http://pingswept.org/2007/06/03/finally-booting-pre-installed-linux-on-an-oem-pc/">my desktop Linux machine</a>, the same test suite executes in 0.012 s. The fact that the times vary by a factor of precisely 100 makes me a little suspicious, but it doesn't seem impossible that a desktop could beat an embedded computer by 100x.
