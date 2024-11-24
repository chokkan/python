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
    </head>
"""

sagemaker_studio_lab = """
<span class="btn__text-container">Colab</span>
</a>
</li>

<li>
    <a href="https://studiolab.sagemaker.aws/import/github/chokkan/python/blob/main/{}"
       class="btn btn-sm dropdown-item"
       title="Launch on SageMaker Studio Lab"
       data-bs-placement="left" data-bs-toggle="tooltip">

<span class="btn__icon-container">
  <i class="fab fa-aws"></i>
</span>
<span class="btn__text-container">SageMaker</span>
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
        content = content.replace('</head>', twitter_card)
        
        # Add the button for SageMaker Studio Lab.
        if path:
            content = content.replace(
                '<span class="btn__text-container">Colab</span>',
                sagemaker_studio_lab.format(path)
                )
        
        # Write out the HTML content.
        with open(src, 'w') as fo:
            fo.write(content)

def update_license():
    for src in glob.glob('*.ipynb'):
        with open(src) as fi:
            content = fi.read()
            #content = content.replace('Copyright 2020-2022', 'Copyright 2020-2024')
        with open(src, 'w') as fo:
            fo.write(content)

if __name__ == '__main__':
    #update_license()
    build()
    modify_html()
