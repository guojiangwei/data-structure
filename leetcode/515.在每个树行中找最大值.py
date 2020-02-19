#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # solution1 bfs 40ms 98.67% 15.3MB
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if root is None : return res
        queue = [root]
        
        while queue:
            max_value = queue[0].val
            cur_len = len(queue)
            while cur_len:
                node = queue.pop(0)
                cur_len -=1
                if max_value < node.val:
                    max_value = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(max_value)
        return  res
            

        
# @lc code=end

