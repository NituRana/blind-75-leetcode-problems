'''

Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Examples
Example 1:
Input:

Nums = [1,2,3,4,5,0]
Output:

 120
Explanation:

In the given array, we can see 1×2×3×4×5 gives maximum product value.

Example 2:
Input:
Nums = [1,2,-3,0,-4,-5]
Output:

 20
Explanation:

 In the given array, we can see (-4)×(-5) gives maximum product value.

'''

nums = [1,2,3,4,5,0]
def maximum_product_value(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            current_product = 1
            for k in range(i, j+1):
                current_product *= arr[k]
                result = max(current_product, result)
    return result

print("---Maximum Product Value : ", maximum_product_value(nums))