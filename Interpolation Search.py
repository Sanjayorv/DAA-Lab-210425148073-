def interpolation(arr,x):
    low = 0
    high = len(arr) - 1
    while low<=high and arr[low] <= x <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == x:
                return low
            return -1
        pos = low + ((high-low)*(x-arr[low])) // (arr[high]-arr[low])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos+1 
        if arr[pos] > x:
            high = pos-1
        return -1
arr = [10,20,30,40,50,60,70,80,90,100]
x = 70
result = interpolation(arr,x)
if result != -1:
    print(f"Element found at the array[{result}]")
else:
    print("Element not found")
