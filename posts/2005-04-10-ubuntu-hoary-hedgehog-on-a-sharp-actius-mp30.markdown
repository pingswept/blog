---
date: 2005-04-10T00:00:00.000Z
format: markdown
title: Ubuntu Hoary Hedgehog on a Sharp Actius MP30
---

I just installed the default Ubuntu "Hoary Hedgehog" release on my Sharp Actius MP30 laptop. The results were about the same as with the preview release-- still need to add a kernel option to get the trackpad working, and I still haven't managed to get the built-in wireless working.
I still have some hope: <a href="http://www.cameltail.com/projects/sharp/">some guy named Carl at Cameltail</a> has managed to get the wireless working under Slackware 10.0.
Some details about how to add the kernel boot option in GRUB:

Open Applications > System Tools > Terminal

    sudo -s

Type in your password.

    pico /boot/grub/menu.lst

Add i8042.nomux to the nonaltoptions line so that it reads:

    nonaltoptions=quiet splash i8042.nomux

Save the file and exit pico.

    update-grub

Restart your laptop. If you hit ESC as it's booting, you will be able to check the GRUB kernel options to see if what you did worked.
