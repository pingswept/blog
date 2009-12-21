--- 
wordpress_id: 107
layout: post
title: Off to BarCampNYC to talk about Wikr
wordpress_url: http://pingswept.org/2006/01/13/off-to-barcampnyc-to-talk-about-wikr/
---
Stage 2 of my trip to New York City for BarCampNYC begins tomorrow morning around 7:30. Stage 1 was last night when I drove down to Boston from Wiscasset, Maine, <a href="http://chewonki.org">where I work</a>. I spent the day debugging a DNS problem and preparing for the <a href="http://pingswept.org/wikr">Wikr</a> presentation at BarCamp.

Wikr is a Firefox extension that Mike Goelzer and I have been working on. (Yes, it's a stupid name, but at least it's short.) The idea is to establish **a means for synchronizing web improvements across trusted peer groups**.

The "means," in this case, is Mike's Rails server and an RSS + SSE feed.

"Web improvements" is a contentious phrase-- what improves the web for me doesn't necessarily improve it for everyone else. The closest implementation I've seen of this idea is Greasemonkey scripts-- scripts that allow the user to filter, augment, combine, and tweak web pages into something they prefer to the original. What Wikr is trying to do is to allow people to subscribe feeds of improvements from people or organizations that they trust. Myself, I'd love to have a feed of Google maps links embedded in any news story I read, so I can see where places mentioned are, like this imaginary weather report: "It was 10 degrees below zero in <a href="http://maps.google.com/maps?f=q&sll=37.0625,-95.677068&sspn=45.8712,63.28125&hl=en&btnG=Search&ll=58.10691,-68.394699&spn=0.120261,0.247192&t=k">Kuujjuaq, Nunavik</a> today." Someone else might want a feed of spelling corrections, or a feed of bloggers' posts about political articles they read.

"Trusted peer groups" means any group of people who trust each other and have the organization to get a feed together. Obviously, a lot of this depends on how easy it is to generate and host feeds. The Platypus extension for Firefox is a GUI for creating Greasemonkey scripts-- in the end, Wikr might turn into a repackaged combination of Platypus and Greasemonkey with a little Javascript gluing it in between.

The authentication model is still half-baked. Each group will need to decide who is allowed read-only access to the feed of improvements and who is allowed bidirectional synchronization (the SSE in RSS + SSE). We haven't developed anything beyond that principle yet.

As a demonstration for BarCampNYC, we have Mike's server set up with an RSS + SSE feed. We also have an extension that synchronizes the pool of Greasemonkey scripts on Mike's server to a local cache of scripts used by Firefox.

We're also hoping to have a website and mailing list set up by the time BarCampNYC ends, so interested parties can follow our progress or join the fun.
