#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_map={}
        for i in range(len(nums)):
            minus = target-nums[i]
            if  res_map.get(minus,None) is None:
                res_map[nums[i]] = i
                # return [i,res_map[nums[i]]]
                # res.append(i)
            else :
                return [i,res_map[minus]]
                # res.append(i)
                # res.append(res_map[minus])
                # break
        return None

        

        
# @lc code=end

