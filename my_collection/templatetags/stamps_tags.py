from django import template
import my_collection.views as views


register = template.Library()

@register.simple_tag(name='getcats')            # Передается в base.html
def get_categories():
    return views.cats_db                # Список из cats_id

@register.inclusion_tag('my_collection/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {"cats": cats, 'cat_selected': cat_selected}