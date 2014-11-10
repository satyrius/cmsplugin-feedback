from django import forms
from django import template
register = template.Library()


@register.filter()
def is_checkbox(field):
    return isinstance(field.field, forms.BooleanField)
