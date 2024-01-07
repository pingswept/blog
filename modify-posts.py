#!/usr/bin/env python3

import codecs, frontmatter, markdown, os, shutil
import datetime as dt
import re

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

def fixDates(filelist):
    for file in sorted(filter(isPage, filelist)):
        with open('posts/' + file, 'r') as infile:
            print('Checking {0}'.format(infile.name))
            text = infile.readlines()
            modified_text = re.sub(r'^date: \'(.*?)\'$', r'date: \1', text, flags=re.MULTILINE)
        with open('posts/' + file, 'w') as outfile:
            outfile.write(modified_text)


if __name__ == '__main__':
    #modifyDateField(postlist)
    fixDates(postlist)
