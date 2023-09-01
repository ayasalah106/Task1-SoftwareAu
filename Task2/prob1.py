def binary_search_recursive(arr, low, high,num):
    if low > high:
        return False 
    mid = low + (high - low) // 2
    if arr[mid] == num:
        return mid  
    elif arr[mid] > num:
        return binary_search_recursive(arr, low, mid - 1, num)
    else:
        return binary_search_recursive(arr, mid + 1, high, num)


arr = [1,2,3,4,5,6,7,8,9,10]
num = 2

result = binary_search_recursive(arr, 0, len(arr) - 1, num)

if result != False:
    print("Element found at index:", result)
else:
    print("Element not found.")