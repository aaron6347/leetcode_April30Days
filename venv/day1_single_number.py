"""day1_single_number.py
    Created by Aaron at 01-Apr-20"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for a in nums:
            x^=a
        return x
run=Solution()
a=[2,2,1]
print(run.singleNumber(a))
# using XOR in eliminating a pair of number that will leave single number out