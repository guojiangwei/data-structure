
import random
import time
import pygame
from mygame_gui_lib import Button
from mygame_gui_lib import Panel
from mygame_gui_lib import OptionButton
import os
import threading
class MainSweeper:
    def __init__(self, main_game):

        self.main_game = main_game        
        # self.level = 1
        self.high = 0
        self.current_score = 0
        self.main_window = main_game.main_window
        self.mine_sweeper = MineSweeper(self)
        self.main_window.add_main(self.mine_sweeper)
        self.sb = ScoreBoard(self)
        self.main_window.register_mouse_down(self.mine_sweeper)
        self.main_window.register_mouse_down(self.sb)
        self.timer = threading.Timer(1, self.compute_score)
        self.running = False
        
        # self.start_game()
        
    def get_game_panel(self):
        return self.main_window.get_main()

    def reset_game(self):
        print("reset sweeper game!")
        self.mine_sweeper.set_level(self.sb.get_level())
        self.mine_sweeper.reset_game()
    def start_game(self):
        self.reset_game()
        self.current_score = 0
        # self.sb.set_curr_label('0')
        # self.sb.set_level(str(self.level))
        self.level = self.sb.get_level()
        self.sb.set_mine_num_label(str(self.mine_sweeper._mine_nums))
        self.running = True
        self.mine_sweeper.running = True
        t = threading.Thread(target= self.compute_score)
        t.start()
        

    def stop_game(self):
        print('stop game!')
        self.running = False
        self.mine_sweeper.running = False
        self.main_game.stop_game()
    
    def compute_score(self):
        if self.running:
            time.sleep(1)
            self.current_score += 1
            self.sb.set_curr_label(str(self.current_score))
            self.compute_score()
class SweeperGrid(Button):
    def __init__(self,row = 0, col = 0, x = 0,y = 0, height = 10, width = 10, image = '', text = '', text_color = (0, 0, 0), background_color = (255, 255, 255)):
        super(SweeperGrid,self).__init__(x = x, y = y, height = height, width = width, image = image, text = text, text_color = text_color, background_color = background_color)
        self.row = row
        self.col = col
        self._content = {'mine':"mygame/resources/mine.png",'redflag':"mygame/resources/redflag.png",'bomb':'mygame/resources/mine-bomb.png'}
    def repose_mouse_down(self,pos , mouse_index = 0):
        # print(mouse_index)
        if self.contain_point(pos):
            print(mouse_index)
            if mouse_index == 0:
                self.change_grid_content('mine')
            elif mouse_index == 1:
                self.change_grid_content('redflag')
                # self.set_image(os.path.abspath("mygame/resources/redflag.png"))
            return True
        return False
    def change_grid_content(self, content):
        print(os.path.abspath("resources/mine.png"))
        self.set_image(os.path.abspath(self._content[content]))

        

