#  The Game Plan :)
#
#      [Winning room] <- [starting room] -> [room 1] -> [room 3] -> [room 4]
#        x coins]                       |    [test]      [test]
#           |                           V                  | 
#           V                        [room 2] -> [room 3]  |
#       [Final room]                                       V
#                                                       [room 5]

import time

room = 'starting'
coins = 0
game_running = True
while game_running:
    if room == 'starting':
        print("You have woken up in a strange place...")
        time.sleep(1)
        print("You don’t know where you are...")
        time.sleep(2)
        print("You look around, but you can’t see anything because it’s dark...")
        time.sleep(2)
        print("However, next to the bed you’re in, you spot a light...")
        time.sleep(3)
        print("It turns out to be a torch...")
        time.sleep(1)
        print("You pick it up and stand up.")
        time.sleep(1)
        print("In front of you is a massive door, and behind you, a smaller one with [] locks.")
        time.sleep