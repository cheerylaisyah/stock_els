# Generated by Django 4.2.5 on 2023-09-12 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
    ]
