"""
A Pygments lexer for Bro policy scripts.
"""

from setuptools import setup

__author__ = 'Matthias Vallentin <vallentin@icir.org>'

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
