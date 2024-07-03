'''
Problem statement
You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.

Note:

You can not sell without buying first.
For Example:
For the given array [ 2, 100, 150, 120],
The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs. 150.
So, the output will be 148.

Sample Input :
arr = [1, 2, 3, 4]

arr =[2, 2, 2, 2]

Sample Output 1:
3
0

'''
def maxprofit(arr):
    max_profit = 0
    mini = arr[0]
    for i, value in enumerate(arr):
        cost = arr[i] - mini
        max_profit = max(max_profit, cost)
        mini = min(mini, arr[i])
    return max_profit

arr = [3, 2, 3, 4, 1, 8]
res = maxprofit(arr)
print(" -------------------------- res : ", res)

