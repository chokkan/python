#!/bin/python

import glob

if __name__ == '__main__':
    for src in glob.glob('*.ipynb'):
        with open(src) as fi:
            content = fi.read()
        content = content.replace('Copyright 2020-2021', 'Copyright 2020-2022')
        content = content.replace('"copyrightYear": 2021,', '"copyrightYear": 2022,')
        with open(src, 'w') as fo:
            fo.write(content)
