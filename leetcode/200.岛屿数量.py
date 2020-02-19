#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    # solution1 dfs 156ms 78%  14.4MB
    # def numIslands(self, grid: List[List[str]]) -> int:

    #     def dfs(i1, j1, m1 , n1):
    #         marked[i1][j1] = True
    #         for direction in directions:
    #             new_i = i1 + direction[0]
    #             new_j = j1 + direction[1]
    #             if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
    #                 dfs(new_i, new_j, m, n)


    #     m = len(grid)

    #     if m == 0:
    #         return 0
    #     n = len(grid[0])
    #     directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    #     marked = [[False for _ in range(n)] for _ in range(m)]
    #     count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if not marked[i][j] and grid[i][j] == '1':
    #                 count += 1
    #                 dfs(i, j, m, n)
    #     return count
    # solution2 dfs 152ms 85% 14.4MB
    # def numIslands(self, grid: List[List[str]]) -> int:

    #     def dfs(i1, j1, m1 , n1):
    #         grid[i1][j1] = '0'
    #         for direction in directions:
    #             new_i = i1 + direction[0]
    #             new_j = j1 + direction[1]
    #             if 0 <= new_i < m and 0 <= new_j < n and  grid[new_i][new_j] == '1':
    #                 dfs(new_i, new_j, m, n)


    #     m = len(grid)

    #     if m == 0:
    #         return 0
    #     n = len(grid[0])
    #     directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    #     # directions = [(1, 0), (0, 1)]

    #     # marked = [[False for _ in range(n)] for _ in range(m)]
    #     count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if  grid[i][j] == '1':
    #                 count += 1
    #                 dfs(i, j, m, n)
    #     return count
    # solution3 bfs 152ms 85% 14.2MB
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     m = len(grid)
    #     if m == 0:
    #         return 0
    #     n = len(grid[0])
    #     count = 0
    #     directions = [(-1, 0), (0, -1), (1, 0), (0,  1)]
        
    #     for i in range(m):
    #         for j in range(n):
                
    #             if grid[i][j] == '1':
    #                 queue = [(i, j)]
    #                 count += 1
    #                 grid[i][j] = '0'
    #                 while queue:
    #                     cur_i, cur_j = queue.pop(0)
    #                     for direction in directions:
    #                         new_i = cur_i + direction[0]
    #                         new_j = cur_j + direction[1]
    #                         if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
    #                             queue.append((new_i,new_j))
    #                             grid[new_i][new_j] = '0'
    #     return count
# solution 4 union set 192ms 30%  16.2MB
    def numIslands(self, grid: List[List[str]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]
            
            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p
            
            def is_connected(self, p, q):
                return self.find(p) == self.find(q)
            
            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)

                if p_root == q_root:
                    return
                
                if self.rank[q_root] < self.rank[p_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1
                
                self.count -= 1

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        def get_index(x, y):
            return x*n + y
        count = m * n
        uf = UnionFind(count + 1)
        directions = [(1, 0), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), count)
                if grid[i][j] == '1':
                    for direction in directions:
                        new_i = i + direction[0]
                        new_j = j + direction[1]
                        if new_i < m  and new_j < n and grid[new_i][new_j] == '1':
                            uf.union(get_index(i, j), get_index(new_i, new_j))
        return uf.get_count() - 1


        
# @lc code=end

