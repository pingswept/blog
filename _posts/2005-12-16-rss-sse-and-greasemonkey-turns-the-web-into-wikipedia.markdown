--- 
wordpress_id: 24
layout: post
title: RSS + SSE and Greasemonkey turns the web into Wikipedia
wordpress_url: http://www.betsymattox.com/pingswept/2005/12/16/rss-sse-and-greasemonkey-turns-the-web-into-wikipedia/
---
I've been thinking about the SSE extension and how it might be combined with Greasemonkey to fix a lot of shyste. Here's an example: you're reading a webpage, and you see a spelling error. You highlight the word, right click on some icon in the status bar, and select "spellcheck" or something like that. The point is that somehow, a Greasemonkey script records your correction, and whenever you visit that URL, it applies your correction.
Then, on a periodic basis, your browser contacts a website (THIS IS WHERE RAILS WOULD BE USED!) and updates an RSS + SSE feed of your corrections to the web (er, "the living web"). These feeds get aggregated, so as I'm browsing, I have a cache of Greasemonkey scripts shared and maintained in concert with people that I trust through RSS + SSE. The spelling example is minor-- it could be expanded to be website commentary, adblocking (ooh! controversial!), or whatever. In fact, it has the potential to make the entire web as unreliable as Wikipedia!
I suspect that there could be scalability problems with this idea. There could also be stupidity problems.

