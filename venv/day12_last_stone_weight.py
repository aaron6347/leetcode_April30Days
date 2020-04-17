"""day12_last_stone_weight.py
    Created by Aaron at 12-Apr-20"""
from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # app1
        # while len(stones)>1:
        #     stones.sort(reverse=True)
        #     if stones[0]>stones[1]:
        #         stones[0]=stones[0]-stones[1]
        #         del stones[1]
        #     elif stones[0]==stones[1]:
        #         del stones[1]
        #         del stones[0]
        #         continue
        # return 0 if len(stones)==0 else stones[0]

        # app2
        l=[-x for x in stones]
        heapq.heapify(l)
        while len(l)>1:
            heapq.heappush(l, heapq.heappop(l)-heapq.heappop(l))
        return -l[0]

run=Solution()
a=[2,7,4,1,8,1]
print(run.lastStoneWeight(a))
# app1 sort everytime after operation, so that we can use first and second max element to find difference
# app2 heap priority queue