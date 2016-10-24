---
date: 2005/11/19 00:00:00
format: markdown
title: Editing files remotely over SSH using Bluefish
---
Every now and then, I think of a good idea for a software feature, and when I look where I think it should live, it's already there. I was using everyone's favorite closed source command line text editor, pico, to edit an XML file on a remote server, and I was missing syntax highlighting, which makes it easier for me to pick up my markup violations. I thought: there should be a GPL'd text editor that I can run locally that will manage the opening, updating, and closing of a source file on a remote server in the background. I tried Gedit, but no luck. It's designed to be lightweight, which is good for a default editor. Then I tried <a href="http://bluefish.openoffice.nl">Bluefish</a> and hit the jackpot. 

In Bluefish 1.0.1, I used File &gt; Open URL and typed in my URL. The file opened, but when I tried to save, it wouldn't let me. In despair, I selected File &gt; Open, and I was surprised to be prompted for my password on the remote machine. I entered the password, and then I could edit and save without a problem. I'm not sure why I wasn't prompted for the password when I tried to save, but the important point is that all the tedium of text editing in pico just dropped out of life, likely forever.

Time to submit the bug to the Bluefish folks.
