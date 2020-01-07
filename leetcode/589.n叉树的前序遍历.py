#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.res = []
    def preorder(self, root: 'Node') -> List[int]:
        self.helper(root)
        return self.res
    def helper(self,node):
        if node is not None:
            self.res.append(node.val)
            for p in node.children:
                self.helper(p)
            

        
# @lc code=end

