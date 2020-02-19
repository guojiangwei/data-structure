#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
# solution 1 dfs 280ms 26.7% 15.8MB
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(-1, 0),  (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1),(-1, 1)]
        row = len(board)
        col = len(board[0])

        def get_sweeper(x, y):
            count = 0
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < row and 0 <= new_y < col and board[new_x][new_y] == 'M':
                    count += 1
            return count
        def dfs(x, y):
            if 0 <= x < row and 0 <= y < col:
                
            
                if board[x][y] == 'M':
                    board[x][y] = 'X'
                    return
                if board[x][y] == 'E':
                    num = get_sweeper(x, y)

                    if num > 0:
                        board[x][y] = str(num)
                    else:
                        board[x][y] = 'B'
                        for direction in directions:
                            new_x = x + direction[0]
                            new_y = y + direction[1]
                            dfs(new_x, new_y)

        dfs(click[0], click[1])
        return board

        
# @lc code=end

