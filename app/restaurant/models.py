from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
        