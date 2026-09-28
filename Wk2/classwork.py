# name = "Shobhit"

# for i in range(len(name)):
#     print(i, name[i])

# indexing
# data = "Hi my name is shobhit prasad devkota"

# print(data[0:])
# print(data[-3:])
# print(data[-1])

# x = ["hello", "My ", "Name", "is "]
# print(x[0])

# filelist = ['myfile.txt', 'myprogram.exe', 'yourfile.txt']

# for filename in filelist:
#     # print(filename)
#     if '.txt' in filename:
#         print(filename)

# Encryption 
# word = input("Enter a word: ")
# value = int(input("Enter shift value: "))

# ciphertext = ""

# for letter in word:
#     new_value = ord(letter) + value
#     if new_value > ord("Z"):
#         new_value = new_value - 26

#     new_letter =chr(new_value)

#     ciphertext += new_letter
# print("Chiphertext:", ciphertext)

# Decryption Code
word = input("Enter ciphertext: ")
value = int(input("Enter shift value: "))

plaintext = ""

for letter in word:
    new_value = ord(letter) - value

    if new_value < ord("A"):
        new_value = new_value + 26

    new_letter = chr(new_value)
    plaintext += new_letter

print("Plaintext:", plaintext)
 