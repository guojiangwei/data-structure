#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start
class Solution:
    # solution1 364ms 5.3% 14.6MB
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return nums[int(len(nums)/2)]
# solution2 204ms 75.2% 14.5MB
    # def majorityElement(self, nums: List[int]) -> int:
    #     n = int(len(nums)/2)
    #     nums_dict = {}
    #     for num in nums:
    #         tmp = nums_dict.get(num,0) +1
    #         if tmp > n:
    #             return num
    #         nums_dict[num] = tmp
    #     return nums[int(len(nums)/2)]

    # solution 3 208ms 67.6% 14.5 MB
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0 :
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
        
# @lc code=end

