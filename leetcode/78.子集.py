#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    # solution 1 36ms 87% 13.5MB
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for i in nums:
    #         res = res + [[i] + num for num in res]
        
    #     return res
    # solution2 52ms 19% 13.4MB
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for i in nums:
    #         for  r in res:
    #             res = res + [[i]+r]
    #     return res

# solution3 36ms 87%  13.5MB
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n=len(nums)
        def helper(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                helper(j + 1, tmp + [nums[j]])
        helper(0,[])
        return res

    
        
# @lc code=end

