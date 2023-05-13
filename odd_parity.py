def calculate_odd_parity(data):
    binary_str = bin(data)[2:]
    count_ones = binary_str.count('1')
    if count_ones % 2 == 0:
        parity_bit = 1
    else:
        parity_bit = 0
    return (binary_str, parity_bit)
data = 124   
result = calculate_odd_parity(data)
print(result)