--- 
wordpress_id: 44
layout: post
title: Hiding the port number on SchoolBell using mod_rewrite
wordpress_url: http://www.betsymattox.com/pingswept/2005/10/10/hiding-the-port-number-on-schoolbell-using-mod_rewrite/
---
I've just set up the Shuttleworth Foundation's slick little calendar server, SchoolBell. It runs on port 7180 by default, but I didn't want to my colleagues (that's what you call everyone else if you work at a school) to have to remember that. Digging around in the README file for a related program, SchoolTool, I found a suggestion that mod_rewrite would help me out.
In the end, this worked on Ubuntu 5.10, Breezy Badger:<br />
<code><br />
<br />
    ServerName calendar.chewonki.org<br />
    RewriteEngine On<br />
    RewriteRule ^/(.*) http://calendar.chewonki.org:7180<br />
</code>
Note that I'm mapping most of our hosts (like "calendar") using our internal DNS server, so all you wandering internet folks can't resolve the URLs above. I also had to enable the mod_rewrite module with the a2enmod command.
We'll see how SchoolBell works. I suspect we'll have 15 excited users, 10 people who think it's a pain in the ass to use computers for calendaring, and everyone else (from the set of all colleagues) won't even know it exists.<br />
<em><br />
Update: I just upgraded Breezy to use SchoolBell 1.2.2 from 1.2.1. The performance difference is shocking. From my little bit of experimenting, it's 5-10 times faster. The slowest task was viewing a whole year at once. It previously took 15-20 seconds to load; now it's 2-3 seconds, and the server is still configuring packages to complete the update, *and* the server sucks. Well done and thank you, Tom Hoffman, Mark Shuttleworth, and co.</em>

