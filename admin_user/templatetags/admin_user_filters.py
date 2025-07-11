from django import template

register = template.Library()

@register.filter
def concat(value, arg):
    return f"{value}{arg}"


@register.filter
def split_by_delimiter(value, delimiter="__####__"):
    if value:
        return value.split(delimiter)
    return []


@register.filter
def split_by_delimiter_doller(value, delimiter="$##$"):
    if value:
        return value.split(delimiter)
    return []
