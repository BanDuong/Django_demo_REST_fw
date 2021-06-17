from django.db import models

# Create your models here.
class cars(models.Model):
    name = models.CharField(max_length=50)
    band = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

