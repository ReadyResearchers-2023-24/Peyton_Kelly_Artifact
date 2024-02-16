from django.db import models
import os
from datetime import datetime
#from django.contrib.auth.models import AbstractUser
#import random
# Create your models here.


class CPU_load(models.Model):
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    totalSiteVisits = models.IntegerField()
    now = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.now)


class Monitor(models.Model):
    continent = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ip
    
    
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

''' 
class CustumUser(AbstractUser):
    phone_number = models.CharField(max_length=12)
    

class CODE (models.Model):
    number = models.CharField(max_length=5)
    user = models.OneToOneField(CustumUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}"
    
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args, **kwargs)
'''