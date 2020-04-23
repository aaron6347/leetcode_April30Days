"""day23_bitwise_AND_of_numbers_range.py
    Created by Aaron at 23-Apr-20"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # app1
        # i = 0
        # while m != n:
        #     m >>= 1
        #     n >>= 1
        #     i += 1
        #     print(m, n, i)
        # return n << i

        # app2
        return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if m != n else m

run=Solution()
a,b=13,15
print(run.rangeBitwiseAnd(a,b))
# app1 make use of bitshift to find the same last 1 in both numbers iteratively
# app2 make use of bitshift to find the same last 1 in both numbers recursively
