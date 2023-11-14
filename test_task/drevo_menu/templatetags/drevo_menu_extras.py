from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context):
    print(context['request'].path)
    return  MenuDrevo.objects.all()
