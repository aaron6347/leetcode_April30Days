"""day9_backspace_string_compare.py
    Created by Aaron at 09-Apr-20"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # app1
        x=0
        a=b=''
        while x<len(S) or x<len(T):
            if x<len(S):
               if S[x]=='#':
                   a=a[:-1]
               else:
                   a+=S[x]
            if x<len(T):
               if T[x]=='#':
                   b=b[:-1]
               else:
                   b+=T[x]
            x+=1
        return a==b

        # app2
        # x=y=0
        # while x<len(S):
        #     if S[x]=='#':
        #         if x!=0:
        #             S=S[:x-1]+S[x+1:]
        #             x-=2
        #         else:
        #             S=S[x+1:]
        #             x-=1
        #     x+=1
        # while y<len(T):
        #     if T[y]=='#':
        #         if y!=0:
        #             T=T[:y-1]+T[y+1:]
        #             y-=2
        #         else:
        #             T=T[y+1:]
        #             y-=1
        #     y += 1
        # return S==T

        # app3
        # x,y=len(S)-1,len(T)-1
        # skipa = skipb = 0
        # while True:
        #     while x>=0 and (skipa or S[x]=='#'):
        #         skipa+=1 if S[x]=='#' else -1
        #         x-=1
        #     while y>=0 and (skipb or T[y]=='#'):
        #         skipb+=1 if T[y]=='#' else -1
        #         y-=1
        #     print(S[x], T[y])
        #     if not (x>=0 and y>=0 and S[x]==T[y]):
        #         return x==y== -1
        #     x-=1;y-=1

run=Solution()
a,b="ab#c","ade##c"
# a,b="a##c","#a#c"
print(run.backspaceCompare(a,b))
# app1 front traverse with 2 new string
# app2 front traverse without new string
# app3 back traverse without modfying