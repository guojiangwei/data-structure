#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    # solution 1 
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     return [int(x) for x in str(int(''.join(str(i) for i in digits))+1)]

    def plusOne(self, digits: List[int]) -> List[int]:
        level = len(digits)
        level = self.plus(digits,level)
        if level == -1:
            digits[:]=[1]+digits[:len(digits)]
        return digits
    def plus(self,digits,level):
        index = level-1
        if index < 0 :
            return -1
        digits[index] = (digits[index]+1)%10
        if digits[index] == 0:
            return self.plus(digits,index)
        return index
        
# @lc code=end

