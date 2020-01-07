#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    # solution 1 time limit exceeded
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     if not heights :
    #         return 0
    #     max_area = 0
    #     n = len(heights)
    #     for i in range(n):
    #         left = i
    #         right = i
    #         while 0 <= left and heights[i] <= heights[left]:
    #             left -= 1
    #         while right <n and heights[i] <= heights[right]:
    #             right +=1
    #         max_area = max(max_area,(right-left-1)*heights[i])
            
    #     return max_area

# solution2 time limit exceeded
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     n = len(heights)
    #     if n == 0 :
    #         return 0
    #     left_i = [0] *n
    #     right_i = [0] *n
    #     left_i[0] = -1
    #     right_i[-1] = n
    #     max_area = 0 

    #     for i in range(1,n):
    #         tmp = i - 1
    #         while 0 <= tmp and heights[i] <= heights[tmp]:
    #             tmp -=1
    #         left_i[i] = tmp
    #     for i in range(n-2 , -1 , -1):
    #         tmp = i+1
    #         while tmp < n and heights[i] <= heights[tmp]:
    #             tmp += 1
    #         right_i[i] = tmp

    #     for i in range(n):
    #         max_area = max(max_area,(right_i[i]-left_i[i]-1)*(heights[i])) 
    #     return max_area
# solution 3
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        max_area= 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                max_area = max(max_area,(i - stack[-1]-1)*heights[tmp])
            stack.append(i)
        return max_area



        
# @lc code=end

