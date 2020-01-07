#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left= None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.res=[]
        # solution1 28ms 95.38% 12.8
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.helper(root)
    #     return self.res

    # def helper(self,node):
    #     if node:
    #         self.res.append(node.val)
    #         self.helper(node.left)
    #         self.helper(node.right)
    # solution2 28ms 95.38% 12.8
    def preorderTraversal(self, root: TreeNode) :
        stack = []
        while stack or root:
            # print(str(root.val)+"  ")
            while root is not None:
                self.res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root=root.right
        return self.res



# if __name__ == "__main__":
#     a = TreeNode(1)
#     a.right = TreeNode(2)
#     a.right.left = TreeNode(3)
#     so = Solution()
#     so.preorderTraversal(a)
#     print(so.res)


        
# @lc code=end


