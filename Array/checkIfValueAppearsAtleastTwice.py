'''

Problem Statement: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true.
Explanation: 1 appeared two times in the input array.

'''

def is_duplicate_ele_exist(arr):
    for i in range (0, len(arr)):
        for j in range (i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return "all the array elements are identical"

arr = [4, 3, 5, 1, 0, 9]
res = is_duplicate_ele_exist(arr)
print("--------------- res :", res)