---
format: markdown
date: 2010-08-20T00:00:00Z
title: Dynamic image listing in PHP
categories: code, php
---

I've been working pretty hard on a [top secret project][1] for the last couple of months, so the blog posts have been a little scarce. More details about the top secret project (TSP) shortly, but in the meantime, here's a little PHP script I wrote this morning.

Having switched from Wordpress to Jekyll (a [blog compiler][2], if you will), I needed a way to quickly browse a directory of images on a webserver and copy links to the images for insertion into blog posts. The PHP script below, if saved as index.php into a directory of images you want to browse, will create a page showing 200-pixel wide versions of all the images in rows of 5. You can tweak the image size and row length by changing the 200 and 5 in the script.

It's not kind on bandwidth, as it makes you download all your images, but it's simple. Save the code below as index.php with your images, and then browse to that file in your image directory (something like http://yoursite.com/img/index.php). Assuming your webserver has the PHP engine running, you'll see rows of images. You can then grab links by right-clicking and paste them wherever you like.

## The code ##

$$code(lang=html+php)
<!DOCTYPE html>
<html>
    <head>
        <title>Images</title>
    </head>
    <body>
        <?php
        echo "<table>\n";
        echo "\t\t<tr>\n";
        $i = 0;
        if ($handle = opendir(".")) {
            while (false !== ($file = readdir($handle))) {
                if (strstr($file, "png")||
                    strstr($file, "jpg")||
                    strstr($file, "bmp")||
                    strstr($file, "gif")) {
                    echo "\t\t\t<td><a href='".$file.
"'><img src='".$file."' width='200px' /></a></td>\n";
                    $i++;
                    if ($i%5 == 0) {
                        echo "\t\t</tr>\n\t\t<tr>\n";
                    }
                }
            }
            closedir($handle);
        }
        echo "\t\t</tr>\n";
        echo "\t</table>\n";
        ?>
    </body>
</html>
$$/code

[1]: http://pingswept.org/2010/04/12/designing-embedded-systems-with-web-frameworks/
[2]: http://pingswept.org/2010/01/01/blogging-like-a-so-called-hacker/
