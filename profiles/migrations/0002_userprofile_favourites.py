# Generated by Django 3.2 on 2023-03-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_favourites'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favourites',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]