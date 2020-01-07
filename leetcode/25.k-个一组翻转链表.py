#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = ListNode(-1)
        cur ,head ,stack = head, p ,[]
        less_k = False
        while cur :
            for i in range(k):
                if cur :
                    stack.append(cur)
                    cur = cur.next
                else:
                    less_k = True
            if not less_k:
                for i in range(k):
                    p.next = stack.pop() 
                    p = p.next
        for i in range(len(stack)):
            p.next = stack[i]
            p = p.next
        
        if len(stack) ==0 :
            p.next = None
        return head.next
        
# @lc code=end

