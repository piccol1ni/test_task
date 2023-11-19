from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.inclusion_tag('drevo_menu/draw_menu.html', takes_context=True)
def draw_menu(context, name_menu):
    all_categories = MenuDrevo.objects.all()
    main_menu = list(filter(lambda category: category.menu_title == name_menu, all_categories))[0]
    children_categories = {}

    for category in all_categories:
        children_categories[category] = list(filter(lambda categori: categori.parent == category, all_categories))

    return {
        'children_categories': children_categories,
        'main_menu': main_menu,
    }

