#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums) <3 :
            return res
        nums.sort()
        n = len(nums)
        for i in range(n):
            if 0 < nums[i] :
                return res
            if 0< i and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n - 1
            while(left < right) :
                temp =nums[i] + nums[left] + nums[right]
                if(temp == 0 ):
                    res.append([nums[i],nums[left],nums[right]])
                    while(left < right and nums[left] == nums[left+1]):
                        left +=1
                    while(left<right and nums[right] == nums[right-1]):
                        right -=1
                    left +=1
                    right -=1
                elif(0 < temp):
                    right -=1
                else:
                    left +=1
        return res
            
        

        
# @lc code=end

