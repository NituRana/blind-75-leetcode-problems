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

arr = [-2,1,-3,4,-1,2,1,-5,4]

def max_sum_sub_array(arr):
    n = len(arr)
    max_sum = arr[0]
    start = end = 0

    for i in range(n):
        for j in range(i + 1, n):
            current_sum = sum(arr[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j
    print(f"------------- sub array : {arr[start:end+1]}")
    return max_sum

res = max_sum_sub_array(arr)
print("------------- res :", res)



