from django.db import models
import os
from datetime import datetime

# Create your models here.


class Record(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    file = models.ImageField(upload_to="uploads/", null=True, verbose_name="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # return self.name
