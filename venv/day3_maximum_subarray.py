"""day3_maximum_subarray.py
    Created by Aaron at 03-Apr-20"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=maxx=0
        for x in range(len(nums)):
            current+=nums[x]
            if current > maxx:
                maxx=current
            if current<0:
                current=0
        return maxx

run=Solution()
a=[-2,1,-3,4,-1,2,1,-5,4]
# a=[2,0,-3,2,1,0,1,-2]
print(run.maxSubArray(a))
# O(n) Kadane algo