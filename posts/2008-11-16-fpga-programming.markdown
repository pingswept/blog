---
date: 2008-11-16T00:00:00.000Z
format: markdown
title: FPGA programming
---

After a little bit of work and screwing around with installers, I have programmed an FPGA for the first time. I wrote a short bit of Verilog that creates a 4-bit counter in a Xilinx Spartan 3A FPGA. Now, when I feed the FPGA a 50 MHz square wave on a certain pin, it counts the rising edges and outputs the count on 4 digital lines. Of course, it has to start over when it gets to 15.

The oscilloscope screenshot below shows the two highest order bits counting up in binary in response to the input signal.

<a href="/img/fpga_counter.png"><img src="/img/fpga_counter-300x212.png" alt="Counting at 6.25 MHz" title="fpga_counter" width="300" height="212" class="size-medium" /></a>

This may seem like a stupid way to spend your time-- who needs a 4-bit counter? You may be right.

However, the theory is that one skilled enough in Verilog might be able to develop not just a 4-bit counter, but, for example, a microprocessor with a custom co-processor designed for ephemeris calculations (or whatever calculations suit you). In reality, it's more likely that I would buy the Verilog to make the microprocessor and then just write the custom math processor myself.

It may prove a useless skill, but it definitely makes me less worried that some 14-year-old cyborg is going to make me obsolete in the next 45 minutes.
