#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) 

        lessk=len(nums) - k

        temp = [ num for num in nums[0:lessk]]
        for i in range(k):
            nums[i] = nums[lessk+i]
        for i in range(lessk):
            nums[k+i] = temp[i]
        

        
# @lc code=end

