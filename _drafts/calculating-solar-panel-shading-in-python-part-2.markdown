In a <a href="http://pingswept.org/2009/03/16/calculating-solar-panel-shading-in-python/">previous post</a>, I described the script I wrote to estimate the height of the tallest obstruction using a spherical image.

Problem: im.load() in despherifyImage() in horizon.py is returning None. WTF?

There is a long-standing bug in the Python Imaging Library, which has been fixed in version 1.1.7, which is still in beta at present (May 2009). A patch that fixes this  bug in earlier versions is here: http://mail.python.org/pipermail/image-sig/2008-March/004886.html
Ubuntu Jaunty has PIL version 1.1.6. For that release, the patch should be applied to /usr/share/pyshared/PIL/Image.py near line 1670.
