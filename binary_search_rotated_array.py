# To find Pivot element
def finding_pivot(arr, l, r):
    mid = int((l + r) / 2)
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    elif arr[mid] >= arr[l]:
        l = mid + 1
        return finding_pivot(arr, l, r)
    else:
        r = mid - 1
        return finding_pivot(arr, l, r)
# To find an element
def binary_search(arr, l, r, x):
    if r >= l: 
        mid = (l+r) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            l = mid + 1
            return binary_search(arr, l, r, x)
        else:
            r = mid - 1
            return binary_search(arr, l, r, x)
    else:
        return -1

print("no of elements to enter")
n = int(input())
arr = list()
#arr = [4,5,1,2,3]
print("Enter sorted rotated array ")
for i in range(0,n):
    num = int(input())
    arr.append(num)

print(arr)

if arr[0] <= arr[len(arr)-1]: 
    print("array is not rotated")
    pivot = 0
else:
    pivot = finding_pivot(arr, 0, len(arr)-1)
    print("pivot element index "+str(pivot))

while True:    
    print ("element to find")
    x = int(input())
    #x = 1
    if x == "":
        continue
    elif x == arr[pivot]:
        result = pivot
    elif x < arr[pivot] and x >= arr[0]:
        result = binary_search(arr, 0, pivot-1, x)
    else:
        result = binary_search(arr, pivot+1, len(arr)-1, x)
   
    if result == -1:
        print (str(x) + " not found")
    else:
        print ("Element is present at index "+str(result))
    