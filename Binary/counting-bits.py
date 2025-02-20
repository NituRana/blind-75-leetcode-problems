'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

'''

# Approach:
# Count the no of set bits in each number from 0 to n and store the set bits count for each number in the array and return the array.
# n = 6 
# def countingSetBits(n):
#     ans = []
#     for i in range(0, n+1):
#         num = i
#         cnt = 0
#         while num > 0:
#             if num & 1:
#                 cnt += 1
#             num = num >> 1
#         ans.append(cnt)
#     return ans

# ans = countingSetBits(n)
# print("=============== ans :", ans)

#Optimal approach :
n = 6

def countingSetBits(n):
    ans = [0]*(n+1)
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    ans[0] = 0
    ans[1] = 1
    for i in range(0, n+1):
        if i & 1:
            ans[i] = ans[i//2] + 1
        else:
            ans[i] = ans[i//2]
    return ans


ans = countingSetBits(n)
print("----------------- ans :", ans)