#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = direct_index = 0
        current = [0, 0]
        obstacleSet = set(map(tuple, obstacles))

        
        for c in commands:
            if c == -1:
                direct_index = (direct_index+1)%4
            elif c == -2:
                direct_index = (direct_index-1)%4
                 
            elif c <=9 and 1 <= c:
                for i in range(c):
                    tmp_x = current[0] + direction[direct_index][0]
                    tmp_y = current[1] + direction[direct_index][1]
                    if (tmp_x, tmp_y) in obstacleSet:
                        break
                    current[0] = tmp_x
                    current[1] = tmp_y
                ans = max(ans, current[0]**2  + current[1]**2 )
        return ans




        
# @lc code=end

