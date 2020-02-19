#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    # solution1 time limit exceeded
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     def viable_word(cur, next):
    #         changes = 0
    #         for i in range(len(cur)):
    #             if cur[i] != next[i] :
    #                 # if changes  == 1:
    #                 #     return False
    #                 changes +=1
    #         return changes == 1
        
    #     queue = [[beginWord, beginWord, 1]]
    #     while queue:
    #         cur , pre ,steps = queue.pop(0)
    #         if cur == endWord :
    #             return steps
    #         for word in wordList:
    #             if word != pre and viable_word(cur, word):
    #                 queue.append([word, cur, steps+1])
    #     return steps
    # solution2 bfs 160ms 47.4% 16.8MB
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = [(begin, 1)] ,set()
            while queue:
                word, steps = queue.pop(0)
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(set(wordList) )

        return bfs_words(beginWord, endWord, d)
        
# @lc code=end

