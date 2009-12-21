--- 
wordpress_id: 156
layout: post
title: The SL1 is out the door
wordpress_url: http://pingswept.org/2008/01/24/the-sl1-is-out-the-door/
---
We finally released our first product at GreenMountain Engineering. I've been working for various different consulting firms (MindTribe, Ideo, and now GreenMountain) over the past few years, and this is the first time I've been involved in shipping a product that wasn't owned by someone else. I feel proud, and I didn't even do the hard part-- most of the development and testing took place in our San Francisco office.

The product is the called the <a href="http://www.greenmountainengineering.com/greentools">Trac-stat SL1</a>. It's a ridiculously accurate sensor for measuring how closely your solar tracker is aimed at the sun. I think the spec is 0.02 degrees for the more accurate of the two sensors it contains.

<a href='http://pingswept.org/wp-content/uploads/2008/01/sl1_on_tracker.jpg' title='SL1'><img src='http://pingswept.org/wp-content/uploads/2008/01/sl1_on_tracker.jpg' alt='SL1' /></a>

Max and two of his west coast disciples have been testing it at our secret rooftop testing facility in San Francisco for the last few months. (Pretend you don't recognize the lights of the Giants' baseball stadium in the background.) The graph below shows the output of the sensor. This was on a tracker of relatively low precision that we have used for a couple of different concentrating solar projects.

<a href='http://pingswept.org/wp-content/uploads/2008/01/sl1_polar_error.png' title='SL1 error plot'><img src='http://pingswept.org/wp-content/uploads/2008/01/sl1_polar_error.png' alt='SL1 error plot' /></a>

Of the many markets that exist for the SL1, the largest is the group of companies that are trying to build concentrating photovoltaic systems. The key point of leverage behind concentrating solar is that if you can gather the same amount of sun with a drastically reduced amount of solar cell, you can win on cost. An unfortunate side effect is that as your target gets smaller, you need to aim ever more precisely at the sun. This means that to be able to evaluate the performance of your concentrating system, you have to know how well you are pointed at the sun. This alone is a serious research project; there is substantial empirical evidence that building a sensor to track the sun takes lots of work, and that doesn't even get you any actuation. You can buy a pretty good tracker, but you won't know how good unless you have some sort of diagnostic instrument that can measure your error very precisely.

When I worked in the Stanford Robotics Lab after grad school, <a href="http://robotics.stanford.edu/~jks/">a shrewd man</a> told me on one occasion, "Don't make everything a research project." (I think I was proposing writing my own TCP/IP stack or something similarly idiotic that would have taken long enough to preclude completion.) My hope is that the concentrating solar companies will not spend the engineering time it would take them to each build an SL1 equivalent.

And finally, did I mention that it also has a sweet command line interface?

(Perhaps I should note that the opinions listed above do not represent those of my employer. Especially not the unreasoning zeal for command line interfaces.)
