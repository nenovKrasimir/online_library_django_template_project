from django import template

register = template.Library()


@register.filter(name="Disabled_fields")
def filters(value):
    return value.as_widget(attrs={'disabled': 'disabled'})