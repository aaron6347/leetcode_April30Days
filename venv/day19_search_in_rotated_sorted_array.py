"""day19_search_in_rotated_sorted_array.py
    Created by Aaron at 19-Apr-20"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end=0, len(nums)
        while start<end:
            middle= (start+end)//2
            if  (nums[middle] < nums[0]) == ( target < nums[0]):
                if target==nums[middle]:
                    return middle
                elif target>nums[middle]:
                    start=middle+1
                else:
                    end=middle
            elif nums[0]<= target:
                end=middle
            else:
                start=middle+1
        return -1

run=Solution()
a,b=[4,5,6,7,0,1,2], 2
# a,b=[1,3], 3
print(run.search(a,b))
# using binary search with 3 pointer start, end, middle, viewing whole list as a list or 2 list,
# always use start and end as to indicate the range of target and use middle to determine lower or greater