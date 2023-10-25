#!/usr/bin/env python3

import codecs, markdown, os, shutil

header = open('header.txt', 'r').read()

postlist = os.listdir('posts')
pagelist = os.listdir('pages')

def isPage(filename):
    if ".markdown" in filename:
        return True
    else:
        return False

def formatRecipeForPrinting(basename, infile, outfile):
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

if not os.path.exists('output'):
    os.makedirs('output')

for file in sorted(filter(isPage, pagelist)):
    (basename, ext) = file.split('.')
    infile = codecs.open('pages/'+ file, 'r', 'utf-8')
    outfile = open('output/' + basename + '.html', 'w')
    formatRecipeForPrinting(basename, infile, outfile)
    infile.close()
    outfile.close()
    print('Done with {0}'.format(infile.name))
    print('')

for dir in ['css', 'files', 'img']:
    dest = 'output/' + dir
    if(os.path.isdir(dest)):
        shutil.rmtree(dest)
    shutil.copytree(dir, dest)