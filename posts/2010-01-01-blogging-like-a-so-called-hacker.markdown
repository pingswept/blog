---
categories: blogging, compilers, wordpress, ruby
date: 2010-01-01T00:00:00.000Z
format: markdown
title: Blogging like a so-called hacker
---

Back in the first decade of the 21st century, I used Wordpress to write this blog, at first running on a server in my garage, later hosted by Dreamhost. A few months ago, I ran across a [blog post by a Mr. Tom Preston-Werner][1] about [Jekyll][2], which is sort of a blog compiler he wrote in Ruby. This is an unusual idea, the blog compiler, but it appeals to irritating people like me who care about the architecture of the systems they use.

**What's this about a blog compiler?**

Most blog software consists of a database and a pile of webpages with scripts embedded in them. When you request a page from the webserver, the skeleton of the page gets loaded, and the scripts are triggered, which query the database for the relevant text, categories, comments, and whatever else is associated with the page you're trying to read. To me, that seems like a lot of work just to load a blog post. It's not that I don't like databases-- in a situation where I might make the request, "Show me all posts with 'bollocks' in the title published in April of any odd-numbered year," a database would be exactly what is needed. But that's not what's happening here. Mostly, people are making requests like "Show me the post whose title I just clicked on."

For a long time, my thought was, "Eh, who cares? So the database is overkill. Whatever." But as this blog has aged, I've spent more and more time dealing with annoyances. My Wordpress install has been hacked twice, which had a few bad consequences-- my blog spent a few months unknowingly boosting the Google rankings of a casino website, I had to spend some time sorting out the problem, and I had to spend more time backing up the database, which is a little more complicated than just saving a pile of text files. I've had to upgrade Wordpress repeatedly, and manage an array of plugins to do things like generate images for equations.

**What's the alternative?**

The alternative is the blog compiler. I write all my blog posts as plain text, with a little bit of formatting like you might use in an email, like asterisks around a word for emphasis. (This is called the [Markdown][3] format.) When I've finished a post, I run the blog compiler, Jekyll. There are other blog compilers-- [Chronicle][4], [Webby][5]-- but Jekyll what I started with. Jekyll takes my pile of posts and some templates and generates HTML that is approximately identical to what Wordpress previously generated when your web browser requested a page. All of the HTML pages for my ~130 posts are pregenerated in this manner, which takes about 5 seconds on my laptop. Once I'm satisfied with the output, I synchronize the updated pile of HTML pages with the pile on the blog server, and I'm done.

**A few other details**

There are a few other advantages and disadvantages. On the good side, I can now back up my blog with whatever backup tool I want. Also, if I decide that Jekyll is lousy and I want to change my blog around, my posts are in a reasonably future-proof format-- at worst, I can drop all the source files in a single directory on a webserver and call that my blog. I could also switch to Webby or some other blog compiler easily. Also, I now understand my blog layout very well, and the stylesheets are at least 5x shorter, so small tweaks to the layout will be easy, 

Another advantage is speed. My host server only needs to deliver a static page, so there's no waiting around for the database server. While my blog places no noticeable load on the database server, now when someone else bogs down Dreamhost's database server, I won't care. (In the long run, I plan to host this blog on an embedded server on my desk. I'm serving pages at 250 kJ each, that is, 0.0004 page views per second at 100 W for a dedicated server. With an embedded server, I could reduce that by 10x (though in reality, a shared server probably wins by a long shot, as the vast majority of the time, both dedicated servers, embedded or not, would be idle.))

The biggest disadvantage so far has been the time I've spent getting this working. Getting the basics working took just an hour or two (and someone more familiar with Ruby than I am could have done it faster), but importing all the posts from Wordpress took a while, and there are still a few posts with broken images. Also, Jekyll doesn't have a good means for commenting beyond an external service like Disqus, but that's a fundamental problem of the architecture. (Would you want random people like you recompiling your blog?) Last, the system of categories that Jekyll uses isn't so great out of the box-- it uses a hierarchy of directories to represent a series of categories, which makes URLs unnecessarily complex. I'll have to do a little tweaking to fix that. (One other thought: I'm not sure that the RSS feed is working correctly-- I suspect the post dates may be wrong. If you're one of the RSS zealots out there, please comment or email about how the feed is deformed. If it is so horribly deformed that you can't read this, you're off the hook.)

Up next: a fascinating post about our new condensing boiler!

[1]: http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html
[2]: http://wiki.github.com/mojombo/jekyll
[3]: http://daringfireball.net/projects/markdown/syntax
[4]: http://www.steve.org.uk/Software/chronicle/
[5]: http://webby.rubyforge.org/
