#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # solution1 recurision
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     if head is None or head.next is None:
    #         return head
    #     temp = head.next
    #     #  temp.next
    #     # head.next = temp.next
        
    #     # head.next = temp.next
    #     head.next = self.swapPairs(head.next.next)
    #     temp.next = head
    #     return temp

    # loop
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     p = ListNode(-1)
    #     a,b,p.next,tmp = p,p,head,p
    #     while b.next  and b.next.next:
    #         a,b = a.next,b.next.next

    #         tmp.next,a.next,b.next = b,b.next,a
    #         tmp,b = a,a

    #     return p.next

        # stack
    def swapPairs(self, head: ListNode) -> ListNode:
        p = ListNode(-1)
        cur,head,stack = head,p,[]
        while cur  and cur.next:
            _,_=stack.append(cur),stack.append(cur.next)

            cur = cur.next.next
            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next
        
        if cur:
            p.next = cur
        else:
            p.next = None

        return head.next

        
# @lc code=end

