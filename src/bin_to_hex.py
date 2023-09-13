def bin_to_hex(bin_str):
    hex_str = hex(int(bin_str, 2))[2:]
    return hex_str.upper()

bin_number = "00000000000000000000000001101101"

hex_number = bin_to_hex(bin_number)
int_number = int(bin_number, 2)

print("Hex: ", hex_number)
print("Int: ", int_number)
