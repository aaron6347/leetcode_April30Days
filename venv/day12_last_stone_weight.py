"""day12_last_stone_weight.py
    Created by Aaron at 12-Apr-20"""
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # app1
        while len(stones)>1:
            stones.sort(reverse=True)
            if stones[0]>stones[1]:
                stones[0]=stones[0]-stones[1]
                del stones[1]
            elif stones[0]==stones[1]:
                del stones[1]
                del stones[0]
                continue
        return 0 if len(stones)==0 else stones[0]

run=Solution()
a=[2,7,4,1,8,1]
print(run.lastStoneWeight(a))
# sort everytime after operation, so that we can use first and second max element to find difference