from django.test import TestCase, Client
from main.models import Product
from datetime import date

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def create_product(self):
        self.product = Product.objects.create(
            name = "Nike Air Force 1",
            amount = 2000000,
            size = 39.5,
            qty = 10,
            description = "Full white"
        )
        return self.product

    # memeriksa apakah object Product berhasil dibuat
    def test_product_creation(self):
        new_product = self.create_product()
        self.assertTrue(isinstance(new_product, Product))

    # memeriksa date_added sesuai dengan tanggal Product dibuat
    def test_date_added(self):
        new_product = self.create_product()
        self.assertIsInstance(getattr(new_product, 'date_added'), type(date.today()))