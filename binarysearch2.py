# recursive binary search

def binarySearch2(lst, start, end, value):
    if start > end:
        return -1
    mid = (start + end)//2
    if lst[mid] == val:
        return mid
    elif val > lst[mid]:
        start = mid+1
        return binarySearch2(lst, start, end, value)
    else:
        end = mid-1
        return binarySearch2(lst, start, end, value)

lst = input("Enter sorted list of numbers separated by spaces: ")
lst = list(map(int, lst.split()))
end = len(lst)-1

val = int(input("Enter value to be found: "))

print (binarySearch2(lst, 0, end, val))    