from django import template

register = template.Library()
@register.filter(name = 'cut')
def cut(value, arg):
    """
    the the arg is going to be removed from value 
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
