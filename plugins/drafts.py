# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import collections
import os.path

from logging import warning, info
from codecs import open

from pelican import signals, contents

class DraftsIndexGenerator(object):
    def __init__(self, context, settings, path, theme, output_path, *null):
        self.output_path = output_path
        self.context = context

    def write_url(self, page, fd):
        pass

    def generate_output(self, writer):
        path = os.path.join(self.output_path, 'drafts.html')

        pages = self.context['articles']

        info('writing {0}'.format(path))

        with open(path, 'w', encoding='utf-8') as fd:
            FakePage = collections.namedtuple('FakePage', ['status', 'date', 'url'])

            for page in pages:
                self.write_url(page, fd)

def get_generators(generators):
    return DraftsIndexGenerator

def register():
    signals.get_generators.connect(get_generators)
