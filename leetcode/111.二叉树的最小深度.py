#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1  44ms 95% 14.5
    # def minDepth(self, root: TreeNode) -> int:
    #     # if root is None:
    #     #     return 0
    #     if root is None:
    #         return 0

    #     if root.left is None and root.right is None:
    #         return 1
        
    #     l_min = float('inf')
    #     r_min = float('inf')
    #     if root.left is not None:
    #         l_min = self.minDepth(root.left)
    #     if root.right is not None:
    #         r_min = self.minDepth(root.right)

    #     return min(l_min,r_min) +1
# solution 2  48ms 87% 14.6MB
     def minDepth(self, root: TreeNode) -> int:
        # if root is None:
        #     return 0
        if root is None:
            return 0
        children = [root.left,root.right]
        if not any(children):
            return 1
        
        min_deepth = float('inf')
        for c in children:
            if c:
                min_deepth = min(self.minDepth(c),min_deepth)
        return min_deepth +1

        
# @lc code=end

