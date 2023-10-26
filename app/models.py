from django.db import models

# Create your models here.

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name