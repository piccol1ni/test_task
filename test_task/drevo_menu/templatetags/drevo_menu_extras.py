from django import template
from drevo_menu.models import MenuDrevo


register = template.Library()

@register.inclusion_tag('drevo_menu/draw_menu.html', takes_context=True)
def draw_menu(context, name_menu):
    all_categories = MenuDrevo.objects.all()
<<<<<<< HEAD
    main_menu = list(filter(lambda category: category.menu_title == name_menu, all_categories))[0]
    children_categories = {}

    for category in all_categories:
        children_categories[category] = list(filter(lambda categori: categori.parent == category, all_categories))

    return {
        'children_categories': children_categories,
        'main_menu': main_menu,
    }
=======
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

>>>>>>> 445eb0a14665e129f7175fab97b441b032bae65b

