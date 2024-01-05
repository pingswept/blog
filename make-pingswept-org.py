#!/usr/bin/env python3

import codecs, markdown, os, shutil

POSTS_PER_PAGE = 4

header = open('header.txt', 'r').read()

postlist = os.listdir('posts')
pagelist = os.listdir('pages')

def isPage(filename):
    if ".markdown" in filename:
        return True
    else:
        return False

def writePage(basename, infile, outfile):
    print('Processing {0} into {1}'.format(infile.name, outfile.name))
    html = markdown.markdown(infile.read(), extras=['metadata']).encode('utf8')
    outfile.write(header)
    outfile.write('<h2>{0}</h2>'.format(' '.join(basename.split('-')).capitalize()))
    #for field in ['Date', 'Makes', 'Source', 'Time']:
    #    try:
    #        outfile.write('<div id="{0}">{0}: {1}</div>'.format(field, html.metadata[field]))
    #    except KeyError:
    #        pass
    outfile.write(html.decode('utf-8'))
    outfile.write('</body>\n</html>')

def writePost(basename, infile, outfile):
    print('Processing {0} into {1}'.format(infile.name, outfile.name))
    html = markdown.markdown(infile.read(), extras=['metadata']).encode('utf8')
    outfile.write(header)
    outfile.write('<h2>{0}</h2>'.format(' '.join(basename.split('-')).capitalize()))
    #for field in ['Date', 'Makes', 'Source', 'Time']:
    #    try:
    #        outfile.write('<div id="{0}">{0}: {1}</div>'.format(field, html.metadata[field]))
    #    except KeyError:
    #        pass
    outfile.write(html.decode('utf-8'))
    outfile.write('</body>\n</html>')

def writeSidebar():
    with open('sidebar.html', 'w') as sb:
        sb.write(
'''
<div id="sidebar">  
    Static pages
    <ul>
''')
        for filename in sorted(filter(isPage, pagelist)):
            (basename, ext) = filename.split('.')
            sb.write('      <li><a href="http://pingswept.org/static/{0}.html">{1}</a></li>\n'.format(basename, basename.replace('-', ' ').capitalize()))
        sb.write(
'''    </ul> 
</div> <!-- end sidebar -->
''')
    sb.close()

def writeIndex():
    posts = sorted(filter(isPage, postlist))
    outfile = open('output/index.html', 'w')
    outfile.write(header)
    for post in reversed(posts[-4:]):
        with open('posts/' + post, 'r') as infile:
            print('Adding {0} to index.html'.format(infile.name))
            html = markdown.markdown(infile.read(), extras=['metadata']).encode('utf8')
            outfile.write('<h2>{0}</h2>'.format(' '.join(post.split('-')[3:]).capitalize()))
            outfile.write(html.decode('utf-8'))
    outfile.write('</body>\n</html>')

if not os.path.exists('output'):
    os.makedirs('output')

for file in sorted(filter(isPage, pagelist)):
    (basename, ext) = file.split('.')
    infile = codecs.open('pages/'+ file, 'r', 'utf-8')
    outfile = open('output/' + basename + '.html', 'w')
    writePage(basename, infile, outfile)
    infile.close()
    outfile.close()
    print('Done with {0}'.format(infile.name))
    print('')

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
    print('Done with {0}'.format(infile.name))
    print('')

writeIndex()

for dir in ['css', 'files', 'img']:
    dest = 'output/' + dir
    if(os.path.isdir(dest)):
        shutil.rmtree(dest)
    shutil.copytree(dir, dest)

writeSidebar()
