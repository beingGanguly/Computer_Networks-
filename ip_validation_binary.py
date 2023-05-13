ip_address = input("Enter an IP address in decimal format (e.g. 192.168.0.1): ")

octets = ip_address.split(".")
binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]

binary_ip_address = ".".join(binary_octets)

print("The binary notation of the IP address {} is {}".format(ip_address, binary_ip_address))

binary_octets = binary_ip_address.split(".")

if len(binary_octets) != 4:
    print("Invalid binary IP address!")
    exit()
for octet in binary_octets:
    if len(octet) != 8:
        print("Invalid binary IP address!")
        exit()
for octet in binary_octets:
    for digit in octet:
        if digit != "0" and digit != "1":
            print("Invalid binary IP address!")
            exit()
print("Valid binary IP address!")