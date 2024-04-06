from django import template
from mymenu.models import MenuItem


register = template.Library()


@register.inclusion_tag('tags/menu.html', takes_context=True)
def draw_menu(context: dict, menu_name: str) -> dict:
    request = context.get('request')
    current_url = request.path if request else ''

    menu = MenuItem.objects. \
        filter(
            menu__name=menu_name,
        ).order_by('mpath'). \
        all()

    return {
        'menu': menu,
        'current_url': current_url
    }


@register.simple_tag
def draw_depth(depth: int) -> str:
    return '─' * depth
