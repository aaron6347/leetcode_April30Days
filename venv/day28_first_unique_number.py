"""day28_first_unique_number.py
    Created by Aaron at 28-Apr-20"""
from typing import List
from collections import OrderedDict
import itertools
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.uni=OrderedDict()
        self.non={}
        for x in nums:
            if x not in self.non and x not in self.uni:
                self.uni[x]=x
            elif x in self.uni and x not in self.non:
                self.uni.pop(x)
                self.non[x]=x

    def showFirstUnique(self) -> int:
        if len(self.uni)>0:
            return next(iter(self.uni))
        return -1

    def add(self, value: int) -> None:
        if value not in self.non and value not in self.uni:
            self.uni[value]=value
        elif value in self.uni and value not in self.non:
            self.uni.pop(value)
            self.non[value]=value

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
a,b=["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"],\
    [[[2,3,5]],[],[5],[],[2],[],[3],[]]
run=FirstUnique(*b[0])
copy=[]
for x in b:
    s=str(*x)
    copy.append(s)
result=[None]*1
for x in range(1, len(copy)):
    if copy[x]=='':
        result.append(eval("run.{0}()".format(a[x])))
    else:
        result.append(eval("run.{0}({1})".format(a[x], int(copy[x]))))
print(result)
# orderedDict for get unique, dictionary for non unique, when adding check, when show straight first element of orderedDict time O(1) space O(n)