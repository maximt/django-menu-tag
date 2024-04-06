from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse
from .models import Menu, MenuItem


class MenuTestCase(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            name="Test Menu",
            title="Test Menu Title"
        )

    def test_menu_creation(self):
        self.assertEqual(str(self.menu), "Test Menu Title")


class MenuItemTestCase(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            name="Test Menu",
            title="Test Menu Title",
        )
        self.item = MenuItem.objects.create(
            menu=self.menu,
            title="Test Item",
        )
        self.subitem = MenuItem.objects.create(
            menu=self.menu,
            title="Test SubItem",
            parent=self.item,
        )

    def test_item_creation(self):
        self.assertEqual(str(self.item), "Test Item")
        self.assertEqual(str(self.subitem), "Test SubItem")

    # def test_item_url_with_named_url(self):
    #     self.item.named_url = 'test_named_url'
    #     self.item.named_url_kwargs = '{"pk":1}'
    #     self.item.save()
    #     item_url = reverse('test_named_url', kwargs={'pk': 1})
    #     self.assertEqual(self.item.get_url(), item_url)

    def test_item_url_with_custom_url(self):
        self.item.url = 'https://example.com'
        self.item.save()
        self.assertEqual(self.item.get_url(), 'https://example.com')

    def test_item_url_default(self):
        self.item.named_url = ''
        self.item.url = ''
        self.item.save()
        self.assertEqual(self.item.get_url(), None)

    @patch('mymenu.models.reverse')
    def test_item_url_with_named_url_with_kwargs(self, mock_reverse):
        expected_url = '/hello-url/1'

        mock_reverse.return_value = expected_url

        self.item.named_url = 'hello_view'
        self.item.named_url_kwargs = '{"pk":1}'
        self.item.save()

        item_url = self.item.get_url()

        mock_reverse.assert_called_once_with('hello_view', kwargs={'pk': 1})
        self.assertEqual(item_url, expected_url)

    @patch('mymenu.models.reverse')
    def test_item_url_with_named_url(self, mock_reverse):
        expected_url = '/hello-url'

        mock_reverse.return_value = expected_url

        self.item.named_url = 'hello_view'
        self.item.named_url_kwargs = ''
        self.item.save()

        item_url = self.item.get_url()

        mock_reverse.assert_called_once_with('hello_view', kwargs={})
        self.assertEqual(item_url, expected_url)

    def test_item_mpath(self):
        expected_mpath = f"{self.item.mpath}/{self.subitem.pk}"

        self.assertEqual(self.item.mpath, self.item.pk)
        self.assertEqual(self.subitem.mpath, expected_mpath)

    def test_item_depth(self):
        self.assertEqual(self.item.depth, 0)
        self.assertEqual(self.subitem.depth, 1)
