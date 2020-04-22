"""day22_subarray_sum_equals_k.py
    Created by Aaron at 22-Apr-20"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # app1
        # from collections import Counter
        # from itertools import accumulate
        #
        # total = 0
        # count = Counter()
        # count[0] += 1
        # for acc in accumulate(nums):
        #     total += count[acc - k]
        #     count[acc] += 1
        #     print(count)
        # return total

        # app2
        dic={0:1}
        count=sum=0
        for x in nums:
            sum+=x
            count+=dic.get(sum-k ,0)
            dic[sum]=dic.get(sum, 0)+1
        return count

run=Solution()
a, b=[1,1,0,1,-1],2
print(run.subarraySum(a, b))
# app1 use of accumulator and Counter from itertools and collection library, Counter using counting as arrange order not from insert order
# app2 cumulative - target to find if we have previous found the differences of target and insert current sum for future