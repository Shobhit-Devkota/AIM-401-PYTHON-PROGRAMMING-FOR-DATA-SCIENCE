# ==========================================
# PYTHON LIST OPERATIONS
# ==========================================

# Creating a list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)


# ==========================================
# 1. append()
# Adds ONE item at the end of the list
# ==========================================

my_list.append(60)

print("After append:", my_list)


# ==========================================
# 2. extend()
# Adds MULTIPLE items from another list
# ==========================================

new_list = [70, 80, 90]

my_list.extend(new_list)

print("After extend:", my_list)


# ==========================================
# 3. insert()
# Adds an item at a specific position
# insert(index, value)
# ==========================================

my_list.insert(2, 25)

print("After insert:", my_list)


# ==========================================
# 4. remove()
# Removes the first occurrence of a value
# ==========================================

my_list.remove(25)

print("After remove:", my_list)


# ==========================================
# 5. pop()
# Removes an item using its index
# If index is not given, removes the last item
# ==========================================

my_list.pop(2)

print("After pop:", my_list)
 

# ==========================================
# 6. index()
# Finds the position/index of an item
# ==========================================

position = my_list.index(40)

print("Index of 40:", position)


# ==========================================
# 7. count()
# Counts how many times a value appears
# ==========================================

my_list.append(20)
my_list.append(20)

print("Count of 20:", my_list.count(20))


# ==========================================
# 8. sort()
# Sorts the list in ascending order
# ==========================================

my_list.sort()

print("After sort:", my_list)


# ==========================================
# 9. reverse()
# Reverses the order of the list
# ==========================================

my_list.reverse()

print("After reverse:", my_list)


# ==========================================
# 10. copy()
# Creates a copy of the list
# ==========================================

copied_list = my_list.copy()

print("Copied List:", copied_list)


# ==========================================
# 11. clear()
# Removes all items from a list
# ==========================================

copied_list.clear()

print("After clear:", copied_list)


# ==========================================
# 12. len()
# Finds the number of items in a list
# ==========================================

print("Length of my_list:", len(my_list))


# ==========================================
# 13. min()
# Finds the smallest value
# ==========================================

print("Minimum value:", min(my_list))


# ==========================================
# 14. max()
# Finds the largest value
# ==========================================

print("Maximum value:", max(my_list))


# ==========================================
# 15. sum()
# Adds all numerical values
# ==========================================

print("Sum:", sum(my_list))


# ==========================================
# 16. in
# Checks whether an item exists in the list
# ==========================================

if 40 in my_list:
    print("40 is present in the list")


# ==========================================
# 17. not in
# Checks whether an item does NOT exist
# ==========================================

if 100 not in my_list:
    print("100 is not present in the list")


# ==========================================
# 18. Slicing
# Gets a portion of the list
# ==========================================

print("First three items:", my_list[:3])

print("Items from index 2:", my_list[2:])

print("Items from index 1 to 3:", my_list[1:4])


# ==========================================
# 19. Accessing an item using index
# ==========================================

print("First item:", my_list[0])

print("Last item:", my_list[-1])


# ==========================================
# 20. Changing an item
# ==========================================

my_list[0] = 100

print("After changing first item:", my_list)