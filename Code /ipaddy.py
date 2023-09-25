import ipaddress
"""
def check(ip):
    # Use the ip_address function from the ipaddress module to check if the input is a valid IP address
    try:
        ipaddress.ip_address(ip)
        print("Valid IP address")
    except ValueError:
        # If the input is not a valid IP address, catch the exception and print an error message
        print("Invalid IP address")
 
# Driver Code
if __name__ == '__main__':
    ip = "192.168.0.1"
    check(ip)
 
    ip = "110.234.52.124"
    check(ip)
 
    ip = "366.1.2.2"
    check(ip)

"""
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)




