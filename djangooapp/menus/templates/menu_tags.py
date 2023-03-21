from django import template
from django.urls import reverse, NoReverseMatch
from models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Get the current URL
    current_url = context['request'].path

    # Get the menu items from the database
    menu_items = MenuItem.objects.filter(name=menu_name)

    # Build a nested dictionary representing the menu
    menu_dict = {}
    for item in menu_items:
        parent_name = item.parent.name if item.parent else None
        if parent_name not in menu_dict:
            menu_dict[parent_name] = []
        menu_dict[parent_name].append(item)

    # Recursively render the menu HTML
    def render_menu(items):
        if not items:
            return ''
        output = '<ul>'
        for item in items:
            if item.url == current_url or item.named_url == current_url:
                css_class = 'active'
            else:
                css_class = ''
            output += f'<li class="{css_class}">'
            try:
                url = reverse(item.named_url)
            except NoReverseMatch:
                url = item.url
            output += f'<a href="{url}">{item.label}</a>'
            output += render_menu(menu_dict.get(item.name, []))
            output += '</li>'
        output += '</ul>'
        return output

    # Render the top-level menu items
    return render_menu(menu_dict.get(None, []))