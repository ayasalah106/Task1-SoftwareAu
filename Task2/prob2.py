import random 
def partition(arr, low, high):
    pivot = random.randint(low,high) 
    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot=arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)  
        quick_sort(arr, low, pivot-1)  
        quick_sort(arr, pivot+1, high)  


# Example usage:
arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)