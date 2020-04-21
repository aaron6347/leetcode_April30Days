"""day21_leftmost_column_with_at_least_a_one.py
    Created by Aaron at 21-Apr-20"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
import math
class BinaryMatrix(object):
    def __init__(self, list):
        self.ar=list
    def get(self, x: int, y: int) -> int:
        return self.ar[x][y]
    def dimensions(self):
        return list((len(self.ar),len(self.ar[0])))

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # app1
        # d = binaryMatrix.dimensions()
        # i, j = 0, d[1] - 1
        # best = 10000
        # while i < d[0]:
        #     start, end, cur=0,j, 10000
        #     while start <= j and end >= 0 and start <= end:
        #         mid = int(math.ceil((end + start) / 2))
        #         if binaryMatrix.get(i, mid) == 0:
        #             start = mid + 1
        #         else:
        #             cur = min(cur, mid)
        #             end = mid - 1
        #     best = min(best, cur)
        #     i += 1
        # if best == 10000:
        #     return -1
        # return best

        # app2
        d=binaryMatrix.dimensions()
        i,j=0,d[1]-1
        ans=-1
        while j>=0 and i<d[0]:
            if binaryMatrix.get(i,j)==0:
                i+=1
            else:
                ans=j
                j-=1
        return ans

run=Solution()
a=[[0,0,1,1,1,1,1],[0,1,1,1,1,1,1],[0,0,0,1,1,1,1],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,1,1],[0,0,0,1,1,1,1]]
run2=BinaryMatrix(a)
print(run.leftMostColumnWithOne(run2))
# app1 binary search O(n*(m/2)+1)
# app2 approach by top right, if 0 go lower if 1 go left O(n+m)