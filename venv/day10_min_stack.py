"""day10_min_stack.py
    Created by Aaron at 10-Apr-20"""
class MinStack:
    # app1
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.ar = []
    # def push(self, x: int) -> None:
    #     self.ar.append(x)
    # def pop(self) -> None:
    #     self.ar.pop()
    # def top(self) -> int:
    #     return self.ar[-1]
    # def getMin(self) -> int:
    #     return min(self.ar)

    # app2
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ar = []
    def push(self, x: int) -> None:
        min = self.getMin()
        if min == None or min > x:
            min = x
        self.ar.append((x, min))
    def pop(self) -> None:
        self.ar.pop()
    def top(self) -> int:
        if len(self.ar) == 0:
            return None
        return self.ar[-1][0]
    def getMin(self) -> int:
        if len(self.ar) == 0:
            return None
        return self.ar[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

a=["MinStack","push","push","push","getMin","pop","top","getMin"]
b=[[None],[-2],[0],[-3],[None],[None],[None],[None]]
run=MinStack()
x=1
ar=[]
while x<len(a):
    if b[x][0]!= None:
        ar.append(eval('run.{0}({1})'.format(a[x], b[x][0])))
    else:
        ar.append(eval('run.{0}()'.format(a[x])))
    x+=1
print(ar)
# app1 using list with min O(n k)
# app2 using tuple in list O(n)