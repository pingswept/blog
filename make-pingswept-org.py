#!/usr/bin/env python3

import codecs, frontmatter, markdown, os, shutil
import datetime as dt
from markdown.extensions import Extension

POSTS_PER_PAGE = 4

header = open('header.html', 'r').read()
footer = open('footer.html', 'r').read()

postlist = os.listdir('posts')
pagelist = os.listdir('pages')

def isPage(filename):
    if ".markdown" in filename:
        return True
    else:
        return False

def writePage(basename, infile, outfile):
    #print('Processing {0} into {1}'.format(infile.name, outfile.name))
    html = markdown.markdown(infile.read(), extras=['metadata']).encode('utf8')
    outfile.write(header)
    outfile.write('<h2>{0}</h2>'.format(' '.join(basename.split('-')).capitalize()))
    outfile.write(html.decode('utf-8'))
    finishPage(outfile)

def writePost(basename, infile, outfile):
    #print('Processing {0} into {1}'.format(infile.name, outfile.name))
    html = markdown.markdown(infile.read(), extras=['metadata']).encode('utf8')
    outfile.write(header)
    outfile.write('<h2>{0}</h2>'.format(' '.join(basename.split('-')).capitalize()))
    outfile.write(html.decode('utf-8'))
    finishPage(outfile)

def writeSidebar():
    with open('sidebar.html', 'w') as sb:
        sb.write(
'''
<input type="checkbox" id="toggleSidebar" class="toggle-checkbox">
<label for="toggleSidebar" id="hamburger">☰</label>

<aside id="sidebar">  
    Static pages
    <ul>
''')
        for filename in sorted(filter(isPage, pagelist)):
            (basename, ext) = filename.split('.')
            sb.write('      <li><a href="http://pingswept.org/{0}.html">{1}</a></li>\n'.format(basename, basename.replace('-', ' ').capitalize()))
        sb.write(
'''     </ul> 
</aside> <!-- end sidebar -->
''')
    sb.close()

def writeMultiPostPage(index, filenames):
    if(index == 0):
        filepath = 'output/index.html'
    else:
        filepath = 'output/page/{0}.html'.format(index)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    outfile = open(filepath, 'w')
    outfile.write(header)
    for post in reversed(filenames):
        with open('posts/' + post, 'r') as infile:
            print('Adding {0} to multipost page'.format(infile.name))
            p = frontmatter.load(infile) # split off the YAML header
            #date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
            #d = dt.datetime.strptime(p['date'], date_format)
            # d = dt.datetime.strptime(p['date'].split(' ')[0], "%Y/%m/%d").strftime("%B %d, %Y")
            outfile.write('<h4>{0}</h4>'.format(p['date'].strftime("%B %d, %Y")))
            html = markdown.markdown(p.content, extras=['metadata']).encode('utf8')
            outfile.write('<article><h2>{0}</h2>'.format(p['title']))
            outfile.write(html.decode('utf-8'))
            outfile.write('</article>')
    if any('1997' in n for n in filenames): # dumb hack to omit "older posts" from oldest page
        pass
    else:
        outfile.write('<a href="/page/{0}.html">older posts</a>'.format(index + 1))
    if(index > 0):
        if(index == 1):
            outfile.write('<a href="/index.html">newer posts</a>')
        else:
            outfile.write('<a href="/page/{0}.html">newer posts</a>'.format(index - 1))
    finishPage(outfile)

def writeMultiposts():
    posts = sorted(filter(isPage, postlist))
    chunks = reversed([posts[x:x+POSTS_PER_PAGE] for x in range(0, len(posts), POSTS_PER_PAGE)])
    for idx, chunk in enumerate(chunks):
        writeMultiPostPage(idx, chunk)    

def copyStaticFiles():
    for dir in ['css', 'files', 'img']:
        dest = 'output/' + dir
        if(os.path.isdir(dest)):
            shutil.rmtree(dest)
        shutil.copytree(dir, dest)

def createOutputDirectory():
    if not os.path.exists('output'):
        os.makedirs('output')

def processPages():
    for file in sorted(filter(isPage, pagelist)):
        (basename, ext) = file.split('.')
        infile = codecs.open('pages/'+ file, 'r', 'utf-8')
        outfile = open('output/' + basename + '.html', 'w')
        writePage(basename, infile, outfile)
        infile.close()
        outfile.close()
        #print('Done with {0}\n'.format(infile.name))

def processPosts():
    for file in sorted(filter(isPage, postlist)):
        (date_and_basename, ext) = file.split('.')
        infile = codecs.open('posts/'+ file, 'r', 'utf-8')
        name_chunks = date_and_basename.split('-')
        year = name_chunks[0]
        month = name_chunks[1]
        day = name_chunks[2]
        basename = '-'.join(name_chunks[3:])
        filepath = 'output/' + year + '/' + month + '/' + day + '/' + basename + '.html'
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as outfile:
            writePost(basename, infile, outfile)
        infile.close()
        #print('Done with {0}'.format(infile.name))

def finishPage(outfile):
    outfile.write('</main>')
    sidebar = open('sidebar.html', 'r').read()
    outfile.write(sidebar)
    outfile.write(footer)

if __name__ == '__main__':
    createOutputDirectory()
    writeSidebar()
    processPages()
    processPosts()
    copyStaticFiles()
    writeMultiposts()
