"""day2_happy_number.py
    Created by Aaron at 02-Apr-20"""
class Solution:
    def check(self, n: int) -> int:
        sum = 0
        while n:
            sum += (n%10)**2
            n = int(n/10)
        return sum

    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            if n == 1:
                return True
            n = self.check(n)
            if n in s:
                return False
            else:
                s.add(n)
run=Solution()
a=19
print(run.isHappy(a))
# keep repeating the same maths until the appeared number reappear then false