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
# [2,2,1]