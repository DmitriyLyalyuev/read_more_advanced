Read More Advaced
===

**Author**: Dmitriy Lyalyuev (https://lyalyuev.info)

This plugin add an "read more" or "continue" link to the end of the object summary.

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
