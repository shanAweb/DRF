from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=100)
    

