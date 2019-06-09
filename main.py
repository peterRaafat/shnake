from env import Env
from player import Player
from timing import RepeatedTimer
from gui import GUI

def main():
    shnake = Env()
    player = Player(shnake)
    player.start()
    rt1 = RepeatedTimer((shnake.refresh_rate/1000), shnake.step)
    window = GUI(shnake)
    window.run()

main()