from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    name            = models.CharField(max_length=150)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=10, decimal_places=2, default=39.99)
    list_date       = models.DateField(default=datetime.now,)
    featured        = models.BooleanField(default=False)
    photo_main      = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

