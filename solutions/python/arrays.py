import array

# Creating an array
my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates integer type

# Accessing elements
print(my_array[0])  # Output: 1

# Modifying elements
my_array[1] = 10
print(my_array)  # Output: array('i', [1, 10, 3, 4, 5])

# Adding elements
my_array.append(6)
print(my_array)  # Output: array('i', [1, 10, 3, 4, 5, 6])

# Removing elements
my_array.pop(2)  # Removes the element at index 2
print(my_array)  # Output: array('i', [1, 10, 4, 5, 6])

# Iterating through the array
for element in my_array:
    print(element)
