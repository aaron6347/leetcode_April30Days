"""day26_longest_common_subsequence.py
    Created by Aaron at 26-Apr-20"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        L = [[None]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    L[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j] , L[i][j-1])
        return L[m][n]

run=Solution()
a,b="oxcpqrsvwf","shmtulqrypy"
print(run.longestCommonSubsequence(a,b))
# dp imagining it as a tree, comparing the last character, if same, both deleted, if not find max of which one character deleted