# binary search without recurrsion

def binarySearch(lst, n, val):
    start = 0
    end = n-1
    flag = 0
    while(start <= end):
        mid = (start + end)//2
        if lst[mid] == val:
            flag = 1
            print("Value Found at index", mid)
            break
        elif val > lst[mid]:
            start = mid+1
        else :
            end = mid-1
    if flag == 0:
        print("Value not found")

lst = input("Enter sorted list of numbers separated by spaces: ")
lst = list(map(int, lst.split()))
n = len(lst)

val = int(input("Enter value to be found: "))

binarySearch(lst, n, val)
