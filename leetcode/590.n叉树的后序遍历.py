#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
        # solution 1 88ms 55%  14.7
    # def postorder(self, root: 'Node') -> List[int]:
    #     self.helper(root)
    #     return self.res
    # def helper(self,node):
    #     if node:
    #         p = node
    #         for p in node.children:
    #             self.helper(p)
    #             # p = p.children
    #         self.res.append(node.val)
    # solution 2 104ms 51.16% 14.6
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]

        while stack :
            node = stack.pop()
            if node is not None:
                if type(node) is int:
                    self.res.append(node)
                else:
                    stack.append(node.val)
                    for i in range(len(node.children)-1,-1,-1):
                        stack.append(node.children[i])
        return self.res

        
# @lc code=end

