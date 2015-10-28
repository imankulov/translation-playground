#!/usr/bin/env python
import os
import sys
import gettext


def hello(languages):
    localedir = os.path.join(os.path.dirname(__file__), 'po')
    trans = gettext.translation('messages', localedir, languages, fallback=True)
    _ = trans.ugettext
    return _(u"Hello world")


if __name__ == '__main__':
    print hello(sys.argv[1:]).encode('utf-8')
