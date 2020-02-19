#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    # solution1 508ms 64% 14.1
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     def helper(start ,level ):
    #         if level == 0:
    #             res.append(list(tmp))
    #             return
    #         for i in range(start,n):
    #             tmp.append(s_num[i])
    #             helper(i+1 ,  level-1)
    #             tmp.pop()

                
    #     res = []
    #     tmp = []
    #     s_num = list(range(1,n+1))
    #     helper(0,k)
    #     return res

    # solution 2 88ms 95.6% 14.1
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,k+1)) + [n+1]

        output , j = [] , 0
        while j < k :
            output.append(nums[:k])

            j = 0
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j +=1
            nums[j] += 1

        return output 
        
# @lc code=end

