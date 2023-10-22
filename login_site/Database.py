
from ip2geotools.databases.noncommercial import DbIpCity
import socket 



def find_my_ip():
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)    
    print(f"Hostname: {hostname}")    
    print(f"IP Address: {ip_address}")    
    return ip_address
    


"""FIle to compare actual vs data"""
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

#find_my_ip()
ip_address = find_my_ip()
printDetails(ip_address)



#compare IP info to database ip info

#driver code

    