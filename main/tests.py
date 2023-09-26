from django.test import TestCase, Client
from main.models import Item
from datetime import date

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def create_item(self):
        self.item = Item.objects.create(
            name = "Nike Air Force 1",
            price = 2000000,
            size = 39.5,
            amount = 10,
            description = "Full white"
        )
        return self.item

    # memeriksa apakah object Item berhasil dibuat
    def test_item_creation(self):
        new_item = self.create_item()
        self.assertTrue(isinstance(new_item, Item))

    # memeriksa date_added sesuai dengan tanggal Product dibuat
    def test_date_added(self):
        new_item = self.create_item()
        self.assertIsInstance(getattr(new_item, 'date_added'), type(date.today()))