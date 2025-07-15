from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(name="Pizza", price=10.99, description="Cheesy")
        self.assertEqual(item.name, "Pizza")
