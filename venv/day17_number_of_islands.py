"""day17_number_of_islands.py
    Created by Aaron at 17-Apr-20"""
from typing import List
class Solution:
    # app1
    # def dfs(self, grid, x, y):
    #     if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]!='1':
    #         return
    #     grid[x][y]='@'
    #     self.dfs(grid, x+1,y)
    #     self.dfs(grid, x-1,y)
    #     self.dfs(grid, x,y+1)
    #     self.dfs(grid, x,y-1)
    #
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #     count=0
    #     for x in range(len(grid)):
    #         for y in range(len(grid[0])):
    #             if grid[x][y]=='1':
    #                 self.dfs(grid,x,y)
    #                 count+=1
    #     return count

    # app2
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

run=Solution()
a=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# a=[["1"]]
print(run.numIslands(a))
# app1 normal dfs with recursive
# app2 dfs with recursive and ingenious map 2 iterables