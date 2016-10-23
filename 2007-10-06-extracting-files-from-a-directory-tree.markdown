---
date: 2007/10/06 00:00:00
format: markdown
title: Extracting files from a directory tree
---
Mr. <a href="http://fiveislandsorchard.wordpress.com/">Ben Polito</a> has recently beating his drum to the tune that I am a repressed **mechanical** engineer who needs to release his inner **software** engineer.

Normally, I am too busy with preparations for the arrival of the Hard Times to spend time busting the myths spread by <a href="http://fiveislandsorchard.wordpress.com/2007/09/30/midnight-on-the-water/">a sailor in the dark</a>, but a recent problem I ran into at work gave me pause. The first version of our corporate wiki, a tweaked version of mediawiki, left a hierarchy of a few hundred directories sprinkled with around 1600 files. These files were attachments to the old wiki, and while most of them were transferred to the new wiki, some were not.

I thought to myself, "Ah! I bet I could write a little Python function that recursed through the directories, copying out the files and calling itself for each subsequent subdirectory!" This was Friday night around 10, after a day spent writing PLC code for work. It was at this moment that I thought, "Perhaps Mr. Polito has a point."

To that end, I present <a href="http://pingswept.org/pylitopy/">Pylito</a>.
