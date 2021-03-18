def BinarySearch(arr,low, high,x):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            return BinarySearch(arr, mid + 1, high,x)
        else:
            return BinarySearch(arr, low, mid-1,x)
    return 0

arr = [1, 4, 5, 10, 12, 14]
high = len(arr)
res = BinarySearch(arr,0,high-1,10)
print(res)