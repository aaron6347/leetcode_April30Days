"""day16_valid_parenthesis_string.py
    Created by Aaron at 16-Apr-20"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        findleft=0
        findright=0
        for x in s:
            findleft += 1 if x=='(' else -1
            findright += 1 if x!=')' else -1
            if findright < 0:
                break
            findleft=max(findleft, 0)
        return findleft==0

run=Solution()
a='(**())'
print(run.checkValidString(a))
# let ( and ) as +1 and -1 and * be both, if ( < 0 make it 0 again and if ) < 0 will be false