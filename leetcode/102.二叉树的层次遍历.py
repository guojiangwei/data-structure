#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution 1 30ms 95.84% 13.6MB
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if root is None:
    #         return []
    #     level_queue = []
    #     queue = [root]
    #     cur = root
    #     res = [[]]
    #     while queue :
    #         cur = queue.pop(0)
    #         res[-1].append(cur.val)
            
    #         if cur.left :
    #             level_queue.append(cur.left)
    #         if cur.right:
    #             level_queue.append(cur.right)
            
    #         if len(queue) == 0 and len(level_queue) != 0:
    #             queue = level_queue[:]
    #             level_queue = []
    #             res.append([])
    #     return res
    # solution2 36ms 89% 13.7
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     def helper(node,level = 0):
    #         if node :
    #             if len(res) == level:
    #                 res.append([]) 
    #             res[level].append(node.val)
    #             helper(node.left,level + 1)
    #             helper(node.right,level + 1)
    #     res = []
    #     # tmp = []
    #     helper(root)
    #     return res
    # solution3 32ms 96% 13.4MB
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]

        while queue :
            res.append([])
            level_len = len(queue)
            for i in range(level_len):
                cur = queue.pop(0)   
                res[-1].append(cur.val)
                if cur.left :
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res     
# @lc code=end

