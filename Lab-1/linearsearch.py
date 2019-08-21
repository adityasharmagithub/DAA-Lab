# Linear search

def linearSearch(lst, val):
    flag = 0
    for i in lst:
        if i == val:
            flag = 1
            print("Value Found!")
            break
    if flag == 0:
        print("Value not in the list")

lst = input("Enter list of numbers separated by spaces: ")
lst = list(map(int, lst.split()))

val = int(input("Enter value to be found: "))

linearSearch(lst, val)
