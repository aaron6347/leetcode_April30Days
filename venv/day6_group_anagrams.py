"""day6_group_anagrams.py
    Created by Aaron at 06-Apr-20"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # app1
        # result = {}
        # for i in strs:
        #     x = "".join(sorted(i))
        #     if x in result:
        #         result[x].append(i)
        #     else:
        #         result[x] = [i]
        # return list(result.values())

        # app1
        # d = {}
        # for w in strs:
        #     # key = sorted(w)             #unhashable
        #     # key = str(sorted(w))        #hashable
        #     # key = "".join(sorted(w))    #hashable
        #     key = tuple(sorted(w))      #hashable
        #     # print(type(key))
        #     d[key] = d.get(key, []) + [w]
        # return list(d.values())

        #app2
        ans={}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)]=ans.get(tuple(count),[])+[s]
        return list(ans.values())

run=Solution()
a=["eat","tea","tan","ate","nat","bat"]
print(run.groupAnagrams(a))
# app1 sorted string
# app2 counting alphabet
# anagrams has canonical form which is similarities with same len, same count of letter and same arrangement of alpha
# using dict, key must be immutable/ hashable such as str, int, tuple; mutable are sets, list