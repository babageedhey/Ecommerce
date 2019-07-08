from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email