#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    # solution 1 time limit exceeded
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = []
    #     strs_dict = {}
        
    #     for s in strs:
    #         strs_dict[s] = strs_dict.get(s,0)+1

    #     while strs_dict:
    #         items = list(strs_dict.items())

    #         tmp=[]
    #         for i in range(items[0][1]):
    #             tmp.append(items[0][0])

    #         for key ,value in items[1:]:
    #             if self.isAnagram(tmp[0],key):
    #                 for i in range(value):
    #                     tmp.append(key)
    #                 del strs_dict[key]
    #         del strs_dict[tmp[0]]
    #         res.append(tmp)

    #     return res
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     alphas=[0]*26
    #     for s1 in s:
    #             alphas[ord(s1)-97] +=1
        
    #     for t1 in t:
    #         alphas[ord(t1)-97] -=1
            
    #     for c in alphas:
    #         if c != 0 :
    #             return False
        
    #     return True
    # # solution 2 120ms 68.4% 18MB
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = {}
        
    #     for s in strs:
    #         alphas = [0] * 26
    #         for c in s:
    #             alphas[ord(c)-97] +=1
    #         t=tuple(alphas)
    #         # res.setdefault(t,[])
    #         # res[t].append(s)
    #         res[t] = res.get(t,[])+[s]
    #     return res.values()

        # solution 3 112ms 85.4% 16.4MB
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            # alphas = [0] * 26
            # for c in s:
            #     alphas[ord(c)-97] +=1
            # t=tuple(alphas)
            # res.setdefault(t,[])
            # res[t].append(s)
            ss = tuple(sorted(s))
            res[ss] = res.get(ss,[])+[s]
        return res.values()

        
# @lc code=end

