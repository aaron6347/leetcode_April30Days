"""day18_minimum_path_sum.py
    Created by Aaron at 18-Apr-20"""
from typing import List
class Solution:
    def minPathSum(self, grid):
        # app1
        # if len(grid) == 0 or len(grid[0]) == 0:
        #     return 0
        # m = len(grid)
        # n = len(grid[0])
        # for i in range(1, n):
        #     grid[0][i] += grid[0][i - 1]
        # for i in range(1, m):
        #     grid[i][0] += grid[i - 1][0]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        # return grid[-1][-1]

        # app2
        # if len(grid) == 0 or len(grid[0]) == 0:
        #     return 0
        # M, N = len(grid), len(grid[0])
        # dp = [0] + [1000] * (N-1)
        # for i in range(M):
        #     dp[0] = dp[0] + grid[i][0]
        #     for j in range(1, N):
        #         dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        # return dp[-1]

        # app3
        if len(grid)==0 or len(grid[0])==0:
            return 0
        r, c = len(grid), len(grid[0])
        pre = cur = [0] * c
        pre[0] = grid[0][0]
        for i in range(1, c):
            pre[i] = pre[i - 1] + grid[0][i]
        for i in range(1, r):
            cur[0] = pre[0] + grid[i][0]
            for j in range(1, c):
                cur[j] = min(cur[j - 1], pre[j]) + grid[i][j]
            pre = cur
        return cur[-1]

run=Solution()
a=[[1,3,1],[1,5,1],[4,2,1]]
print(run.minPathSum(a))
# app1 modify the list into cumulative by first doing all 1st row and leftest element where there is only 1 choice to go
# and then others element will choosing the smallest combo O(m*n) space
# app2 same method but with different code O(m*n) space
# app3 using two pointer to point at 1st list, set up prev and to be use in current O(n)