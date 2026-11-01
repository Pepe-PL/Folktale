#  The Game Plan :)
#
#      [Winning room] <- [starting room] -> [room 1] -> [room 3] -> [room 4]
#        x coins]                            [test]      [test]
#           |                                  |           | 
#           V                                  |           V
#       [Final room]                           V        [room 5]
#                                             [room 2]           

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
        print("In front of you is a massive doors, and behind you, a smaller one with [] locks.")
        time.sleep(3)
        print('If you want to enter the massive doors, enter "1". If you want to try to open the smaller doors, enter "2".')

        answer = input("1-2: ")

        if answer == "1":
            room = 'room 1'
        elif answer == "2":
            room = 'room 2'
        else:
            print("Invalid input. Please enter '1' or '2'.")
    elif room == 'room 1':
        print("You enter the massive doors and find yourself in a large hall.")