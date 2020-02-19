#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1 44ms 89.4% 14.9MB
    # def maxDepth(self, root: TreeNode) -> int:
    #     def helper(root):
    #         if root:
    #             l_deep = helper(root.left)
    #             r_deep = helper(root.right)

    #             return max(l_deep,r_deep)+1
    #         else:
    #             return 0
    #     return helper(root)
    def maxDepth(self, root: TreeNode) -> int:
        deepth = 0
        stack = [(1,root)]
        while len(stack) > 0:
            curr_deepth,node = stack.pop()
            if node is not None :
                deepth = max(deepth,curr_deepth)
                stack.append((deepth+1,root.left))
                stack.append((deepth+1,root.right))
        return deepth


        
# @lc code=end

