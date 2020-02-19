#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1  56ms 98.7% 17MB
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left = 0,in_right = len(inorder)):
            nonlocal pre_idx
            if in_left == in_right:
                return None
            
            node_val = preorder[pre_idx]
            node = TreeNode(node_val)

            index = idx_map[node_val]
            pre_idx +=1
            node.left = helper(in_left,index)
            node.right = helper(index+1, in_right)

            return node
        
        pre_idx = 0
        idx_map = {val:idx for idx , val in enumerate(inorder)}
        return helper()
        

        
# @lc code=end

