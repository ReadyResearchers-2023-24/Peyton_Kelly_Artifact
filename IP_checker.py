import ipaddress
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity

def inputs():
    ip = input("Enter IP address: ")
    return ip

def check(ip):
    # Use the ip_address function from the ipaddress module to check if the input is a valid IP address
    try:
        ipaddress.ip_address(ip)
        print("Valid IP address")
    except ValueError:
        # If the input is not a valid IP address, catch the exception and print an error message
        print("Invalid IP address")




def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
ip_add = input("Enter IP: ")  # 198.35.26.96
printDetails(ip_add)



        

# Driver Code
if __name__ == '__main__':
    ip = inputs()
    check(ip)
