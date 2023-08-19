
from django import template
register = template.Library()

@register.filter(name="increment_by")
def increment_by(value,arg):
    return value + str(arg)