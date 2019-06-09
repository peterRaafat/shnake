import numpy as np
import random


class Env:

    def __init__(self):
        """
        Initialize the paramaeters of the grid world
        Paramaeters:
        ------------
        dimensions  :   int
            dimension of the grid world
        grid    :   2d numpy array
            the grid world of the environment
        apple_loc : list of int
            the location of the apple
        score   :   int
        maximum_moves   :   int
        done    :   boolean
        snake_heading   :   list of 4 ints
            index 0 : moving up
            index 1 : moving right
            index 2 : moving down
            index 3 : moving left
        snake_body  :  2d list of int
            indices where the snake body is
        """
        self.dimensions = 30
        self.grid = np.zeros((self.dimensions, self.dimensions))
        # initialize snake to be at top left
        self.grid[0][0] = -1
        # pick a random location for the apple
        random_row = random.randint(1, self.dimensions-1)
        random_column = random.randint(1, self.dimensions - 1)
        self.grid[random_row][random_column] = 1
        self.apple_loc = [random_column, random_column]
        self.apple_eaten = False
        # initialize zero score
        self.score = 0
        # initialize maximum number of moves
        self.maxiumum_moves = 500
        self.done = False
        # initialize snake body and direction to right
        self.snake_heading = [0, 1, 0, 0]
        self.snake_body = [[0, 0], [0, 1]]
        # manage time
        self.update_apple_loc()  # remove later
        self.update_grid() # remove later
        self.refresh_rate = 300  # ms


    def get_refresh_rate(self):
        return self.refresh_rate

    def step(self):
        """
        Take an action in the environment
        :param
        action  :   list of int
        :return
        state   :   the grid values of the game
        score   :   int
        done    :   boolean
        """
        state = [self.grid, self.snake_heading]
        score = self.score
        done = self.done
        if self.done:
            print("game over")
        else:
            print("heading: {}". format(self.snake_heading))
            # update heading
            # check if you are changing direction in direction not opposite to the heading
            # update snake body
            self.update_snake()
            # update done
            self.update_done()
            # update apple location
            self.update_apple_loc()
            #delete snake tail if apple was eaten
            self.delete_tail()
            # update grid
            self.update_grid()

        # update moves left
        return state, score, done

    def update_snake(self):
        """
        update the indicies which contain snake body
        :param
        heading :   list of int
        :return:
        """

        snake_body = self.snake_body[:]
        head = snake_body[-1][:]
        #check heading
        if self.snake_heading[0] == 1: #moving up
            # decrement the row value of the last index of snake body (head)
            head[0] -= 1
            snake_body.append(head)
        elif self.snake_heading[1] == 1: #moving right
            # increment the column value of the last index of snake body (head)
            head[1] += 1
            snake_body.append(head)
        elif self.snake_heading[2] == 1: #moving down
            # increment the row value of the last index of snake body (head)
            head[0] += 1
            snake_body.append(head)
        elif self.snake_heading[3] == 1: #moving left
            # decrement the column value of the last index of snake body (head)
            head[1] -= 1
            snake_body.append(head)
        self.snake_body = snake_body

    def update_grid(self):
        """
        change values of grid depending on snake and apple location
        :return:
        """
        if not self.done:
            self.grid = np.zeros((self.dimensions, self.dimensions))
            # insert -1 at snake locations
            for index in self.snake_body:
                self.grid[index[0], index[1]] = -1
            # insert 1 at apple location
            self.grid[self.apple_loc[0], self.apple_loc[1]] = 1

    def update_done(self):

        occurrences = {}
        # check if no moves left
        if self.maxiumum_moves == 0:
            self.done = True
            return
        for index in self.snake_body:
            # check if snake left grid
            if (-1 in index) or (self.dimensions in index):
                self.done = True
                return
            # check if snake hit it self
            str_index = ""
            for i in index:
                str_index += str(i)
            if str_index in occurrences:
                self.done = True
                return
            occurrences[str_index] = 1

    def act(self, action):
        if action != None:
            opposite_action = action[2:] + action[:2]
            if (action == self.snake_heading) or (opposite_action == self.snake_heading):
                pass
            else:
                self.snake_heading = action

    def update_apple_loc(self):
        """
        update the apple location and score in case apple was eaten
        :return:
        """
        print(len(self.snake_body))
        if self.snake_body[-1] == self.apple_loc:
            # increment score
            self.score += 1
            # update apple location
            # avoid getting apple location at snake location
            grid = np.zeros((self.dimensions, self.dimensions))
            available_spots = []
            for i, row in enumerate(grid):
                for j, column in enumerate(row):
                    if list([i, j]) not in self.snake_body:
                        available_spots.append([i, j])

            random_loc = random.sample(available_spots, k=1)
            self.apple_loc = [random_loc[0][0], random_loc[0][1]]
            # change the eaten flag to true to increase length of snake body
            self.apple_eaten = True

    def delete_tail(self):
        # delete tail if no apple was eaten
        if self.apple_eaten == False:
            del self.snake_body[0]
        else:
            # reset the flag if apple was eaten
            self.apple_eaten = False

if __name__ == '__main__':
    shnake = Env()
    while True:
        shnake.step()
