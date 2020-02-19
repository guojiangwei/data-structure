#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1 28ms 95.14% 12.7
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            tmp = root.right
            root.right = root.left
            root.left = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        
# @lc code=end

