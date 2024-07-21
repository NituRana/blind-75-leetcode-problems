'''

roblem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

Examples
Example 1:
Input Format:
 N = 5, array[] = {1,2,4,5}
Result:
 3
Explanation: 
In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format:
 N = 3, array[] = {1,3}
Result:
 2
Explanation: 
In the given array, number 2 is missing. So, 2 is the answer.


'''

#1. Brute Force Approach

# def missing_number(arr, n):
#     # Outer loop that runs from 1 to N:
#     for i in range(1, n + 1):
#         flag = 0
#         for j in range(len(arr)):
#             if arr[j] == i:
#                 flag = 1
#                 break
#         if flag == 0:
#             return i

#     return -1
# n = 5
# arr = [1, 2, 4, 5]
# ans = missing_number(arr, n)
# print("The missing number is:", ans)


#1. Better Approach
def missingNumber(a, N):
    hash = [0] * (N + 1)

    for i in range(N - 1):
        hash[a[i]] += 1


    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    return -1

N = 9
a = [1, 2, 3, 4, 5, 6, 8, 9,]
ans = missingNumber(a, N)
print("-------The missing number is:", ans)