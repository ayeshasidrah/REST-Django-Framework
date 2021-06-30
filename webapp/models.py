from django.db import models


class mobiles(models.Model):
    name = models.CharField(max_length=10)
    performance = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.name
