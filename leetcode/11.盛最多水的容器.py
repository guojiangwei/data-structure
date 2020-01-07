#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     length = len(height)
    #     left,right = 0,length-1
    #     max_area = 0
    #     for i in range(length):
    #         if height[left] > height[right]:
    #             temp = height[right] * (right - left)
    #             right -=1
    #         else:
    #             temp = height[left] * (right - left)
    #             left +=1
            
    #         if temp>max_area:
    #             max_area=temp
    #     return max_area

# < is faster than >
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                temp = height[left] * (right - left)
                left +=1
                
            else:
                temp = height[right] * (right - left)
                right -=1
                
            
            # if temp>max_area:
            max_area= max(temp,max_area)
        return max_area
        
# @lc code=end

