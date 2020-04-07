"""day7_counting_elements.py
    Created by Aaron at 07-Apr-20"""
from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        # app1
        # count=0
        # for x in arr:
        #     if x+1 in arr:
        #         count+=1
        # return count

        # return len([1 for x in range(len(arr)) if arr[x]+1 in arr ])

        # return sum([1 for x in range(len(arr)) if arr[x]+1 in arr ])

        # app2
        s=set(arr)
        count=0
        for x in arr:
            if x+1 in s:
                count+=1
        return count

run=Solution()
a=[1,3,2,3,5,0]
a=[1,1,2,2]
print(run.countElements(a))
# find the element x+1, if exist then just increment counter
# app1 find element O(n^2)
# app2 using set find O(n)