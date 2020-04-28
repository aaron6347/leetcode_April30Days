"""day25_jump_game.py
    Created by Aaron at 25-Apr-20"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
       #  app1
       # last=len(nums)-1
       # for x in reversed(range(len(nums)-1)):
       #     if x+nums[x]>=last:
       #         last=x
       # return last == 0

       # app2
       mx = 0
       for i, n in enumerate(nums):
           if i > mx:
               return False
           mx = max(mx, i + n)
       return True

       # app3
       #  return reduce(lambda m, (i, n): max(m, i + n) * (i <= m), enumerate(nums, 1), 1) > 0

run=Solution()
# a=[5,9,3,2,1,0,2,3,3,1,0,0]
a=[3,2,1,0,4]
print(run.canJump(a))
# app1 start from last position, if any traverse can reach the last position change the last position, goal driven greedy dp O(n)
# app2 start from first position, if any traverse can reahc higher pos change the max position, data-driven greedy dp with enum O(n)
# app3 similar to app2 but using enum with lambda and tuple unpacking