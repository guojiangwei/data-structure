#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
# solution 1 168ms 59% 33MB
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root:
            queue =  [root]
        else : return '[]'
        res = [root.val]
        while queue:
            node = queue.pop(0)
            if node.left :
                res.append(node.left.val)
                queue.append(node.left)
            else:
                res.append(None)
            if node.right :
                res.append(node.right.val)
                queue.append(node.right)
            else:
                res.append(None)
        return str(res)




        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = eval(data)
        
        if len(data_list) == 0:
            return None
        head = TreeNode(data_list[0])
        queue  = [head]
        # p = head
        i = 1
        while queue:
            p = queue.pop(0)
            if data_list[i] is not None:
                node = TreeNode(data_list[i])
                p.left = node
                queue.append(node)
            i +=1
            if data_list[i] is not None:
                node = TreeNode(data_list[i])
                p.right = node
                queue.append(node)
            i +=1
        return head
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

if __name__ == "__main__":
    codec = Codec()
    head = TreeNode(1)
    node = TreeNode(2)
    head.left = node
    node = TreeNode(3)
    head.right = node
    cnode = TreeNode(4)
    node.left = cnode
    cnode = TreeNode(5)
    node.right = cnode
    stree = codec.serialize(head)
    print(stree)
    print(codec.serialize(codec.deserialize(stree)))
