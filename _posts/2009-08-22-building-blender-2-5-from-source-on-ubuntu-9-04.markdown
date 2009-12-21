--- 
wordpress_id: 530
layout: post
title: Building Blender 2.5 from source on Ubuntu 9.04
wordpress_url: http://pingswept.org/?p=530
---
I recently tried building an early release of <a href="http://www.blender.org/development/current-projects/blender-25-project/">Blender 2.5</a> from source on Ubuntu Linux 9.04 (the so-called 'Jaunty Jackalope'). So that the world might benefit from my tribulations, I thought I'd record the details here.

The 2.5 build process is standardized against Python 3.1, which isn't in the Ubuntu repositories yet, so you have to build that from source. Download the 3.1.1 tarball from python.org and build it like this:

{% highlight bash %}
wget http://python.org/ftp/python/3.1.1/Python-3.1.1.tgz
tar xzvf Python-3.1.1.tgz
cd Python-3.1.1
./configure
make
sudo make install
{% endhighlight %}

You also need a big pile of libraries and build tools, so install those using apt-get like this:
{% highlight bash %}
sudo apt-get install subversion openexr libopenexr-dev build-essential libjpeg-dev libpng12-dev libopenal-dev libalut-dev libsdl-dev libfreetype6-dev libtiff4-dev python-dev gettext libxi-dev yasm libsamplerate0-dev
{% endhighlight %}

Then, you're ready to check out the latest source and build Blender. (I'm sure you don't actually need most of the lib directory in the second command, but I don't know which parts are superfluous.)
{% highlight bash %}svn checkout https://svn.blender.org/svnroot/bf-blender/branches/blender2.5/blender/ /home/brandon/blender2.5{% endhighlight %}

{% highlight bash %}svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/ /home/brandon/blender2.5/lib{% endhighlight %}

A few configuration changes are necessary to make the build work with the stock Ubuntu setup. In blender2.5/config/linux2-config.py, change
{% highlight bash %}BF_PYTHON = '/usr'{% endhighlight %}
to
{% highlight bash %}BF_PYTHON = '/usr/local'{% endhighlight %}

and in the same file, disable FFMPEG support
{% highlight bash %}WITH_BF_FFMPEG = True  # -DWITH_FFMPEG{% endhighlight %}
to
{% highlight bash %}WITH_BF_FFMPEG = False  # -DWITH_FFMPEG{% endhighlight %}

Create a user config file in your blender2.5 directory like this:
{% highlight bash %}
echo "BF_OPENAL_LIB = 'openal alut'" &gt;&gt; user-config.py
{% endhighlight %}

Then, the final build step can be executed like this:
{% highlight bash %}
python ./scons/scons.py
{% endhighlight %}

The build process will create two folders in the same folder as your blender2.5 folder: <em>build</em> and <em>install</em>. The executable is located at <em>install/linux2/blender</em>. If your menus are missing when you run Blender, perhaps it is because you have rushed ahead and executed <em>build/linux2/bin/blender</em>, which is not what you want.

Victory is yours!

<a href="http://pingswept.org/wp-content/uploads/2009/08/blender-2.5.png"><img class="size-full wp-image-541 " title="Blender-2.5 screenshot" src="http://pingswept.org/wp-content/uploads/2009/08/blender-2.5.png" alt="Screenshot of Blender 2.5" width="425" /></a>
