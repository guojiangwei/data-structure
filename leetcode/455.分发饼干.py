#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # sorted(s)
        num = 0
        size_g = len(g)
        size_s = len(s)

        if size_g == 0 or size_s ==0:
            return 0
        index_s = index_g = 0
        while index_s < size_s and index_g < size_g:
            if s[index_s] >= g[index_g]:
                index_s += 1
                index_g += 1
                num +=1
            elif s[index_s] < g[index_g]:
                index_s += 1
        return num

        
# @lc code=end

