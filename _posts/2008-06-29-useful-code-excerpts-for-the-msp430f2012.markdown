--- 
wordpress_id: 147
layout: post
title: Useful code excerpts for the MSP430F2012
wordpress_url: http://pingswept.org/2008/06/29/useful-code-excerpts-for-the-msp430f2012/
---
Here are a couple little code excerpts that took me some time to figure out. I'm hoping that Google might help the rest of the world's MSP430F2012 programmers save 5 minutes. (If they all find it, a total savings of 55 minutes!)

The MSP430F2012 defaults to a clock speed of 1 MHz, sourced from an onboard DCO. In order to get the DCO to be accurate, you have to load calibration constants from flash.

<blockquote>BCSCTL1 = CALBC1_1MHZ;          // DCO calibration: set range
DCOCTL = CALDCO_1MHZ;           // DCO calibration: set DCO step and modulation</blockquote>

Then you can initialize the timer to count in increments of 100 ms. 

<blockquote>TACCTL0 = CCIE;         // CCR0 interrupt enabled, compare mode
TACCR0 = 50000;
TACTL = TASSEL_2 + ID_1 + MC_1; // SMCLK as source; divide by 2; up mode
</blockquote>

Anyway, I hope this is useful to someone out there.
