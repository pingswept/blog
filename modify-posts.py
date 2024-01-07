#!/usr/bin/env python3

import codecs, frontmatter, markdown, os, shutil
import datetime as dt

postlist = os.listdir('posts')
pagelist = os.listdir('pages')

def isPage(filename):
    if ".markdown" in filename:
        return True
    else:
        return False

def modifyDateField(filelist):
    for file in sorted(filter(isPage, filelist)):
        with open('posts/' + file, 'r') as infile:
            print('Checking {0}'.format(infile.name))
            p = frontmatter.load(infile) # split off the YAML header
            p['date'] = p['date'].split(' ')[0].replace('/','-') + 'T00:00:00.000Z'
        with open('posts/' + file, 'w') as outfile:
            outfile.write(frontmatter.dumps(p) + '\n')

if __name__ == '__main__':
    modifyDateField(postlist)