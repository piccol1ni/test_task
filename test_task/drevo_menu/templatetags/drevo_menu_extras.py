from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    all_categories = MenuDrevo.objects.all()
    main_menu = list(filter(lambda category: category.menu_title == name_menu, all_categories))[0]
    menu_categories = list(filter(lambda category: category.parent == main_menu, all_categories))
    children_categories = {}

    def tree(main_menu):
        if menu_categories == []:
            return main_menu
        else:
            for category in menu_categories:
                return tree(category)
        

        

        return children_categories
    #--Wraper

    return tree(main_menu, all_categories)