class MineSweeper(Panel):
    def __init__(self, main_sweeper, level=1):
        self.main_sweeper = main_sweeper
        parent_window = main_sweeper.get_game_panel()
        print(parent_window)
        super(MineSweeper,self).__init__(x=5, y=5, height=parent_window.get_height()-10,width=parent_window.get_width()-10)
        # status: 0 initial, 1 failed, 2 success, 3,playing
        self.running = False
        self._max_rows = 16
        self._max_cols = 30
        self.init_graph_grid()
        self.set_level(level)
        self.reset_game()
        
    def init_graph_grid(self):
        self.mine_grid = [  [ 'E' for _ in range(self._max_cols)] for _ in range(self._max_rows) ]
        self.graph_grid = [  [] for _ in range(self._max_rows) ]
        for i in range(self._max_rows):
            for j in range(self._max_cols):
                button = SweeperGrid(row = i, col=j, background_color=(0,0,255))
                button.set_visible(False)
                self.graph_grid[i].append(button)
                self.add(button)
                
        
    def reset_game(self):
        self.create_graph_grid()
        self.create_grid()
    # 50 width per grid
    def create_graph_grid(self):
        self.changed = True
        # if self.active:
        dx = (self._width/self._cols)
        dy = (self._height/self._rows)
        print("main size:", self._width, self._height)
        x = 0
        y = 0
        # self.graph_grid = []
        
        for i in range(self._max_rows):
            # x = 10
            for j in range(self._max_cols):
                if i < self._rows and j < self._cols:
                    self.graph_grid[i][j].set_visible(True)
                    self.graph_grid[i][j].active = True
                    self.graph_grid[i][j].set_position(x + dx * j, y= y + dy * i)
                    self.graph_grid[i][j].set_width(dx+1)
                    self.graph_grid[i][j].set_height(dy+1)
                    self.graph_grid[i][j].set_image("")
                    self.graph_grid[i][j].set_bgcolor((0,0,255))
                    # print("dx:dy", dx, dy)
                    self.mine_grid[i][j] = 'E'
                else:
                    self.graph_grid[i][j].set_visible(False)
                
                # button = SweeperGrid(row = i, col=j, x= x + dx *j ,y= y + dy * i, height=dy,width=dx,background_color=(0,0,255))
                # self.main_window.register_mouse_down(button)
                # self.graph_grid[i].append(button)
                # print("test")
        
    def set_level(self, level = 1):
        self._level = level
        if level == 1:
            self._rows = 9
            self._cols = 9
            self._mine_nums = 10
            # self.create_grid(9,9,10)
        elif level == 2:
            self._rows = 16
            self._cols = 16
            self._mine_nums = 40
            # self.create_grid(16,16,40)
        elif level == 3:
            self._rows = 16
            self._cols = 30
            self._mine_nums = 99
            # self.create_grid(16,30,99)

    def create_grid(self):
        random.seed(time.time())
        nums = 0
        while True:
            m = random.randint(0,self._rows - 1)
            n = random.randint(0,self._cols - 1)
            if self.mine_grid[m][n] != 'M':
                self.mine_grid[m][n] = 'M'
                nums += 1
                if nums == self._mine_nums :
                    break
                # judge whether there is a sweeper in specified position
    def _exist_sweeper(self, row, col):
        return self.mine_grid[row][col] == 'M' 
    def gameover(self):
        
        self.running = False
        
        for i in range(self._rows):
            for j in range(self._cols):
                self.graph_grid[i][j].active = False
                if self.mine_grid[i][j] in ['M', 'm']:
                    self.graph_grid[i][j].change_grid_content('mine')
        self.main_sweeper.stop_game()
