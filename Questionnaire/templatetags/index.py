from django import template

register = template.Library()

@register.filter(name='index')
def index(value, ndx):
    return value[ndx]
