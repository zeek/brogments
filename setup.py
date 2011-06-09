"""
A Pygments lexer for Bro policy scripts.
"""

from setuptools import setup

__author__ = 'Matthias Vallentin'
__email__ = 'vallentin@icir.org'
__copyright__ = 'Copyright 2011, Matthias Vallentin'
__license__ = 'BSD'
__version__ = '0.1'
__maintainer__ = 'Matthias Vallentin'

entry_points = '''[pygments.lexers]
brolexer = bro_lexer.bro:BroLexer
'''
 
setup(
    name = 'brogments',
    version = '0.1',
    description= __doc__,
    author = __author__,
    packages = ['bro_lexer'],
    entry_points = entry_points
)
