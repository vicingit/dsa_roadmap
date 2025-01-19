def find_max_min(array):
    # case where the array is empty
    if not array:
        return None, None
    
    # Initialize max_value and min_value with the first element of the array
    max_value = array[0]
    min_value = array[0]

    # loop from the second element to the last element of the array
    for element in array[1:]:
        if element > max_value:
            max_value = element
        if element < min_value:
            min_value = element

    return max_value, min_value

# example usage
array = []
max_val, min_val = find_max_min(array)


# handle output based return values
if max_val is None and min_val is None:
    print("Array is empty")
else:
    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")



