# binary_num = input("Enter a binary number: ")

# binary_digits = ['0', '1']

# for char in binary_num:

#     if char not in binary_digits:
#         print("Invalid binary number")
#         break

# else:
#     decimal_value = 0
#     exponent = len(binary_num) - 1

#     for digit in binary_num:
#         decimal_value += int(digit) * (2 ** exponent)


# Decimals into biinary:

decimal_num = int(input("Enter a decimal number: "))

binary_num = ""

while decimal_num > 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num
    decimal_num = decimal_num // 2

print(f"Binary equivalent: {binary_num}")