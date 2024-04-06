from django.core.management.base import BaseCommand, CommandError
from mymenu.models import Menu, MenuItem


class Command(BaseCommand):
    help = "Create menu examples"

    def create_menu(self, name: str, title: str) -> Menu:
        try:
            menu = Menu.objects.get(name=name)
            menu.delete()
        except Menu.DoesNotExist:
            # nothing to delete
            pass

        menu = Menu.objects.create(name=name, title=title)

        self.stdout.write(
            self.style.SUCCESS('Menu  "%s" is created' % menu.name)
        )

        return menu

    def handle(self, *args, **options):
        menu1 = self.create_menu('main_menu', 'Main menu')

        m1 = MenuItem.objects.create(
            menu=menu1, title='item1')
        m2 = MenuItem.objects.create(
            menu=menu1, title='item2')
        m3 = MenuItem.objects.create(
            menu=menu1, title='item3', parent=m2)
        MenuItem.objects.create(
            menu=menu1, title='item4', parent=m3)
        MenuItem.objects.create(
            menu=menu1, title='item5', parent=m1)
        m6 = MenuItem.objects.create(
            menu=menu1, title='item6', parent=m1)
        MenuItem.objects.create(
            menu=menu1, title='item7', parent=m6)

        menu2 = self.create_menu('second_menu', 'Second menu')

        MenuItem.objects.create(
            menu=menu2, title='item1_2')
        m2 = MenuItem.objects.create(
            menu=menu2, title='item2_2')
        MenuItem.objects.create(
            menu=menu2, title='item3_2', parent=m2)
        m4 = MenuItem.objects.create(
            menu=menu2, title='item4_2', parent=m2)
        MenuItem.objects.create(
            menu=menu2, title='item5_2', parent=m4)
