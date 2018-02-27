from django import template
from django.template.defaultfilters import stringfilter
from string import ascii_letters

register = template.Library()


@register.filter
@stringfilter
def lower_upper(string: str):
    res = ''
    i = 0
    for c in string:
        if c not in ascii_letters:
            res += c
            i = 0
        else:
            if i % 2 == 0:
                res += c.lower()
            else:
                res += c.upper()
            i += 1
    return res
