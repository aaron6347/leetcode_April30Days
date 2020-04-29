"""day29_binary_tree_maximum_path_sum.py
    Created by Aaron at 29-Apr-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # insert by 1,2,4,8,16,32,64
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

    # print
    def printLevelOrder(self, root):
        h = self.height(root)
        ar = []
        for i in range(1, h + 1):
            self.printGivenLevel(root, i, ar)
        print(ar)

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printGivenLevel(self, root, level, ar):
        if root is None:
            ar.append(None)
            return
        if level == 1:
            ar.append((root.val))
        elif level > 1:
            self.printGivenLevel(root.left, level - 1, ar)
            self.printGivenLevel(root.right, level - 1, ar)

class Solution:
    # app1
    # def maxPathSum(self, root: TreeNode) -> int:
    #     def backtracking(node: TreeNode) -> tuple:
    #         if not node or node.val ==None: return float('-inf'), 0
    #         left_so_far, left_ending_here = backtracking(node.left)
    #         right_so_far, right_ending_here = backtracking(node.right)
    #         max_so_far = max(left_so_far, right_so_far,
    #                          node.val + left_ending_here + right_ending_here)
    #         max_ending_here = max(0, node.val + max(left_ending_here, right_ending_here))
    #         return max_so_far, max_ending_here
    #     return backtracking(root)[0]

    # app2
    def maxPathSum(self, root: TreeNode) -> int:
        self.globalmax = float("-inf")
        self.findmax(root)
        return self.globalmax

    def findmax(self, node):
        if not node or node.val==None:
            return 0
        left = self.findmax(node.left)
        right = self.findmax(node.right)
        if left < 0: left = 0
        if right < 0: right = 0
        self.globalmax = max(left + right + node.val, self.globalmax)
        return max(left, right) + node.val

run=Solution()
a=[-10,9,20,None,None,15,7]
copy=a
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
# node.printLevelOrder(node)
print(run.maxPathSum(node))
# app1 recursive, use tuple, examine if go left, go right, go both and determine the max with passing max in tuple
# app2 recursive, make use of global max and if left child or right child is <0 straight as 0