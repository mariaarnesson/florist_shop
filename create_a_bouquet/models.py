from django.db import models


class bouquet(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024,
                                null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    colours = models.CharField(max_length=254)
    flowers = models.CharField(max_length=254)
    arrangement = models.CharField(max_length=254)                        

    def __str__(self):
        return self.name