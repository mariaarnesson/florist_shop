# Generated by Django 3.2 on 2023-03-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_a_bouquet', '0003_rename_flowers_bouquet_select_flowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='select_colour',
            field=models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Pink', 'Pink')], default='Red', max_length=254),
        ),
    ]
