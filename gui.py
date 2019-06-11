from tkinter import *
from env import Env
import numpy as np


class GUI():
    """
    this class handles the user interface for the game
    """
    def __init__(self, env):
        """
        initialize the GUI parameters
        Parameters:
        ----------
        env     :       object of type Env
        """
        self.env = env
        self.window = Tk()
        self.window.title("shnaaaaaaaake")
        self.window.resizable(False, False)

        #initalize sizes
        score_frame_size = (25,600)
        self.game_frame_size = (600, 600) # must be square
        self.cell_size = (self.game_frame_size[0]//env.dimensions)

        # initialize working frame
        self.main_frame = Frame(self.window, height = score_frame_size[0], width = score_frame_size[1])
        self.main_frame.pack()
        # initialize labels
        self.score_label = Label(self.main_frame, text=("Score  " + str(env.score)))
        self.max_moves_label = Label(self.main_frame, text=("Maximum moves  " + str(env.maxiumum_moves)))
        self.score_label.pack()
        self.max_moves_label.pack()
        self.score_label.place(bordermode=INSIDE, x=0,y=0)
        self.max_moves_label.place(bordermode=INSIDE, x=((score_frame_size[1]//3)), y=0)

        # create canvas to draw grid
        self.canvas = Canvas(self.window, height = self.game_frame_size[0], width = self.game_frame_size[1])
        self.canvas.pack(side=BOTTOM)
        self.grid_update()

    def grid_update(self):
        """
        Update the colors of the grid depending on the environment
        :return:
        """
        self.canvas.delete(ALL)
        grid = self.env.grid
        snake_length = len(self.env.snake_body)
        rainbow_colors = ["purple", "blue", "cyan", "green", "orange", "yellow", "red"]
        snake_colors = []
        partition = (snake_length//len(rainbow_colors) + 1)
        counter = 0
        for i, snake_color in enumerate(self.env.snake_body, 1):
            if i % partition == 0:
                counter +=1

            snake_colors.append(rainbow_colors[counter])
        color = ["grey", "black"]
        # create list of rectangle
        snake_index = 0
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                # create rectangle in canvas
                top_left = [j*self.cell_size, i*self.cell_size]
                bottom_right = [(j+1)*self.cell_size, (i+1)*self.cell_size]
                if entry == 0:
                    self.canvas.create_rectangle(top_left[0], top_left[1], bottom_right[0], bottom_right[1],
                                                 outline = "black",fill=color[0])
                elif entry == -1:
                    self.canvas.create_rectangle(top_left[0], top_left[1], bottom_right[0], bottom_right[1],
                                                 outline="black", fill=snake_colors[snake_index])
                    snake_index += 1
                else:
                    self.canvas.create_rectangle(top_left[0], top_left[1], bottom_right[0], bottom_right[1],
                                                 outline="black", fill=color[1])
        self.score_label['text'] = "Score  " + str(self.env.score)
        self.max_moves_label['text'] = "Maximum moves  " + str(self.env.maxiumum_moves)
        self.canvas.after(int(self.env.refresh_rate/3), self.grid_update)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    env = Env()
    gui = GUI(env)
