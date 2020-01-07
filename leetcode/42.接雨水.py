#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res,left_max,right_max = 0,0,0
        left ,right = 0,len(height)-1
        while left < right :
            if height[left] < height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    res +=right_max - height[right]
                right -= 1
        return res
        
# @lc code=end

