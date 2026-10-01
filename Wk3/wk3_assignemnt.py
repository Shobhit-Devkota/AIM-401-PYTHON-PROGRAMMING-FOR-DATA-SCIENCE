
# Lesson 3: Inventory Management System

# Task 1: Create inventory dictionary
inventory = {
    "Widget": 10,
    "Gadget": 5,
    "Sensor": 0,
    "Cable": 15,
    "Keyboard": 8
}

# Create a list of customer orders
orders = [
    ["Widget", 3],
    ["Sensor", 2],
    ["Gadget", 7],
    ["Cable", 5],
    ["Mouse", 4],
    ["Keyboard", 10],
    ["Widget", 4]
]

# Create a list to store unfulfilled orders
unfulfilled_orders = []

# Count fully fulfilled orders
fully_fulfilled = 0

# Task 2: Process each customer order
print("========== ORDER PROCESSING ==========")

for order in orders:
    item = order[0]
    quantity = order[1]

    # Check the available stock
    stock = inventory.get(item)

    print("\nItem:", item)
    print("Requested quantity:", quantity)

    # Check if the item exists
    if stock is None:
        print("ALERT: Item does not exist in inventory.")
        unfulfilled_orders.append([item, quantity])

    # Check if the item is out of stock
    elif stock == 0:
        print("ALERT: Item is out of stock.")
        unfulfilled_orders.append([item, quantity])

    # Full fulfillment
    elif stock >= quantity:
        inventory[item] = stock - quantity
        fully_fulfilled = fully_fulfilled + 1

        print("Order fully fulfilled.")
        print("Remaining stock:", inventory[item])

    # Partial fulfillment
    else:
        supplied = stock
        remaining = quantity - supplied

        inventory[item] = 0
        unfulfilled_orders.append([item, remaining])

        print("Partial order fulfilled.")
        print("Quantity supplied:", supplied)
        print("Quantity not supplied:", remaining)

# Task 3: Display final summary
print("\n========== FINAL INVENTORY ==========")
print(inventory)

print("\n========== ORDER SUMMARY ==========")
print("Total fully fulfilled orders:", fully_fulfilled)

print("\n========== UNFULFILLED ORDERS ==========")

if len(unfulfilled_orders) == 0:
    print("All orders were fully fulfilled.")
else:
    for order in unfulfilled_orders:
        print("Item:", order[0], "| Quantity not supplied:", order[1])

print("\nInventory processing completed.") 