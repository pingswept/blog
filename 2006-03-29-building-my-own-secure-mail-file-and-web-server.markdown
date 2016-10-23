---
date: 2006/03/29 00:00:00
format: markdown
title: Building my own secure mail, file, and web server
---
After multiple complaints from an <a href="http://goelzer.com">irritating associate</a> of mine, I am building a secure server for my various secure computing needs. The complaints have focused on the fact that I have a Gmail account. While I generally agree that allowing a company to host all of my personal email, where it can be indexed, queried, and sold to various individuals and companies around the world, is a bad idea, so far, the worst side effect has been all the Google ads for Dallas real estate. Like I think Kennedy's really dead!

All the same, I've been thinking it would be fun to buy a rackmount server, install OpenBSD, apache, qmail, roundcube, and sshd. I'll install my public key in sshd so my remote logins and file transfers would be encrypted. I'll generate an SSL certificate to encrypt the roundcube exchanges. The machine will be colocated at the InterNAP datacenter in Somerville, if I get a reasonably good deal on rack space. Then I just have to guard against physical intrusions into the server and convince everyone who emails me to use GPG, and maybe I'll finally drop back off the CIA's radar.

Maybe an encrypted filesystem will be necessary as well. I realize that the US government could just subpoena the bejesus out of me, but at least then I'd know what they were getting. (In reality, this will never occur; I'm just preparing for the day when I actually have something useful to encrypt.)
Comments about the security holes I'm missing are welcome from those who are not the irritating associate.
