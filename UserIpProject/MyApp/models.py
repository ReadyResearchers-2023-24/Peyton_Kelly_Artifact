from django.db import models

# Create your models here.
#TAKE NOTE: This is where you create your database tables

#STORE THE USER IP ADDRESS
class UserIp: 
    ip_address = None
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __str__(self):
        return self.ip_address 

 
    
# WHERE CAN I DO SOMETHING WITH THE IP ADDRESS
class UserIpLocation(models.Model):
    ip_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)


class Data(models.Model):
    ip_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    

    def __str__(self):  
        return self.ip_address