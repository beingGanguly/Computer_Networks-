import ipaddress
def check(ip):
    try:
        ipaddress.ip_address(ip)
        print("Valid IP address")
    except ValueError:
        print("Invalid IP address")
if __name__ == '__main__':
    ip = "192.168.117.1"
    check(ip)
 
    ip = "366.1.2.2"
    check(ip)