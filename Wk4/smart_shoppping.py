
def shopping_cart():
    prices = []

    # Ask the user to enter 5 product prices
    for i in range(5):
        price = float(input(f"Enter price of product {i + 1}: "))
        prices.append(price)

    total = 0
    for price in prices:
        total = total + price

    if total >= 5000:
        discount = total * 0.15
    elif total >= 3000:
        discount = total * 0.10
    elif total >= 1000:
        discount = total * 0.05
    else:
        discount = 0

    # Calculate the final payable amount
    final_amount = total - discount

    # Display the shopping cart details
    print("\n===== SMART SHOPPING CART =====")
    print("Product Prices:")

    for i in range(5):
        print(f"Product {i + 1}: Rs. {prices[i]:.2f}")

    print("-------------------------------")
    print(f"Total Amount: Rs. {total:.2f}")
    print(f"Discount Amount: Rs. {discount:.2f}")
    print(f"Final Payable Amount: Rs. {final_amount:.2f}")
    print("===============================")


# Call the function
shopping_cart()