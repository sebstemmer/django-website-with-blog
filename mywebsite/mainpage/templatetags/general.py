from django import template

register = template.Library()


@register.filter
def startswith(path, arg):
    if path.startswith(arg):
        return True
    else:
        return False
