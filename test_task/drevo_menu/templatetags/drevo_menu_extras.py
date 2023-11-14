from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.inclusion_tag("drevo_menu/index.html")
def draw_menu():
    return { "all":
        MenuDrevo.objects.all(),
    }
