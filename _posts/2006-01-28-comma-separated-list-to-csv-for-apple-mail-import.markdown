--- 
wordpress_id: 112
layout: post
title: Comma separated list to .csv for Apple Mail import
wordpress_url: http://pingswept.org/2006/01/28/comma-separated-list-to-csv-for-apple-mail-import/
---
A handy command for turning a comma-separated list into a standard .csv file. I used this to convert old Eudora contacts files into a format that Apple's Mail could import.

cat input.txt | tr ',' '\012' |sed s/^/,,/ > output.csv

I believe I had to add a line at the top of each file after conversion to tell Mail what it was I was importing:

First,Last,Email (other)
