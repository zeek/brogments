ABOUT
=====

The Bro network intrusion detection systems has its own Turing-complete
scripting language. When publishing code snippets in the Bro language, syntax
highlighting can help to quickly pinpoint and parse the syntax with the naked
eye. Because the popular syntax highlighter [Pygments](http://pygments.org/)
lacks a lexer for the Bro language, this is a first attempt to provide one.

INSTALL
-------

    python setup.py install

USAGE
-----

    pygmentize -f html foo.bro
