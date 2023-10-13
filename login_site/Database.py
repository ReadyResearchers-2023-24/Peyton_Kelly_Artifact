
from ip2geotools.databases.noncommercial import DbIpCity

"""FIle to compare actual vs data"""
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
ip_add = input("Enter IP: ")  # 198.35.26.96 198.35.26.96
printDetails(ip_add)

#compare IP info to database ip info
