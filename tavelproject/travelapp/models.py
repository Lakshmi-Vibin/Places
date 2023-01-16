from django.db import models


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Guides(models.Model):
    imgg = models.ImageField(upload_to='pics')
    nameg = models.CharField(max_length=250)
    descg = models.TextField()

    def __str__(self):
        return self.nameg