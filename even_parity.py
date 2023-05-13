def calculate_even_parity(data):
    binary_str = bin(data)[2:]
    count_ones = binary_str.count('1')
    if count_ones % 2 == 0:
        parity_bit = 0
    else:
        parity_bit = 1
    return (binary_str, parity_bit)

data = 123   
result = calculate_even_parity(data)
print(result)    
