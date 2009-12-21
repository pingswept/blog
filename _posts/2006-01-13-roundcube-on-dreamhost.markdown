--- 
wordpress_id: 104
layout: post
title: Installing Roundcube on Dreamhost
wordpress_url: http://pingswept.org/2006/01/13/roundcube-on-dreamhost/
---
I followed Hookturns' guide to <a href="http://www.hookturns.com/setting-up-roundcube-on-dreamhost/">installing Roundcube on Dreamhost</a> a few days ago, but I used a more recent version (<a href="http://sourceforge.net/project/showfiles.php?group_id=139281&package_id=171500&release_id=378726">roundcubemail-cvs-20051216.tar.gz</a>) and found that it still worked with the following changes:
<ol>
	<li>After Hookturns' Step 4, change config/*.php.dist to *.php</li>
	<li>In Hookturns' Step 6, line 54 is now line 57.</li>
</ol>
I haven't tested my Roundcube installation thoroughly, but I was able to log in and send mail; I didn't see any obvious errors.

Just for reference, in the Dreamhost domain management settings, I had "Run PHP as CGI" selected, but not "PHP Version 5." This may be the default, but I was tempted to use PHP 5; maybe you will be too.
