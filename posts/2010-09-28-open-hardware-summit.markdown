---
format: markdown
date: 2010/09/28 00:00:00
title: Thoughts on the 2010 Open Hardware Summit
draft: False
categories: openhardware, embedded, rascal
---
Last Thursday, I went to the Open Hardware Summit in Queens, NY. The Summit had a lot going for it-- people from all of the major open hardware players were there ([Arduino][1], [Adafruit][2], [Sparkfun][3], [Bug Labs][4], and [Beagleboard][5], to name a few), and it took place at the [New York Hall of Science][6], a cool science museum right next to Flushing Meadows with its enormous, awesome [Unisphere][7].

For the past few months, I have been working solo on a [device that I intend to be open hardware][8]. In my circumstances as not just a "small business," but the *smallest possible* business, the crucial question is whether opening my hardware designs to the world will result in someone taking a design and replicating it more cheaply than I can, thereby stealing all my customers. Against that fear, I have the hope that opening my designs will result in people improving them in ways that I can't predict.

This issue came up repeatedly at the summit. Many of the speakers were actually building and selling open hardware. Very few came from VC-funded companies (Bug Labs is the notable exception). Most of them were engineers who had bootstrapped their way from a few small designs they made themselves. They are evidence that my fears are unfounded, particularly in my current state of obscurity.

The explanations varied. Limor Fried of [Adafruit][2] said something like, "People say they will copy you, but it's hard to actually do. . . . Being obscure is worse than being ubiquitous." (A video of her talk is now [available][9].)

In a later talk, Chris Anderson, who runs [DIY Drones][10], mentioned the power of the community. They design small, autonomous aircraft and release all the plans on the internet. Their customers buy the electronics from DIY Drones and then tweak them. Anderson isn't worried about closed competitors: "We think the customers will go with the community." He also pointed out that the community of drone zealots was innovating faster than most private companies; even if you were to copy the hardware today, you'd be obsolete in short order.

After one of the panels, I talked to Nathan Seidle of [Sparkfun][3] for a few minutes. Sparkfun is the internet version of what Radio Shack was in the 70's, when they sold lots of electronic components. They have over 80 employees and around $10M in annual revenue. I asked Nathan why Sparkfun, if run by an evil version of him, wouldn't just collect open hardware designs and start replicating them. His answer was that breaking the trust of the community like that would devastate his sales.

Later in the day, I talked with Chris Gammell of the [Amp Hour][11] for a few minutes. He said that he was worried about what was going to happen when larger distributors enter the open hardware market. This is an interesting point viewed in the light of Nathan Seidle's and Chris Anderson's comments about the trust of the community. When the open hardware community is a small subgroup of a 10-100 thousand people forming a somewhat cohesive culture, losing the support of the community might be catastrophic. But if the electronic hobbyist world grows so that most of Sparkfun's customers don't even know that the hardware they're buying is open, it might be worth it for a giant like Digikey to risk alienating the hardcore open hardware folks. The situation might be like the [libertarian anti-Obamacare editorial][12] published by the CEO of Whole Foods in the Wall Street Journal last year-- hardcore liberals started [boycotting Whole Foods][13], but the majority of their customers didn't care, because *have you tried their almond cookies?*

For me, as a new entrant to the market, I have no worries about a large corporation stealing my ideas-- risking the $100,000 it would take to beat me on volume on the hope that this solitary engineer has come up with a winning product would be colossal folly. I do think that the Rascal will be a great product, but it's definitely not there yet, and it will take a community of users to get it there.

## Footnote: mbed.org ##

One other interesting note-- during lunch, I met Simon Ford and Dan Ros of [mbed.org][14], a small group within ARM that is making development tools for ARM processors. The Mbed is not fully open hardware, though they do distribute schematics of the system. Simon said it was because he wanted to be sure they were built right.

The Mbed is an interesting board. It actually has two microcontrollers on it. The main processor, on top, is an LPC1768 running at 96 MHz. There is a second processor running at 12 MHz on the underside of the board that acts as the programmer for the first processor. You compile your code on their website and then transmit your programs to this supervisory processor via USB. It puts the code on the second processor via JTAG. The advantage of this is that the main processor behaves exactly as it will in a final design. You can design a device using the mbed, and when you're done, you can buy the same LPC1768 processor and replicate what you've got, minus the second processor, which is no longer necessary. It's an elegant architecture.

[1]: http://arduino.cc
[2]: http://adafruit.com
[3]: http://sparkfun.com
[4]: http://buglabs.net
[5]: http://beagleboard.org
[6]: http://nysci.org/
[7]: http://en.wikipedia.org/wiki/Unisphere
[8]: http://rascalmicro.com
[9]: http://www.adafruit.com/blog/2010/09/25/open-source-hardware-summit-keynote-limor-ladyada-fried/
[10]: http://diydrones.com/
[11]: http://theamphour.com
[12]: http://online.wsj.com/article/SB10001424052970204251404574342170072865070.html
[13]: http://www.facebook.com/group.php?gid=119099537379
[14]: http://mbed.org