#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    # solution 1 60ms 13MB
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     s_dict={}
    #     for s1 in s:
    #         s_dict[s1]=s_dict.get(s1,0)+1
    #     for s2 in t:
    #         ss = s_dict.get(s2,None)
    #         if ss is None :
    #             return False
    #         ss  -= 1
    #         s_dict[s2] = ss
    #         if ss == 0:
    #             del s_dict[s2]
    #             # len(s_dict)
        
    #     return (len(s_dict) == 0)
# solution 2 84ms 17.33% 12.9 
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
        
    #     s_dict={}
    #     for s1 in s:
    #         s_dict[s1]=s_dict.get(s1,0)+1
    #     for s2 in t:
    #         ss = s_dict.get(s2,None)
    #         if ss is None :
    #             return False
    #         ss  -= 1
    #         s_dict[s2] = ss
    #     for key in s_dict.keys():
    #         if s_dict[key] != 0 :
    #             return False
    #     return True
    # solution 3 56ms 72.15% 13MB
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     s_dict={}
    #     for s1 in s:
    #         s_dict[s1]=s_dict.get(s1,0)+1
    #     for s2 in t:
    #         ss = s_dict.get(s2,0)
    #         if ss == 0 :
    #             return False
    #         if ss == 1:
    #             del s_dict[s2]
    #         else:
    #             ss  -= 1
    #             s_dict[s2] = ss
            
    #             # len(s_dict)
        
    #     return (len(s_dict) == 0)

       # solution 4 60ms 63.15% 13MB
    # 
    # solution 4 use set   52ms 81.05% 13.1m
    # def isAnagram(self, s: str, t: str) -> bool:
    #     res = True
    #     s_set = set(s)
    #     if s_set == set(t):
    #         for i in s_set:
    #             res = res and s.count(i) == t.count(i)
    #     else:
    #         return False
    #     return res
# solution 5
    def isAnagram(self, s: str, t: str) -> bool:
        alphas=[0]*26
        if len(s) != len(t):
            return False
        for s1 in s:
            alphas[ord(s1)-97] +=1
        for t1 in t:
            alphas[ord(t1)-97] -=1
            
        for c in alphas:
            if c != 0 :
                return False
        
        return True
        

        
# @lc code=end

