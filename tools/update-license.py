#!/bin/python

import glob

if __name__ == '__main__':
    for src in glob.glob('*.ipynb'):
        with open(src) as fi:
            content = fi.read()
        content = content.replace('Copyright 2020-2022', 'Copyright 2020-2024')
        content = content.replace('"copyrightYear": 2022,', '"copyrightYear": 2024,')
        with open(src, 'w') as fo:
            fo.write(content)
