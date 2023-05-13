def calculate_checksum(data):
    # Split the 24-bit data into 3 8-bit segments
    segment1 = (data >> 16)
    segment2 = (data >> 8) 
    segment3 = data 
    checksum = segment1 + segment2 + segment3
    return checksum & 0xFF
data = 0x123456
checksum = calculate_checksum(data)

print(f"Data: {hex(data)}")
print(f"Checksum: {hex(checksum)}")

