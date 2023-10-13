from django.shortcuts import HttpResponse
from .models import UserIp, UserIpLocation
from django.shortcuts import render
from ip2geotools.databases.noncommercial import DbIpCity
# Create Viewe

def ipaddress(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip is not None:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    #send IP to the models.py file
    user_ip = UserIp(ip_address=ip)
    # get the user ip address
    return HttpResponse("Welcome User!<br>You are visiting from: {}".format(ip))
# Create your views here.


# use the ip2location database to get the location of the user

# Update view to show the location of the user
def location(ip,request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip is not None:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    res = DbIpCity.get(ip, api_key="free")
    city = res.city
    region = res.region
    country = res.country
    latitude = res.latitude
    longitude = res.longitude
    # save the user ip address
    user_ip = UserIp(ip_address=ip)
    #save the user ip location
    UserIp.save(user_ip)
   # save the user ip location
    user_ip_location = UserIpLocation(ip_address=ip, city=city, region=region, country=country, latitude=latitude, longitude=longitude)
    

# Create a view to show the location of the user
