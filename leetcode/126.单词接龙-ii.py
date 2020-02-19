#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
import collections
class Solution:
    # solution 1 bfs 620ms 25% 17.4MB
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
    #     if endWord not in words:
    #         return []
    #     found, q, nq = False, {beginWord}, set()
    #     while q and not found:
    #         words -= set(q)
    #         for x in q:
    #             for y in [x[:i] + c +x[i+1:] for i in range(n) for c in 'abcdefghijklmnopqrstuvwxyz']:
    #                 if y in words:
    #                     if y == endWord:
    #                         found = True
    #                     else:
    #                         nq.add(y)
    #                     tree[x].add(y)
    #         q, nq = nq, set()
    #     def bt(x):
    #         return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        
    #     return bt(beginWord) 
    # solution2 bfs 216ms 54.3% 20MB
    #   def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
    #     def build_word_dict():
    #         d = {}
            
    #         for word in wordList:
    #             for i in range(len(word)):
    #                 s = word[:i] + '_' + word[i + 1:]
    #                 d[s] = d.get(s,[]) + [word]
    #         return d

    #     word_dict = build_word_dict()

    #     tree, words = collections.defaultdict(set), set(wordList)
    #     if endWord not in words:
    #         return []
    #     found, q, nq = False, {beginWord}, set()
    #     while q and not found:
    #         words -= set(q)
    #         for x in q:
    #             for i in range(len(x)):
    #                 for y in word_dict.get(x[:i] + '_' + x[i+1:],[]) :
    #                     if y in words:
    #                         if y == endWord:
    #                             found = True
    #                         else:
    #                             nq.add(y)
    #                         tree[x].add(y)
    #         q, nq = nq, set()
    #     def bt(x):
    #         return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        
    #     return bt(beginWord) 
    # solution3 bi-bfs  92ms 98% 17.3MB
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        def build_word_dict():
            d = {}
            
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    d[s] = d.get(s,[]) + [word]
            return d

        word_dict = build_word_dict()

        tree, words = collections.defaultdict(set), set(wordList)
        if endWord not in words:
            return []
        found, q, eq, nq,rev = False, {beginWord},{endWord}, set(), False
        while q and not found:
            words -= set(q)
            for x in q:
                for i in range(len(x)):
                    for y in word_dict.get(x[:i] + '_' + x[i+1:],[]) :
                        if y in words:
                            if y in eq:
                                found = True
                            else:
                                nq.add(y)
                            tree[y].add(x) if rev else tree[x].add(y)
            q, nq = nq, set()
            if len(eq) < len(q) :
                eq, q, rev = q, eq, not rev
        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        
        return bt(beginWord) 
        
# @lc code=end

