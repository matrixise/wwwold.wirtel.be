# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import requests
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer


INLINESTYLES = False
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES)
VARIANTS = {
    'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
}


class Gist(Directive):
    """ Embed Gist in posts.

    Usage:
    .. gist:: GISTID/filename
    """
    required_arguments = 1
    optional_arguments = 0
    option_spec = dict([(key, directives.flag) for key in VARIANTS])
    final_argument_whitespace = False
    has_content = False

    def run(self):
        gist = self.arguments[0].strip()

        ext = os.path.splitext(gist)[-1]

        language = {'.py': 'python'}.get(ext)

        url = 'https://raw.github.com/gist/%s' % gist
        response = requests.get(url)
        content = response.content

        try:
            lexer = get_lexer_by_name(language)
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()
        # take an arbitrary option if more than one is given
        formatter = self.options and VARIANTS[self.options.keys()[0]] or DEFAULT
        parsed = highlight(content, lexer, formatter)

        return [
            nodes.raw('', parsed, format='html')
        ]

directives.register_directive('gist', Gist)


class LiteralInclude(Directive):
    """ Source code syntax hightlighting.
    """
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = dict([(key, directives.flag) for key in VARIANTS])

    def run(self):
        filename = self.arguments[0].strip()

        ext = os.path.splitext(filename)[-1]

        language = {'.py': 'python'}.get(ext)

        try:
            lexer = get_lexer_by_name(language)
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()
        # take an arbitrary option if more than one is given
        formatter = self.options and VARIANTS[self.options.keys()[0]] or DEFAULT

        with open(filename) as fp:
            content = fp.read()
        parsed = highlight(content, lexer, formatter)
        return [nodes.raw('', parsed, format='html')]

directives.register_directive('literal-include', LiteralInclude)


def register():
    pass
