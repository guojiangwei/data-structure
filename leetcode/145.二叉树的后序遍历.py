#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1 32ms 88.26% 12.7
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.res = [ ]
    #     self.helper(root)
    #     return self.res
    # def helper(self,node):
    #     if node:
    #         self.helper(node.left)
    #         self.helper(node.right)
    #         self.res.append(node.val)
# solution 2 36ms 73% 12.5
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while  stack :
            node = stack.pop()
            if node:
                if type(node) is int:
                    res.append(node)
                else:
                    stack.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
        return res



        
# @lc code=end

