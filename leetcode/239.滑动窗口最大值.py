#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque
class Solution:
    # solution 1
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if len(nums) == 0 :
    #         return []
    #     res = []
    #     for i in range(len(nums)-k+1):
    #         res.append(max(nums[i:i+k]))
    #     return res

# solution2 is slower than solution 1
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     if n == 0 :
    #         return []

    #     return [max(nums[i:i+k]) for i in range(n - k +1)]
        # Solution 3 use deque
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     if n * k ==0:
    #         return []
    #     if k == 1:
    #         return nums

    #     def clean_deque(i):
    #         if deq and deq[0] == i- k:
    #             deq.popleft()
            
    #         while deq and nums[i] > nums[deq[-1]]:
    #             deq.pop()
            
    #     deq = deque()
    #     max_idx = 0
    #     for i in range(k):
    #         clean_deque(i)
    #         deq.append(i)
    #         if nums[i] > nums[max_idx]:
    #             max_idx = i
    #     output = [nums[max_idx]]
    #     for i in range(k,n):
    #         clean_deque(i)
    #         deq.append(i)
    #         output.append(nums[deq[0]])
    #     return output
    # solution 3 fastest
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_area = []
        n = len(nums)
        max_posi = -1
        if n == 0 :
            return max_area
        
        for i in range(k-1,n ):
            temp = i - k +1
            if max_posi < temp :
                max_value = nums[temp]
                max_posi = temp
                for j in range(temp+1,temp+k):
                    if max_value < nums[j]:
                        max_value = nums[j]
                        max_posi = j
            else :
                if max_value <= nums[i]:
                    max_value = nums[i]
                    max_posi = i

            max_area.append(max_value)
        return max_area





# @lc code=end

