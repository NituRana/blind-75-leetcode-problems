'''

Code
Testcase
Test Result
Test Result
371. Sum of Two Integers
Medium
Topics
Companies
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5


'''

def add(a, b):
    if b == 0:
        return a
    else:
        sum_without_carry = a ^ b
        carry = (a & b) << 1
        return add(sum_without_carry, carry)

a = 15
b = 5
print("----------------", add(a, b))