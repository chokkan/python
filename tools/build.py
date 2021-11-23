#!/bin/python
import glob
import os
import re
import shutil
import sys

twitter_card = """
    <meta name="twitter:card" content="summary">
    <meta name="twitter:site" content="@chokkanorg">
    <meta name="twitter:title" content="Python早見帳">
    <meta name="twitter:description" content="Python早見帳は、Pythonのプログラムと実行例をさっと確認できるようにまとめたJupyter Notebookです。">
    <meta name="twitter:image" content="https://chokkan.github.io/python/_static/python-note.png">

    <!-- Google Analytics -->
"""

def build():
    os.system('jupyter-book build --all .')

def add_twitter_card():
    shutil.copyfile('./material/python-note.png', './_build/html/_static/python-note.png')
    for src in glob.glob('_build/html/*.html'):
        with open(src) as fi:
            content = fi.read()
        content = content.replace('<!-- Google Analytics -->', twitter_card)
        with open(src, 'w') as fo:
            fo.write(content)

if __name__ == '__main__':
    build()
    add_twitter_card()
