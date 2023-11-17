from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    all_categories = MenuDrevo.objects.all()
    children_categories = {}

    def tree(name_menu):
        try:
            main_menu = list(filter(lambda category: category.menu_title == name_menu, all_categories))[0]
        except IndexError:
            return children_categories
        menu_categories = list(filter(lambda category: category.parent == main_menu, all_categories))
        print(children_categories)
        if menu_categories == []:
            children_categories[main_menu] = []
        else :
            children_categories[main_menu] = menu_categories
            for category in menu_categories:
                return tree(category.menu_title)

    return tree(name_menu)


