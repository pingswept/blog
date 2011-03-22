---
date: 2006/01/28 00:00:00
format: markdown
title: Comma separated list to .csv for Apple Mail import
---
A handy command for turning a comma-separated list into a standard .csv file. I used this to convert old Eudora contacts files into a format that Apple's Mail could import.

cat input.txt | tr ',' '\012' |sed s/^/,,/ > output.csv

I believe I had to add a line at the top of each file after conversion to tell Mail what it was I was importing:

First,Last,Email (other)
