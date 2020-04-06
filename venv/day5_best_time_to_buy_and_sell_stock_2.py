"""day5_best_time_to_buy_and_sell_stock_2.py
    Created by Aaron at 05-Apr-20"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # app1
        # total=current=0; nex=1
        # while current<len(prices) and nex<len(prices):
        #     if prices[current] < prices[nex]:
        #         while nex!=len(prices)-1:
        #             if prices[nex]< prices[nex+1]:
        #                 nex+=1
        #             else:
        #                 total+=prices[nex]-prices[current]
        #                 break
        #         if nex==len(prices)-1:
        #             total += prices[nex] - prices[current]
        #         current = nex + 1
        #         nex = current + 1
        #     else:
        #         current=nex
        #         nex=current+1
        # return total

        # app2
        # total=0
        # for x in range(len(prices)-1):
        #     if prices[x]< prices[x+1]:
        #         total+=prices[x+1]-prices[x]
        # return total

        # app3
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))

run=Solution()
# a=[1,2,3,4,5]
# a=[7,1,5,3,6,4]
a=[7,6,4,3,1]
print(run.maxProfit(a))
# app1 brute
# app2 cumulative
# app3 max comparison, buy->sell&buy->sell to buy->sell