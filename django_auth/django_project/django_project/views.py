# pip install django-ipware
import ipaddress



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

# add the returned ip_addr to db.sqlite3
# add the returned ip_addr to db.sqlite3
def add_ip_to_db(ip_addr, request):
    ip_addr = get_client_ip_address(request)
    ip_addr = ipaddress.ip_address(ip_addr)
    ip_addr.save()
    


def get_client_location(ip, request):
    ip = get_client_ip_address(request)
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
      # 198.35.26.96
    print(get_client_location(ip))

