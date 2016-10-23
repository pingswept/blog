#!/usr/bin/env python

import codecs, markdown2, os

header = open('header.txt', 'r').read()

dirlist = os.listdir('.')

def isPage(filename):
    if ".markdown" in filename:
        return True
    else:
        return False

def formatRecipeForPrinting(basename, infile, outfile):
    print('Processing {0} into {1}'.format(infile.name, outfile.name))
    html = markdown2.markdown(infile.read(), extras=['metadata']).encode('utf8')
    outfile.write(header)
    outfile.write('<h2>{0}</h2>'.format(' '.join(basename.split('-')).capitalize()))
    #for field in ['Date', 'Makes', 'Source', 'Time']:
    #    try:
    #        outfile.write('<div id="{0}">{0}: {1}</div>'.format(field, html.metadata[field]))
    #    except KeyError:
    #        pass
    outfile.write(html)
    outfile.write('</body>\n</html>')

for file in sorted(filter(isPage, dirlist)):
    (basename, ext) = file.split('.')
    infile = codecs.open(file, 'r', 'utf-8')
    outfile = open('output/' + basename + '.html', 'w')
    formatRecipeForPrinting(basename, infile, outfile)
    infile.close()
    outfile.close()
    print('Done with {0}'.format(infile.name))
    print('')