# get the amount of mine which is not mined
    def get_true_mine_nums(self):
        count = 0
        for rows in self.mine_grid:
            for mine in rows:
                if mine == 'M':
                    count += 1
        return  count 

    def response_mouse_down(self,pos , mouse_index = 0):
        pos = self._convert_to_relatepos(pos)
        if self.running:
            for i in range(self._rows):
                for j in range(self._cols):
                    if self.graph_grid[i][j].active and self.graph_grid[i][j].contain_point(pos) :     
                        if mouse_index == 1: #left button
                            if self._exist_sweeper(i,j):
                                self.graph_grid[i][j].change_grid_content('bomb')
                                self.gameover()
                            else:
                                self.span_mine(i,j)
                                
                                self.update_graph_grid( )
                        elif mouse_index == 0: #right button
                            self.mine_grid[i][j] = 'm'
                            self._mine_nums -= 1
                            if self._mine_nums == 0:
                                self.gameover()
                                return
                            if self._mine_nums < 2 and self.get_true_mine_nums() == self._mine_nums and self.count_unmined_grid() == 2:
                                self.gameover()
                                self._mine_nums = 0
                                self.main_sweeper.main_game.play_button.set_text("successful! play again?")
                            self.main_sweeper.sb.set_mine_num_label(str(self._mine_nums))
                            self.graph_grid[i][j].change_grid_content('redflag')

                        
                        return True
        
        return False
    def count_unmined_grid(self):
        count = 0
        for i in range(self._rows):
            for j in range(self._cols):
                if self.mine_grid[i][j] in ['E', 'M']:
                    print("i,j:", i, j)
                    count += 1
        print("count:",count)
        return  count
        # sweep mine algorithm
    def update_graph_grid(self):
        for i in range(self._rows):
            for j in range(self._cols):
                if self.mine_grid[i][j] == 'B':
                    self.graph_grid[i][j].set_bgcolor((200,200,200))
                elif self.mine_grid[i][j] != 'B' and self.mine_grid[i][j] != 'm' and self.mine_grid[i][j] != 'E' and self.mine_grid[i][j] != 'M':
                    # print("update grid text:", self.mine_grid[i][j])
                    self.graph_grid[i][j].set_text(self.mine_grid[i][j])

    def span_mine(self,row, col):
        directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        def get_mine_num(i, j):
            count = 0
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i and new_i < self._rows and 0 <= new_j < self._cols and self.mine_grid[new_i][new_j] in ['M', 'm']:
                    count +=1
            return count
        def dfs(i= row,j=col):
            mine_nums = get_mine_num(i, j)
            if 0 < mine_nums:
                print("remain mine amount around the grid:" ,mine_nums)
                self.mine_grid[i][j] = str(mine_nums)
            else:
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if 0 <= new_i and new_i < self._rows and 0 <= new_j < self._cols and self.mine_grid[new_i][new_j] == 'E':
                        self.mine_grid[new_i][new_j] = 'B'
                        dfs(new_i, new_j)
        dfs(row,col)
class ScoreBoard:
    def __init__(self,minesweeper):
        self.minesweeper = minesweeper
        panel = minesweeper.main_window.get_right()
        ym = panel.get_height()/2 - 40
        xm = panel.get_width()/2 - 5
        height = 40
        color = (200, 200, 200)


        # display level
        # panel.add(Button(x=2, y=ym, width= xm, height= height, text="level",background_color=color))
        # self.level_label = Button(x=xm+3, y=ym, width= xm, height= height,background_color=color)
        self.level_label = OptionButton([1, 2, 3],x=2, y=ym-30, width= 2*xm-3, height= height+30,background_color=color)
        panel.add(self.level_label)

        ym = ym +height
        # remain mine num
        label = SweeperGrid(x=xm/2 - height/2, y=ym, width= height, height= height ,background_color=color)
        label.change_grid_content('mine')
        panel.add(label)
        self.mine_num_label = Button(x=xm+3, y=ym, width= xm, height=height,background_color=color)
        panel.add(self.mine_num_label)
        

        # display high score
        ym = ym +height
        panel.add(Button(x=2, y=ym, width= xm, height= height, text="High",background_color=color))
        self.high_label = Button(x=xm+3, y=ym, width= xm, height= height,background_color=color)
        panel.add(self.high_label)

        # display current score
        ym = ym +height
        panel.add(Button(x=2, y=ym, width= xm, height= height, text="Score"))
        self.curr_label = Button(x=xm+3, y=ym, width= xm, height= height)
        panel.add(self.curr_label)
    
    def set_curr_label(self, curr):
        
        self.curr_label.set_text(curr)

    def set_high_label(self, high):
        self.high_label.set_text(high)

    # def set_level(self, level):
    #     self.level_label.set_text(level)
    def get_level(self):
        return self.level_label.current_value

    def set_mine_num_label(self, num):
        self.mine_num_label.set_text(num)

    def  response_mouse_down(self,pos , mouse_index = 0):
        print("level label response_mouse_down")
        result = self.level_label.response_mouse_down(pos, mouse_index)
        if result :
            self.minesweeper.reset_game()
        return result
    
    def can_response(self, pos):
        print("level label can response")
        return self.level_label.can_response(pos)
        


        # super(MineSweeper,self).__init__(x=5, y=5, height=parent_window.get_height()-10,width=parent_window.get_width()-10)
