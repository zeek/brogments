ABOUT
=====

The Bro network intrusion detection systems has its own Turing-complete
scripting language. When publishing code snippets in the Bro language, syntax
highlighting can help to quickly pinpoint and parse the syntax with the naked
eye. 

Brogments is a syntax highlighter for [Pygments](http://pygments.org/). As of
[ca1fbb012c9d](https://bitbucket.org/birkenfeld/pygments-main/changeset/ca1fbb012c9d),
Brogments became officially part of Pygments. However, if you use Pygments 1.4
or older, Brogments comes in handy.

INSTALL
-------

    python setup.py install

USAGE
-----

    pygmentize -f html foo.bro

or

    pygmentize -l bro -f html < foo.bro
