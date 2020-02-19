#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution1 60ms 50.59% 15.3MB
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def helper(node):
    #         if node and self.is_sorted:
                
    #             helper(node.left)
    #             if(0 < len(self.res) and node.val <= self.res[-1]):
    #                 self.is_sorted =  False
    #             self.res.append(node.val)
    #             helper(node.right)
    #     self.is_sorted = True
    #     self.res = []
    #     helper(root)
    #     return self.is_sorted
    # solution 2 48ms 86.8% 15.6MB
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return True
    #     def helper(node):
    #         if node and self.is_sorted:
                
    #             helper(node.left)
    #             if( node.val <= self.res):
    #                 self.is_sorted =  False
    #             self.res = node.val
    #             helper(node.right)
    #     def get_min(node):
    #         while node.left  is not None:
    #             node = node.left
    #         self.res = node.val - 1

    #     self.is_sorted = True
    #     get_min(root)
    #     helper(root)
    #     return self.is_sorted
# solution3 36ms 99.67% 15.4MB
      def isValidBST(self, root: TreeNode) -> bool:
        # if root is None:
        #     return True
        def helper(node):
            if node and self.is_sorted:
                
                helper(node.left)
                if( node.val <= self.res):
                    self.is_sorted =  False
                self.res = node.val
                helper(node.right)

        self.is_sorted = True
        self.res = float('-inf')
        helper(root)
        return self.is_sorted
    
            

        
# @lc code=end

