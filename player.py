from pynput.keyboard import Listener
from env import Env


class Player:
    """
    This class handles the input from the user
    """
    def __init__(self, env):
        """
        initialize class parameters
        """
        # initialize player action
        self.action = None
        # run keyboard listener
        self.listener = Listener(on_press= self.set_action)
        self.env = env

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def set_action(self, key):
        print(key)
        if key == key.up:
            self.action = [1,0,0,0]
        elif key == key.right:
            self.action = [0,1,0,0]
        elif key == key.down:
            self.action = [0,0,1,0]
        elif key == key.left:
            self.action = [0,0,0,1]
        self.env.act(self.action)
