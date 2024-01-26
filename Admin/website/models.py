from django.db import models

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
    

    def __str__(self):
        return (f"{self.first_name}+ {self.last_name}")
        #return self.name



class Companies(models.Model):
    Name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    Product = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    Quantity = models.CharField(max_length=200)
    Total = models.CharField(max_length=200)
    def __str__(self):
        return (f"{self.Name} : {self.Price}")
        #return self.name
    
    
    