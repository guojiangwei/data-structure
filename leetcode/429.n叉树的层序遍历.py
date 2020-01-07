#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.res = []
        # solution 1 48ms 98.56% 14.5
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     self.helper(root,0)
    #     return self.res
    # def helper(self,node,level):
    #     if node is not None:
    #         if len(self.res) == level:
    #             self.res.append([])
    #             self.res[level].append(node.val)
    #         else:
    #             self.res[level].append(node.val)
    #         for p in node.children:
    #             self.helper(p,level+1)
    # solution2 92ms 64.99% 14.3
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return self.res
        prev_layer = [root]
        while prev_layer:
            current_layer = []
            self.res.append([])
            for  node in prev_layer:
                self.res[-1].append(node.val)
                current_layer.extend(node.children)
            prev_layer = current_layer
        return self.res

                



        
# @lc code=end

