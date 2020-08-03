'''
Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==1: return 0
        not_hold, hold, cool_down = 0, float('-inf'), float('-inf')
        for p in prices:
            not_hold,hold,cool_down = max(not_hold,cool_down),max(hold,not_hold-p),hold+p

        return max(not_hold,max(hold, cool_down))

#Runtime: 60 ms
#Memory Usage: 14.1 MB