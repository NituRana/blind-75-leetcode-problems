'''

Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

'''
# Brute force approach linear search: 

# def findMin(nums):
#     min_element = nums[0]
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             # if nums[j] < min_element:
#             #     min_element = nums[j]
#             min_element = min(min_element, nums[j])
#     return min_element
# arr = [4,5,6,7,0,1,2]
# print("------------------ minimum element :", findMin(arr))



# Using Binary Search Approach


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [5, 6, 7, 1, 2, 3, 4]
target = 3
print(search(nums, target)) 