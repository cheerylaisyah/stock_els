from django.test import TestCase

# Create your tests here.
<<<<<<< HEAD
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
=======
>>>>>>> 3ba95868477853d24f55d047e152a90645a72ab9
