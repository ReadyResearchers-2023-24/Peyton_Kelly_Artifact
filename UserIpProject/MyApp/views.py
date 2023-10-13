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
    postal = res.zipcode
    # save the user ip address
    user_ip = UserIp(ip_address=ip)
    user_ip.save()
    # save the user ip location
    user_ip_location = UserIpLocation(ip_address=ip, city=city, region=region, country=country, latitude=latitude, longitude=longitude, postal=postal)
    user_ip_location.save()

# Create a view to show the location of the user
