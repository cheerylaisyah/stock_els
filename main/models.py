from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()  # for quantity of the stock
    size = models.FloatField()
    price = models.IntegerField()
    description = models.TextField()
<<<<<<< HEAD
    date_added = models.DateField(auto_now_add=True, name="date_added")
=======
    date_added = models.DateField(auto_now_add=True)
>>>>>>> 9ab20b349401b9a085ac9a0a73561a22a80a4a0e
