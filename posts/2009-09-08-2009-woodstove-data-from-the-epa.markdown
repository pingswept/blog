---
categories: energy, engineering
date: 2009-09-08T00:00:00.000Z
format: markdown
title: 2009 woodstove data from the EPA
---

The EPA regulates woodstove emissions in the US. Each year, they publish a list of the roughly 700 types of woodstoves sold in the US that includes an emissions metric (grams of particulate per hour) and a range of output power (BTU/h)  for each stove.

For reasons that I may never understand, the EPA releases <a href="http://www.epa.gov/oecaerth/resources/publications/monitoring/caa/woodstoves/certifiedwood.pdf">this data as a PDF</a>.

Datacentric citizen that I am, I have converted the data to spreadsheet format, so you can sort it by emissions rate, if that's your kind of thing. I also removed some of the duplicate data. Some stoves were listed by two manufacturers, where one is a subsidiary of the other, but in some cases, one company or the other no longer exists. Such is the case with CFM Corporation, the bankrupt owner of Vermont Castings and Majestic Products, so I deleted those rows. (It appears that both brands, as well as several others, are now manufactured by a new parent company, Monessen Hearth Systems.)

By the way, as a quick summary of the data: **if you want a clean stove, buy one from <a href="http://www.vermontcastings.com">Vermont Castings</a>**. They make 6 of the 10 cleanest stoves, 5 of which emit less than 1 g/h of particulates. For comparison, fireplaces produce around 30-60 g/h.

Here are the files:

* [Gnumeric spreadsheet][1]
* [OpenOffice spreadsheet][2]

And, for those of you using the only operating system where virus scanners are normal: [Excel spreadsheet][3]

I should also say that particulate emissions are not the only emissions to think about with a woodstove. <a href="http://www.eia.doe.gov/oiaf/1605/coefficients.html">According to the Energy Information Administration</a> and <a href="http://www.google.com/search?q=195+pounds+per+1000000+BTU+in+g+per+megajoule">Google's sweet unit conversion feature</a>, wood releases around 85 g of CO<sub>2</sub> per MJ of heat. That's better than coal, which is up around 90-100 g/MJ, but worse than natural gas, at 50 g/MJ. Electric heat is the worst, at 125 g/MJ, assuming the electricity is coming from a ~40% efficient natural gas power plant like the Exelon Power plant in Everett that supplies Somerville's peak loads.

Of course, you have to heat your house somehow (or move to the tropics). Trees will grow back soon, while coal and natural gas take a little longer.

[1]: http://pingswept.org/files/Woodstoves_EPA_2009.gnumeric
[2]: http://pingswept.org/files/Woodstoves_EPA_2009.ods
[3]: http://pingswept.org/files/Woodstoves_EPA_2009.xls
