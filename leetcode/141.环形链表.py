#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # solution 1 set
    # def hasCycle(self, head: ListNode) -> bool:
    #     # if not head :
    #     #     return True
    #     node_set = set()
    #     # node_set.add(head)
        
    #     while head :
    #         if head in node_set:
    #            return True
    #         node_set.add(head)
    #         head = head.next
    #     # len(node_set)
    #     return False

    def hasCycle(self, head: ListNode) -> bool:
        # if not head :
        #     return True
        node_set = {}
        # node_set.add(head)
        
        while head :
            if head in node_set:
               return True
            node_set[head] = 1
            head = head.next
        # len(node_set)
        return False
# @lc code=end

