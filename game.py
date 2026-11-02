#  The Game Plan :)
#
#      [Winning room] <- [starting room] -> [room 1] -> [room 3] -> [room 4]
#        x coins]                            [test]      [test]
#           |                                  |           
#           V                                  |           
#       [Final room]                           V        
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
        time.sleep(1)
        print("There are two doors in front of you, one to the left and one to the right.")
        time.sleep(1)
        print("Also in the room, you see a table with a small machine on it.")
        time.sleep(1)
        print('On the machine there is a note that says: "Win a coin by answering a question correctly. If you answer incorrectly, you will die instantly."')
        time.sleep(1)
        print('If you want to answer the question, enter "1". If you want to go through the left door, enter "2". If you want to go through the right door, enter "3". If you want to turn back and go back to the starting room, enter "4".')

        answer = input("1-4: ")

        if answer == "1":
            print("You approach the machine and read the question on the screen.")
            time.sleep(1)
            print("The question is: 'What is the capital of Australia?'")
            time.sleep(1)
            print('If you want to answer "Canberra", enter "1".')
            print('If you want to answer "Sydney", enter "2".')
            print('If you want to answer "Melbourne", enter "3".')
            print('If you want to answer "Brisbane", enter "4".')

            room1_answer = input("Enter your answer: ")

            if room1_answer == "1":
                print("Correct! You have won a coin.")
                coins += 1
                time.sleep(1)
                print(f"You now have {coins} coin(s).")

            elif room1_answer in ["2", "3", "4"]:
                print("Incorrect! You have died instantly.")
                time.sleep(1)
                print("Game Over.")
                time.sleep(1)
                again = input("Do you want to play again? (yes/no): ")
                if again.lower() != "yes":             
                    coins = 0
                    room = 'starting'
                else:
                    print("Thx for playing <3")

        elif answer == "2":
            room = 'room 2'

        elif answer == "3":
            room = 'room 3'

        elif answer == "4":
            room = 'starting'

        else:
            print("Invalid input. Please enter '1', '2', '3', or '4'.")

        