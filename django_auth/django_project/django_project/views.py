# pip install django-ipware
import ipaddress

import requests

from ip2geotools.databases.noncommercial import DbIpCity


def get_client_ip_address(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    return ip_addr
# returns client IP address as a string
#puts ip address into a variable for next function



def get_client_location(ip):
    ip = get_client_ip_address(requests)
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
      # 198.35.26.96
    get_client_location(ip)
