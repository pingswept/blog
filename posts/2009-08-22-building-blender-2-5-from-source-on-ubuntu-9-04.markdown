---
categories: software
date: 2009-08-22T00:00:00.000Z
format: markdown
title: Building Blender 2.5 from source on Ubuntu 9.04
---

I recently tried building an early release of <a href="http://www.blender.org/development/current-projects/blender-25-project/">Blender 2.5</a> from source on Ubuntu Linux 9.04 (the so-called 'Jaunty Jackalope'). So that the world might benefit from my tribulations, I thought I'd record the details here.

The 2.5 build process is standardized against Python 3.1, which isn't in the Ubuntu repositories yet, so you have to build that from source. Download the 3.1.1 tarball from python.org and build it like this:

<pre class="brush: bash">
wget http://python.org/ftp/python/3.1.1/Python-3.1.1.tgz
tar xzvf Python-3.1.1.tgz
cd Python-3.1.1
./configure
make
sudo make install
</pre>

You also need a big pile of libraries and build tools, so install those using apt-get like this:

<pre class="brush: bash">
sudo apt-get install subversion openexr libopenexr-dev build-essential libjpeg-dev libpng12-dev libopenal-dev libalut-dev libsdl-dev libfreetype6-dev libtiff4-dev python-dev gettext libxi-dev yasm libsamplerate0-dev
</pre>

Then, you're ready to check out the latest source and build Blender. (I'm sure you don't actually need most of the lib directory in the second command, but I don't know which parts are superfluous.)
<pre class="brush: bash">
svn checkout https://svn.blender.org/svnroot/bf-blender/branches/blender2.5/blender/ /home/brandon/blender2.5
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/ /home/brandon/blender2.5/lib
</pre>

A few configuration changes are necessary to make the build work with the stock Ubuntu setup. In blender2.5/config/linux2-config.py, change
<pre class="brush: bash">
BF_PYTHON = '/usr'
</pre>
to
<pre class="brush: bash">
BF_PYTHON = '/usr/local'
</pre>

and in the same file, disable FFMPEG support
<pre class="brush: bash">
WITH_BF_FFMPEG = True  # -DWITH_FFMPEG
</pre>
to
<pre class="brush: bash">
WITH_BF_FFMPEG = False  # -DWITH_FFMPEG
</pre>

Create a user config file in your blender2.5 directory like this:
<pre class="brush: bash">
echo "BF_OPENAL_LIB = 'openal alut'" &gt;&gt; user-config.py
</pre>

Then, the final build step can be executed like this:
<pre class="brush: bash">
python ./scons/scons.py
</pre>

The build process will create two folders in the same folder as your blender2.5 folder: *build* and *install*. The executable is located at *install/linux2/blender*. If your menus are missing when you run Blender, perhaps it is because you have rushed ahead and executed *build/linux2/bin/blender*, which is not what you want.

Victory is yours!

<a href="http://pingswept.org/img/blender-2.5.png"><img src="http://pingswept.org/img/blender-2.5.png" alt="Screenshot of Blender 2.5" width="425" /></a>
