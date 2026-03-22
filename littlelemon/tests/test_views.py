from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=200, inventory=10)
        Menu.objects.create(title="Burger", price=100, inventory=5)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)