def crc(data, key):
    
    # Append zeros to the data string to make it the length of the key
    data += "0" * (len(key) - 1)
    key_int = int(key, 2)
    data_int = int(data, 2)
    for i in range(len(data)):
        if ((data_int >> (len(data) - 1 - i)) & 1):
            data_int ^= key_int

    crc_str = "{0:b}".format(data_int)

    crc_str = crc_str.zfill(len(key) - 1)

    return crc_str

data = "1101011011"  
key = "1011"        
crc_val = crc(data, key)
final_word = data + crc_val
print("Data: ", data)
print("Key: ", key)
print("Calculated CRC: ", crc_val)
print("Code Word: ", final_word)
