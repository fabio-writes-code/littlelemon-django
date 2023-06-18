from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu


class MenuViewTest(TestCase):

  def setUp(self):
    Menu(title='Test Cream 1', price=1, inventory=6).save()
    Menu(title='Test Cream 2', price=2, inventory=7).save()
    Menu(title='Test Cream 3', price=3, inventory=8).save()

    self.client = APIClient()

  def test_getall(self):
    response = self.client.get('/restaurant/menu/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), len(Menu.objects.all()))
