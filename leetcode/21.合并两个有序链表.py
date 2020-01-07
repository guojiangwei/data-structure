#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # solution 1 loop
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     p = ListNode(-1)
    #     head = p
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             p.next = l1
    #             l1 = l1.next
    #         else:
    #             p.next = l2
    #             l2 = l2.next
    #         p = p.next
    #     while l1:
    #         p.next = l1
    #         l1=l1.next
    #         p = p.next
    #     while l2:
    #         p.next = l2
    #         p = p.next
    #         l2 = l2.next
    #     return head.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2 :
            if l1.val > l2.val :
                l1,l2 = l2,l1
            l1.next=self.mergeTwoLists(l1.next,l2)

        return l1 or l2
        
# @lc code=end

