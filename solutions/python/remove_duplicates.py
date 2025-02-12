def remove_duplicates(arr):
    if not arr:
        return 0
    
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1

#eg

arr = [1,2,4,4,5,5,6]
length = remove_duplicates(arr)

print(arr[:length])