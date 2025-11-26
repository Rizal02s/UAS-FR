from django.db import models

class Pemain(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    position = models.CharField(max_length=40)
    player_number = models.IntegerField(unique=True)
    salary = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name