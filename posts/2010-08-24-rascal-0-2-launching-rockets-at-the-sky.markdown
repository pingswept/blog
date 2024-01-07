---
title: "Rascal 0.2: launching rockets at the sky"
slug: rascal-0-2-launching-rockets-at-the-sky
author: Brandon Stafford
lastmod: 2014-03-01T15:44:00.000Z
date: 2010-08-24T20:46:00.000Z
source: rascalmicro.com
---
The second revision of the Rascal arrived in mid-August. After a little mucking about with a JTAG pod, it can execute code.

<img class="span14" src="/img/950px-rascal-0.2.jpg">

A lot of my friends have been asking me whether the Rascal is ready for action now. The hardware is in good shape-- it's not flawless, but it's somewhere above 95% operational. The remaining work is the software, which seems easy, maybe because it's made of electrons. It's not actually easy, so I thought I should explain some of the details.

Making the Rascal load an operating system like Linux or Android is more complicated than you might expect. (The good news is that I've already done the hard part for you; once the code is configured correctly, it boots automatically when the Rascal is turned on.)

When I got the first Rascals back from the assembly house, all of the memory was blank, except for a small chunk of code that the chip manufacturer, Atmel, burns into every chip. I added two other pieces of software, called bootloaders, to help start up an operating system.

## Three levels of bootloaders ##

The first chunk of code, burned into memory by Atmel, is called the ROM Boot Program. It switches the processor from using a low speed oscillator to using a high speed crystal, which drives a frequency-multiplying circuit called a phase-locked loop. This kind of hardware initialization is needed no matter what you're doing with the chip, which is why Atmel includes the code. (Strictly speaking, you can bypass it in some chips, or if you have a certain kind of memory attached to your chip.)

When the ROM Boot Program ends, it starts the next program, which is called AT91Bootstrap. This program, which works with all processors in the AT91 series, configures the processor to talk to all of the peripheral chips on the Rascal PCB. Atmel made the first version of AT91Bootstrap; I edited the source code slightly to fit the wiring of the chips on the Rascal circuit board and recompiled it to make a new program just for the Rascal.

AT91Bootstrap has a few jobs, but most importantly, it configures the memory bus, which allows the use of external RAM and Flash chips. (Rascal 0.1 had a problem with the memory bus, so this was as far as those boards could get.) The last job of AT91Bootstrap is to copy the third bootloader, U-boot, into RAM from Flash.

## Booting the Linux kernel ##

U-boot is somewhere between a bootloader and a minimal operating system. It can load files into memory, tell you the status of different hardware components, and download new code from the internet.

Here's an example of using U-boot to query the Rascal's Ethernet controller.

```language-bash
    U-Boot> mii info
    PHY 0x00: OUI = 0x0885, Model = 0x11, Rev = 0x02,  10baseT, HDX
    U-Boot> mii dump            
    0.     (3100)                 -- PHY control register --
      (8000:0000) 0.15    =     0    reset
      (4000:0000) 0.14    =     0    loopback
      (2040:2000) 0. 6,13 =   b01    speed selection = 100 Mbps
      (1000:1000) 0.12    =     1    A/N enable
      (0800:0000) 0.11    =     0    power-down
      (0400:0000) 0.10    =     0    isolate
      (0200:0000) 0. 9    =     0    restart A/N
      (0100:0100) 0. 8    =     1    duplex = full
      (0080:0000) 0. 7    =     0    collision test enable
      (003f:0000) 0. 5- 0 =     0    (reserved)
```

In actual operation, U-boot doesn't do very much other than load Linux from Flash into RAM, and then start executing it. In the long run, we might change the Rascal so that AT91Bootstrap loads and boots Linux directly, but for development, having the flexibility and diagnostic capabilities of U-boot is great.

There are still more layers of user software to build on top of the operating system, but I hope this clears up some of what I've been messing around with the past couple of weeks.
