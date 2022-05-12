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
    <meta name="twitter:description" content="Python早見帳は、Pythonのプログラムと実行例をさっと確認（早見）できるJupyter Notebook（帳）です。">
    <meta name="twitter:image" content="https://chokkan.github.io/python/_static/python-note.png">

    <!-- Google Analytics -->
"""

sagemaker_studio_lab = """
alt="Interact on Colab">Colab</button></a>

<a class="colab-button" href="https://studiolab.sagemaker.aws/import/github/chokkan/python/blob/master/{}">
    <button type="button" class="btn btn-secondary topbarbtn" title="起動 SageMaker Studio Lab" data-toggle="tooltip" data-placement="left">
        <i class="fab fa-aws"></i>
        SageMaker
    </button>
</a>
"""

def build():
    os.system('jupyter-book build --all .')

def modify_html():
    # Copy the Twitter card.
    shutil.copyfile('./material/python-note.png', './_build/html/_static/python-note.png')
    # Modify the generated HTML files.
    for src in glob.glob('_build/html/**/*.html', recursive=True):
        print(f'Updating: {src}')

        # Load the HTML content.
        with open(src) as fi:
            content = fi.read()

        # Find the path to .ipynb
        path = ''
        m = re.search(r'"https://colab\.research\.google\.com/github/chokkan/python/blob/main/([^"]+)"', content)
        if m is not None:
            path = m.group(1)
            print(f'    path: {path}')

        # Add meta tags for Twitter card.
        content = content.replace('<!-- Google Analytics -->', twitter_card)

        # An ad-hoc fix for the incorrect translation.
        content = content.replace('title="発売 ', 'title="起動 ')

        # Add the button for SageMaker Studio Lab.
        if path:
            content = content.replace(
                'alt="Interact on Colab">Colab</button></a>',
                sagemaker_studio_lab.format(path)
                )

        # Write out the HTML content.
        with open(src, 'w') as fo:
            fo.write(content)

def update_license():
    for src in glob.glob('*.ipynb'):
        with open(src) as fi:
            content = fi.read()
        with open(src, 'w') as fo:
            fo.write(content)

if __name__ == '__main__':
    #update_license()
    build()
    modify_html()
