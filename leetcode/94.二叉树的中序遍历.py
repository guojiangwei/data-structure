#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        # solution 1 24ms 99.15%  12.7MB
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         self.inorderTraversal(root.left)
    #         self.res.append(root.val)
    #         self.inorderTraversal(root.right)
    #     return self.res
# solution2 32ms 87.12%  12.7
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
    
        while root or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.res.append(root.val)
            root = root.right
        return self.res

        
# @lc code=end

