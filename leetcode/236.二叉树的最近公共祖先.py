#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # # solution1 120ms 18% 25.7 80ms  83% 25.6
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     self.ans = None
    #     def helper(node):
    #         if node :
                
    #             left = helper(node.left)
    #             right = helper(node.right)

    #             mid = node == p or node == q

    #             if mid + left +right >=2:
    #                 self.ans = node
    #             return mid or left or right
    #         return False

    #     helper(root)
    #     return  self.ans

    #  solution 2  80ms  83% 25.6
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def helper(node) :
            if node and self.ans is None:
                
                left = helper(node.left)
                right = helper(node.right)

                mid = node == p or node == q

                if mid + left +right >=2:
                    self.ans = node
                return mid or left or right
            return False

        helper(root)
        return  self.ans

        
# @lc code=end

