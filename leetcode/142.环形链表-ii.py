#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node_dict = {}
        # i = 0
        while head :
            if head in node_dict :
                return head
            node_dict[head] = 1
            head = head.next
        return  None
        
# @lc code=end

