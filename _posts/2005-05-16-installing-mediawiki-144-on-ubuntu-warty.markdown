---
date: 2005/05/16 00:00:00
format: markdown
title: Installing Mediawiki-1.4.4 on Ubuntu Warty
---
I installed Mediawiki, the software that runs Wikipedia, on an Ubuntu
Warty machine yesterday. I issued an sudo -s command at the start so
that I didn’t have to type sudo repeatedly.

To get access to all the different package repositories, I uncommented
the warty universe lines in /etc/apt/sources.list and added one line so
that I had:
<code>
deb http://archive.ubuntu.com/ubuntu/ warty main restricted
deb http://archive.ubuntu.com/ubuntu/ warty universe
deb-src http://archive.ubuntu.com/ubuntu/ warty universe
deb ftp://ftp.debian.org/debian sarge main contrib non-free #
</code>

Then I installed a load of software:
<code>
apt-get install apache2-mpm-prefork apache2-prefork-dev
libapache2-mod-php4 php4-dev php4-mysql php4-pear
</code>

Untar Mediawiki in the default Apache directory:
<code>
cd /var/www
tar xzvf mediawiki-1.4.4.tar.gz
</code>

Ubuntu has a mechanism for Apache configuration that I don’t
understand. I used the commands below as a quick hack to relocate
Mediawiki so that Apache will find it:
<code>
mv apache2-default/ apache2-default_orig/
mv mediawiki-1.4.4/ apache2-default
</code>

Set the MySQL root password:
<code>
mysqladmin -u root password 'password'
</code>

I realized that I don’t really know how to use mysqladmin, so after
a few weak attempts, I figured PHPMyAdmin was a better solution.
<code>
apt-get install phpmyadmin
</code>

I used PHPMyAdmin, which showed up at http:///phpmyadmin. At that
address, I was able to log in as “root” with my MySQL root
password, set above.

Then the standard steps of the Mediawiki installation:
<code>
chmod a+w config/
mv LocalSettings.php ..
chmod ug-w config/
</code>
The wiki I am setting up needs to be able to display equations, which
requires the texvc extension to Mediawiki. Texvc parses Tex markup and
feeds it to ImageMagick, which generates .png files of the equations. I
needed gcc to compile the code.
<code>
apt-get install gcc ocaml imagemagick gs cjk-latex tetex-extra
php4-imagick
</code>
Compile the code:
<code>
cd /var/www/apache2-default/math/
make
</code>
Wikimedia’s site on <a href="http://meta.wikimedia.org/wiki/Running_MediaWiki_on_Debian_GNU/Linux">running Mediawiki on Debian</a> was quite useful.
