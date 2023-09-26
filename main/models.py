from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)       
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    size = models.FloatField()
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True, name="date_added")