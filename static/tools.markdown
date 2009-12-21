---
layout: default
title: Tools 
---

Renaming files in bash:

    for a in *.rtf; do mv “$a” “$(echo “$a” | sed ’s/02142006.rtf$/060221.rtf/’)”; done

A handy command for turning a comma-separated list into a standard .csv file. I used this to convert old Eudora contacts files into a format that Apple’s Mail could import.

    cat input.txt | tr ‘,’ ‘\012′ |sed s/^/,,/ > output.csv

I believe I had to add a line at the top of each file after conversion to tell Mail what it was I was importing:

    ,,Email (other)


