#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
import collections
class Solution:
    # solution1 dfs 40ms 56% 13.2MB
    # def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # changes = {'A':'GCT',
        # 'G':'ACT',
        # 'C':'AGT',
        # 'T':'AGC'}
        # bank = set(bank)
        # def helper(node , count , _bank):
            # if node == end :counts.append(count)
            # if not _bank : return
            # for i , s in enumerate(node):
                # for c in changes[s]:
                    # new_node = node[:i] + c + node[i + 1:]
                    # if new_node in _bank:
                        # _bank.remove(new_node)
                        # helper(new_node, count + 1, _bank)
                        # _bank.add(new_node)
        # counts = []
        # helper(start,0,bank)
        # if not counts : return -1
        # else: return min(counts)
# solution2 bfs 32ms 85% 13.2
    # def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    #     def vaible_mutation(cur, next):
    #         changes = 0
    #         for i in range(len(cur)):
    #             if cur[i] != next[i]:
    #                 changes += 1
    #         return changes == 1
    #     queue = []
    #     queue.append([start, start, 0])
    #     while queue:
    #         current, previous, steps = queue.pop(0)
    #         if current == end: return steps
    #         for gen in bank:
    #             if vaible_mutation(current,gen) and gen != previous:
    #                 queue.append([gen,current, steps + 1])
    #     return -1
    #solution3 use collections library
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def vaible_mutation(cur, next):
            changes = 0
            for i in range(len(cur)):
                if cur[i] != next[i]:
                    changes += 1
            return changes == 1
        queue = collections.deque()
        queue.append([start, start, 0])
        while queue:
            current, previous, steps = queue.popleft()
            if current == end: return steps
            for gen in bank:
                if vaible_mutation(current,gen) and gen != previous:
                    queue.append([gen,current, steps + 1])
        return -1
# @lc code=end

