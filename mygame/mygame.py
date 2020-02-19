import pygame
from mygame_gui_lib import Panel
from mygame_gui_lib import Button
from main_window import MainWindow
import sys
# from minesweeper import MineSweeper
from minesweeper import MainSweeper
import os
from settings import Settings
import types
class PlayGameButton(Button):
    def __init__(self,mainwindow,text='Play Game!',width=150):
        super(PlayGameButton, self).__init__(text=text,width=width)
        self.main_window = mainwindow
    def response_mouse_down(self, pos, mouse_index=0):
        if self._visible:
            self.set_visible(False)
            self.main_window.start()
            return True
        return False

class MainGame:
    def __init__(self):
        settings = Settings()
    
        self.main_window = MainWindow()
        self.exit_button = Button(text="exit", background_color=(200, 200, 200))
        self.sweep_button = Button(width=70, text="sweep", background_color=(200, 200, 200))
        self.main_window.add_top(self.exit_button)
        self.exit_button.set_right()
        self.main_window.add_top(self.sweep_button)
        
        self.main_sweeper = MainSweeper(self)
        self.current_game = self.main_sweeper
        
        self.play_button = PlayGameButton(self)
        self.main_window.add_main(self.play_button)
        self.main_window.register_mouse_down(self.play_button)
        self.main_window.register_sys_exit(self)
    def start(self):
        self.current_game.start_game()
    
    def get_game_panel(self):
        # print("test:", self.main_window.get_main())
        return self.main_window.get_main()
    def stop_game(self):
        self.play_button.set_visible(True)
        self.play_button.active = True
        self.play_button.set_text("play again!")

    def sys_exit(self):
        print("sys exit")
        self.stop_game()
        self.main_sweeper.stop_game()
        
    def start_game(self):

        while True:
            self.main_window.show_window()
            self.main_window.start_listen_event()



if __name__ == "__main__":
    print(os.getcwd())
    print(sys.argv)
    main_game = MainGame()
    main_game.start_game()

    # mine_sweeper = MineSweeper(main_window.get_main())
    # main_window.add_main(mine_sweeper)
    
    

    

        
        


