'''You are given an array A, consisting of "n" not negative integers. Now you need to answer Q queries, given an integer K in each query. You need to find the min length l of any sub array of A
such that if all elements of sub arrays are represented in binary notation and concatenated to form a binary string. Then no. of 1s in the result in the resulting string is atleast K'''

def checkOne(A, n, k):
    binaryA = []
    lengths = []
    ones = 0

    # making the binary equivalent array
    for i in A:
        binaryA += [bin(i)]

    # counting lengths of all possible subarrays
    for i in range(n):
        for j in range(i, n):
            ones += binaryA[j].count('1')
            if ones >= k:
                lengths += [j-i+1]
                break
        ones = 0

    # minimum length of subarray)
    minLen = min(lengths)
    print("Length of smallest possible subarray: ", minLen)

lst = input("Enter list of numbers separated by spaces: ")
lst = list(map(int, lst.split()))
n = len(lst)

Q = int(input("Enter number of queries: "))
for i in range(Q):
    k = int(input("Integer: "))
    checkOne(lst, n, k)
