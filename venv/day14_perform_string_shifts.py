"""day14_perform_string_shifts.py
    Created by Aaron at 14-Apr-20"""
from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # app1
        # for x in range(len(shift)):
        #     if shift[x][0]==0:
        #         s=s[shift[x][1]:]+s[:shift[x][1]]
        #     elif shift[x][0]==1:
        #         s=s[-shift[x][1]:]+s[:-shift[x][1]]
        # return s

        # app2
        move=0
        for x,y in shift:
            if x== 0:
                move-=y
            else:
                move+=y
        move %=len(s)               #interesting idea
        return s[-move:]+s[:-move]

run=Solution()
a='abc'
b=[[0,1],[1,2]]
# b=[[1,1],[0,3]]
print(run.stringShift(a, b))
# app1 substring processes by modifying the string
# app2 have pointer to calculate movement and only return with substring without modfying