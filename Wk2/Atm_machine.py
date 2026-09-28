balance = 3000
while True:
    print("\n ---Select your choice to perform the operation---")
    print("1. Check Balance ")
    print("2. Deposit Money")
    print("3. Exit")

    choice = int(input("Enter your choice(1/2/3): "))
    if choice == 1:
            print(f"Your current balance is: {balance}")
    elif choice == 2:
        deposit_amount = float(input("Enter amount to deposit: "))
        balance+= deposit_amount
        print(f"Successfully deposited: Rs {deposit_amount} and, New balance is: Rs {balance}")
    elif choice == 3:
        print("Thank you for using the ATM machine. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1 to 3 option.")
        break