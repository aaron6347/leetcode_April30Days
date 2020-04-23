"""day11_diameter_of_binary_tree.py
    Created by Aaron at 11-Apr-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, root, n, middle, times):
        if times > 0:
            if n <= middle:
                self.left.insert(root, n, middle - 2, times - 1)
            else:
                self.right.insert(root, n, middle + 2, times - 1)
        else:
            if n % 2 == 1:
                self.left = TreeNode(root)
            elif n % 2 == 0:
                self.right = TreeNode(root)


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans =0
        def depth(node):
            if not node: return 0
            if node.val==None: return 0     # for pycharm
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1
        depth(root)
        return self.ans

run = Solution()
a=[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
# fill then become
# [4,-7,-3,None,None,-9,-3,None,None,None,None,9,-7,-4,None,None,None,None,None,None,None,None,None,6,None,-6,-6,
# None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0,6,None,None,
# 5,None,9,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
# None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,-4,None,
# None,None,None,None,None,None,None,None,-2,]
copy=a  # fill in missing None into list
i=0
while i<len(a):
    if all ( y is None for y in a[i:-1]):
        break
    if a[i]==None:
        copy.insert(i * 2 + 1, None)
        copy.insert(i * 2 + 2, None)
    i+=1
    a=copy
for x in range(len(a)-1, -1,-1):    # cutting the extra None at the end list
    if a[x]!=None:
        i=x
        break
a=a[:i+1]
node = TreeNode(a[0])
bi=[2,4,8,16,32,64] # symmetry binary tree
for x in range(1, len(a)):
    sum=0
    for y in range(len(bi)):
        sum+=bi[y]
        if x<=sum:
            node.insert(a[x], x, sum-bi[y]+(bi[y]/2), y)
            break
print(run.diameterOfBinaryTree(node))
# depth first search, left then right, compare the max of left and right, if no more left or right return 0