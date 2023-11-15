from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    all_categories = MenuDrevo.objects.all()
    main_menu = list(filter(lambda category: category.menu_title == name_menu, all_categories))[0]
    main_menu.parent = None
    children_categories = {}
    #--wrapper
    def tree(main_menu, all_categories):
        children_categories[main_menu] = list(filter(lambda category: category.parent == main_menu, all_categories))

        return children_categories
    #--Wraper

    return tree(main_menu, all_categories)
