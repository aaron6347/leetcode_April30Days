"""day24_lru_cache.py
    Created by Aaron at 24-Apr-20"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        else:
            self.lru.move_to_end(key)
            return self.lru[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.pop(key)
        self.lru[key] = value
        if len(self.lru) > self.cap:
            self.lru.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
a,b=["LRUCache","put","put","get","put","get","put","get","get","get"],[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
run=LRUCache(*b[0])
result=[]
for x in range(1, len(b)):
    try:
        i,j=b[x]
        result.append(eval("run.{0}({1},{2})".format(a[x], i, j)))
    except ValueError:
        i=b[x][0]
        result.append(eval("run.{0}({1})".format(a[x], i)))
print(result)
# get and put will affect order of LRU and need to aware of replacing same key that might exist in LRU