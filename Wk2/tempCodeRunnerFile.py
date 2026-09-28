binary_num = int(input("Enter a binary number: "))
binary_digits = ['0','1']
for char in binary_num:
    if char not in binary_digits:
        print("Invalid binary number")
        break
else:
    decimal_value = 0
    exponent =len(binary_num) - 1
    for digit in binary_num:
        decimal_value += digit * (2** exponent)
        exponent -= 1

print("Decimal equivalent : {decimal_value}")
