# Caesar-Shift Log Decryptor and Security Alert Filter
input_file = open(r"D:\Python_For_DataScience\Wk2\raw_logs.txt", "r")
master_file = open("decrypted_master.txt", "w")
alert_file = open("security_alerts.txt", "w")

for line in input_file:
    decrypted_line = ""

    for character in line:
        if "A" <= character <= "Z":
            decrypted_character = chr((ord(character) - ord("A") - 3) % 26 + ord("A"))
            decrypted_line = decrypted_line + decrypted_character
        elif "a" <= character <= "z":
            decrypted_character = chr((ord(character) - ord("a") - 3) % 26 + ord("a"))
            decrypted_line = decrypted_line + decrypted_character
        else:
            decrypted_line = decrypted_line + character

    decrypted_line = decrypted_line.strip()
    master_file.write(decrypted_line + "\n")

    if "BREACH" in decrypted_line.upper():
        alert_file.write(decrypted_line + "\n")

input_file.close()
master_file.close()
alert_file.close()

print("Log decryption and filtering completed.")
print("Decrypted logs saved to decrypted_master.txt")
print("Security alerts saved to security_alerts.txt")


