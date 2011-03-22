---
date: 2007/07/08 00:00:00
format: markdown
title: OOXML is not fully documented by ECMA 376
excerpt: No explanation of "the behavior of Microsoft Word 95" is given. How might a competing vendor determine all the rules that Word 95 uses for character spacing? Type all possible sequences of characters in all fonts on a computer borrowed from the Computer History Museum, and then analyze the results?
---
Comment sent to Massachusetts about their bone-headed inclusion of ECMA 376 (OOXML) in their latest draft of the Enterprise Technical Reference Model:

<blockquote>Hello,

I'm a long-term resident of Massachusetts; I run an engineering firm in Waltham. I have no affiliation with any company that produces any document format.

I have two objections to the inclusion of Microsoft's ECMA 376 in ETRM 4.0:

1. As a citizen, I don't want to buy a certain vendor's software to read government documents.

2. As a technical professional in a competitive market, I don't want to pay the overhead of upgrading the de facto standard Microsoft Office every 3 years for no good reason.

ITD had the right idea with its choice of ISO 26300 (ODF) as a single, open standard for government documents.

In the engineering work that I do, we need to maintain two sets of tools--  one in metric units and one in English units. The choice of two standards for the same function provides nothing but inefficiency. ITD should not introduce similar inefficiency into government document formats.

It is predictable that no other vendors will implement ECMA 376 well enough to guarantee document fidelity across platforms. To see why, consider this excerpt from page 1379 of ECMA 376:

"If this compatibility setting is turned on:
   &lt;w:compat&gt;
       &lt;w:autoSpaceLikeWord95 /&gt;
   &lt;/w:compat&gt;
Then applications should mimic the behavior of Microsoft Word 95 when determining the space between those characters, as needed."

No explanation of "the behavior of Microsoft Word 95" is given. How might a competing vendor determine all the rules that Word 95 uses for character spacing? Type all possible sequences of characters in all fonts on a computer borrowed from the Computer History Museum, and then analyze the results?

This sort of incomplete specification, found throughout ECMA 376, will mean that nobody other than Microsoft will be able to implement ECMA 376 completely. While ECMA 376 is nominally open, in my judgment, it is so incomplete as to be effectively proprietary. In the language of ITD, ECMA 376 is publicly available, but not fully documented. The predictable result of ECMA 376 adoption will be a series of buggy import functions in competing software, while Microsoft Office remains the government-supported standard.

The same cannot be said for ODF. Many competing products that implement ODF already exist; I've been using them for all my personal documents for several years. I understand the objection that the switch to ODF from Microsoft's closed formats will be painful, but it's a better choice than upgrading to the next Microsoft format every three years for eternity.

I request that Massachusetts return to its innovative idea of choosing a single, open standard for government documents; I believe that ODF is the best choice for that standard.

Thanks for your consideration,
Brandon Stafford
Cambridge, MA
</blockquote>

