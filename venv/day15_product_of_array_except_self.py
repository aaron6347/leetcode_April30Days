"""day15_product_of_array_except_self.py
    Created by Aaron at 15-Apr-20"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # app1
        # L, R= [0] * len(nums), [0] * len(nums)
        # L[0] = 1
        # for i in range(1, len(nums)):
        #     L[i] = nums[i - 1] * L[i - 1]
        # R[len(nums) - 1] = 1
        # for i in reversed(range(len(nums) - 1)):
        #     R[i] = nums[i + 1] * R[i + 1]
        # return [L[i] * R[i] for i in range(len(nums))]

        # app2
        answer = [0] * len(nums)
        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1;
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer

run=Solution()
a=[1,2,3,4]
print(run.productExceptSelf(a))
# app1 seperate left and right side and then only multiply, dp solution O(n) time and space
# app2 instead of using left list, use result list as left O(n) time and O(1) space