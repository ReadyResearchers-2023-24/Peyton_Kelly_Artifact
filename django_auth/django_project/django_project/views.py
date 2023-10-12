# pip install django-ipware
import ipaddress
from ip2geotools.databases.noncommercial import DbIpCity

def Index(request):
    context = {}
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for is not None:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("IP OF USER: ",ip)


# returns client IP address as a string
#puts ip address into a variable for next function

# add the returned ip_addr to db.sqlite3
# add the returned ip_addr to db.sqlite3

    



# compare IP info to database ip info
