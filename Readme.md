Read More Advaced for [Pelican](http://getpelican.com/)
===

**Author**: Dmitriy Lyalyuev (https://lyalyuev.info)

This plugin split article with "more" tag and add an "read more" or "continue" link to end of first part of article.

Settings
---
    # This indicates what goes inside the read more link
    READ_MORE_LINK = None (ex: 'Read more...')

    # This is the format of the read more link
    READ_MORE_LINK_FORMAT = '<a class="read-more" href="/{url}">{text}</a>'

Usage
---

Add to article tag:

&lt;!-- more --&gt;

and article will be truncated at this line.

BASED ON
===

This plugin based on '[Read More Link](https://github.com/getpelican/pelican-plugins/tree/master/read_more_link)' plugin
