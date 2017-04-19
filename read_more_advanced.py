# -*- coding: utf-8 -*-
"""
Read More Advanced
===========================

This plugin adds an "read more" or "continue" link to the end of the object summary.
"""

from pelican import signals, contents
from pelican.utils import truncate_html_words
from pelican.generators import ArticlesGenerator

def insert_instead_more_comment(html, link):
    """
    function to add "Read more" link to the of html
    example:
        html = '<p>paragraph1</p><p>paragraph2...</p>'
        element = '<a href="/read-more/">read more</a>'
        ---> '<p>paragraph1</p><p>paragraph2</p><a href="/read-more/">read more</a>'
    """

    import sys;
    reload(sys);
    sys.setdefaultencoding("utf8")

    try:
        doc = "{html}<br />{link}".format(html=html, link=link)
        return doc
    except Exception as e:
        print e
        return ''

def insert_read_more(instance):
    """
    Add an inline "read more" link to the end of the summary
    :param instance:
    :return:
    """

    # only deals with Article type
    if type(instance) != contents.Article: return

    READ_MORE_TEXT = instance.settings.get('READ_MORE_TEXT', None)
    READ_MORE_LINK_FORMAT = instance.settings.get('READ_MORE_LINK_FORMAT',
                                                  '<a class="read-more" href="/{url}">{text}</a>')

    if not (READ_MORE_TEXT and READ_MORE_LINK_FORMAT): return

    import re
    rx=re.compile(r'<!--\s+more\s+-->')
    summary = rx.sub('<!--more-->', instance.content).split('<!--more-->', 1)[0]

    if summary != instance.content:
        read_more_link = READ_MORE_LINK_FORMAT.format(url=instance.url, text=READ_MORE_TEXT.encode('utf-8'))
        instance._summary = insert_instead_more_comment(summary, read_more_link)
    else:
        instance._summary = instance.content


def run_plugin(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                insert_read_more(article)


def register():
    try:
        signals.all_generators_finalized.connect(run_plugin)
    except AttributeError:
        # NOTE: This may result in #314 so shouldn't really be relied on
        # https://github.com/getpelican/pelican-plugins/issues/314
        signals.content_object_init.connect(insert_read_more)
