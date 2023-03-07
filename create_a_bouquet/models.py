from django.db import models


class select_flower(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name                                 


class bouquet(models.Model):
    
    COLOURS_CHOICES = (('Red', 'Red'),
                       ('White', 'White'),
                       ('Pink', 'Pink'))
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024,
                                null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    select_colour = models.CharField(max_length=254, choices=COLOURS_CHOICES, default='Red')
    select_flowers = models.CharField(max_length=254)
    arrangement = models.CharField(max_length=254)                        

    def __str__(self):
        return self.name