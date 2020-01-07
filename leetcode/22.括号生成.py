#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    # solution1 104 6.27% 13
    # def generateParenthesis(self, n: int) -> List[str]:
    #     def generate(A = []):
    #         if len(A) == 2*n:
    #             if valid(A):
    #                 res.append("".join(A))
    #         else:
    #             A.append('(')
    #             generate(A)
    #             A.pop()
    #             A.append(')')
    #             generate(A)
    #             A.pop()
        
    #     def valid(A):
    #         count = 0
    #         for c in A:
    #             if c == '(' :
    #                 count +=1
    #             else:
    #                 count -=1
                
    #             if count < 0:
    #                 return False
    #         return count ==0
        
    #     res = []
    #     generate()
    #     return res

    # def valid(self,A):
    #     count = 0
    #     for c in A:
    #         if c == '(' :
    #             count +=1
    #         else:
    #             count -=1
            
    #         if count < 0:
    #             return False
    #     return count ==0
    # # solution2  84ms 7.61% 12.7
    # def generateParenthesis(self, n: int) -> List[str]:
    #     res = []
    #     def backtrack(s = '',left = 0, right = 0):
    #         if len(s) == 2*n:
    #             if self.valid(s):
    #                 res.append(s)
    #             return
    #         if left < n:
    #             backtrack(s+'(',left +1 ,right)
    #         if right < n:
    #             backtrack(s+')',left,right+1)
            
    #     backtrack()
    #     return res    
# solution3 dp 28ms 98.76% 12.7MB
        def generateParenthesis(self, n: int) -> List[str]:
            dp = [[] for _ in range(n+1)]
            dp[0] = ['']
            for i in range(1,n+1):
                for p in range(i):
                    l1 = dp[p]
                    l2 = dp[i-1-p]
                    for k1 in l1:
                        for k2 in l2:
                            dp[i].append('({0}){1}'.format(k1,k2))
            return dp[n]


        
# @lc code=end

