"""day27_maximal_square.py
    Created by Aaron at 27-Apr-20"""
from typing import List
class Solution:
   def maximalSquare(self, matrix: List[List[str]]) -> int:
       # app1
       # if len(matrix) == 0: return 0
       # i, j = len(matrix), len(matrix[0])
       # prefix = [[int(matrix[x][y]) for y in range(j)] for x in range(i)]
       # mx = max(max(prefix))
       # for x in range(1, i):
       #     for y in range(1, j):
       #         if matrix[x][y] == '1':
       #             prefix[x][y] = min(prefix[x - 1][y - 1], prefix[x - 1][y], prefix[x][y - 1]) + 1
       #             mx = max(mx, prefix[x][y])
       # return mx ** 2

       # app2
       # if not matrix:
       #     return 0
       # r, c = len(matrix), len(matrix[0])
       # pre = cur = [0] * (c + 1)
       # res = 0
       # for i in xrange(r):
       #     for j in xrange(c):
       #         cur[j + 1] = (min(pre[j], pre[j + 1], cur[j]) + 1) * int(matrix[i][j])
       #         res = max(res, cur[j + 1] ** 2)
       #     pre = cur
       #     cur = [0] * (c + 1)
       # return res

       # app3
       if len(matrix) == 0:
           return 0
       for i, r in enumerate(matrix):
           print(i,r)
           r = matrix[i] = list(map(int, r))
           print(r)
           for j, c in enumerate(r):
               if i * j * c:
                   r[j] = min(matrix[i - 1][j], r[j - 1], matrix[i - 1][j - 1]) + 1
       return max(list(map(max, matrix+ [[0]]))) ** 2

run=Solution()
a=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(run.maximalSquare(a))
# app1 dp with 1st row and 1st column element as prefix, if the diagonally is 1 then investigate the three parts, dp time O(n*m) space O(n*m)
# app2 similar with app1, but using 1d list as row and exchange after each iterate, dp time O(n*m) space (2m)
# app3 similar with app1 but using map and enum to execute faster