try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'command scanner',
    'author': 'Stafford',
    'url': 'https://github.com/staffordc/ex49.py',
    'download_url': 'Where to get it at.',
    'author_email': '*//stafford.carh@gmail.com//*',
    'version': '0.1',
    'install_requires': ['nose, nose.tools'],
    'packages': [''],
    'scripts': ['lexicon'],
    'Game': 'Scanning'
}
setup(**config)
