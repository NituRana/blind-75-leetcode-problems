'''

Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Examples
Example 1:
Input:
 arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output:
 6 


'''
# Approaches to Solve the Problem


# 1. Brute Force Approach

arr = [-2,1,-3,4,-1,2,1,-5,4]

# def max_sum_sub_array(arr):
#     n = len(arr)
#     max_sum = arr[0]
#     start = end = 0

#     for i in range(n):
#         for j in range(i + 1, n):
#             current_sum = sum(arr[i:j+1])
#             if current_sum > max_sum:
#                 max_sum = current_sum
#                 start, end = i, j
#     print(f"------------- sub array : {arr[start:end+1]}")
#     return max_sum

# res = max_sum_sub_array(arr)
# print("------------- res :", res)


def max_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf')
    start = end = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j

    print(f"Subarray: {arr[start:end+1]}")
    return max_sum


print(max_subarray_sum(arr))


