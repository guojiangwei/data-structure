#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # solution 1 loop
    # def reverseList(self, head: ListNode) -> ListNode:
    #     cur=head
    #     pre = None
    #     while cur :
            
    #         temp = cur.next
    #         cur.next = pre
    #         pre=cur
    #         cur = temp
    #     return pre
# solution 2 recurision
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        cur=self.reverseList(head.next)
        head.next.next=head
        head.next = None
        return cur
        
        

        
# @lc code=end

