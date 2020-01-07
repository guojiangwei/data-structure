#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    # solution 1 fatest
    # def isValid(self, s: str) -> bool:
    #     brackets_dict = {'}':'{',')':'(',']':'['}
    #     stack = []
    #     for c in s :
    #         if len(stack) == 0:
    #             stack.append(c)
    #             continue
    #         c2 = brackets_dict.get(c,None)
    #         if  c2 is None:
    #             stack.append(c)
               
    #         elif c2 == stack[-1]:
    #             stack.pop()
    #         else:
    #             stack.append(c)
        
    #     # if len(stack) == 0 :
    #     #     return True
    #     return not stack
    def isValid(self, s: str) -> bool:
        brackets_dict = {'}':'{',')':'(',']':'['}
        stack = []
        for c in s:
            if c in brackets_dict :
                top_char = stack.pop() if stack else '#'
                if top_char != brackets_dict[c]:
                    return False
            else:
                stack.append(c)
        return not stack

        
# @lc code=end

