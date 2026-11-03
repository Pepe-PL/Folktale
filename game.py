# Made by Patryk Powirski (Pepe-PL) 2026


#  The Game Plan :)
#
#      [Winning room] <- [starting room] -> [room 1] -> [room 3] -> [room 4]
#        x coins]                            [test]      [test]
#           |                                  |           
#           V                                  |           
#     [Winning room]                           V        
#                                           [room 2]           

import time
import random

room = 'starting'
keys = 0
coin_to_room_3 = False
room1_quiz_answered = False
game_running = True

while game_running:
    if room == 'starting':
        print("You have woken up in a strange place...")
        time.sleep(2)
        print("You dont know where you are...")
        time.sleep(2)
        print("You look around, but you cant see anything because its dark...")
        time.sleep(2)
        print("However, next to the bed youre in, you spot a light...")
        time.sleep(3)
        print("It turns out to be a torch...")
        time.sleep(2)
        print("You pick it up and stand up.")
        time.sleep(2)
        print("In front of you is massive doors, and behind you, a smaller one with 3 locks.")
        time.sleep(3)
        print('If you want to enter the massive doors, enter "1". If you want to try to open the smaller doors, enter "2".')

        answer = input("1-2: ")

        if answer == "1":
            room = 'room 1'
        elif answer == "2":
            room = 'winning room'
        else:
            print("Invalid input. Please enter '1' or '2'.")
    
    elif room == 'room 1':
        
        time.sleep(2)
        print("You enter the massive doors and find yourself in a large hall.")
        time.sleep(2)
        print("There are two doors in front of you, one to the left and one to the right.")
        time.sleep(2)
        print("Also in the room, you see a table with a small machine on it.")
        time.sleep(2)
        print('On the machine there is a note that says: "Win a coin by answering a question correctly. If you answer incorrectly, you will die instantly."')
        print("")
        time.sleep(2)
        print('If you want to answer the question, enter "1". If you want to go through the left door, enter "2". If you want to go through the right door, enter "3". If you want to turn back and go back to the starting room, enter "4".')

        answer = input("1-4: ")

        if answer == "1":

            if room1_quiz_answered:
                print("You have already answered the question in this room. You cannot answer it again.")
                time.sleep(2)
                print("You must choose another option.")
                room = 'room 1'
                room1_quiz_answered = True

            else:
                
                print("You approach the machine and read the question on the screen.")
                time.sleep(2)
                print("The question is: 'What is the capital of Australia?'")
                time.sleep(2)
                print('If you want to answer "Canberra", enter "1".')
                print('If you want to answer "Sydney", enter "2".')
                print('If you want to answer "Melbourne", enter "3".')
                print('If you want to answer "Brisbane", enter "4".')

                room1_answer = input("Enter your answer: ")

                if room1_answer == "1":
                    print("")
                    print("Correct! You have won a key.")
                    room1_quiz_answered = True
                    keys += 1
                    time.sleep(2)
                    print(f"You now have {keys} key(s).")
                    print("")

                elif room1_answer == "2" or room1_answer == "3" or room1_answer == "4":
                    print("")
                    print("Incorrect! You have died instantly.")
                    room1_quiz_answered = True
                    time.sleep(2)
                    print("Game Over.")
                    time.sleep(2)
                    again = input("Do you want to play again? (yes/no): ")
                    if again.lower() == "yes":             
                        keys = 0
                        room1_quiz_answered = False
                        coin_to_room_3 = False
                        room = 'starting'
                    else:
                        print("Thx for playing! <3")
                        game_running = False

                else:
                    print("Invalid input. Please enter '1', '2', '3', or '4'.")

        elif answer == "2":
            room = 'room 2'

        elif answer == "3":
            room = 'room 3_before'

        elif answer == "4":
            room = 'starting'

        else:
            print("Invalid input. Please enter '1', '2', '3', or '4'.")

    elif room == 'room 2':

        print("You enter the doors and find yourself in a small room with a locked chest.")
        time.sleep(2)
        print("There is a note on the chest that says: 'If you want to go and open the chest, you must answer a riddle.'")
        print("")
        time.sleep(2)
        print("The riddle is: 'What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?'")
        print("Write your answer below:")

        room2_answer = input("Enter your answer: ")

        if room2_answer.lower() == "river":
            print("")
            print("Correct! The chest opens and you find a coin inside.")
            time.sleep(2)
            print("You take the coin and leave the room.")
            print("")
            coin_to_room_3 = True
            room = 'room 1'
        else:
            print("Incorrect! You have died instantly.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(2)
            again = input("Do you want to play again? (yes/no): ")

            if again.lower() == "yes":
                keys = 0
                room = 'starting'
                coin_to_room_3 = False
                room1_quiz_answered = False
            else:
                print("Thx for playing! <3")
                game_running = False


    elif room == 'room 3_before':

        if coin_to_room_3 == True:
            print("You have a coin to enter this room. You can now enter the room.")
            time.sleep(2)
            room = 'room 3'
        else:
            print("You don't have a coin to enter this room. You must go back to the starting room and find a coin first.")
            room = 'room 1'


    elif room == 'room 3':
        time.sleep(2)

        print("You enter the third room and find yourself in a dark corridor.")
        time.sleep(2)
        print("There is a small table with a piece of paper on it that says 'To get the key, you must solve this math problem.'")
        time.sleep(2)
        print("The math problem is: 'What is 7 * 8 + 6 / 2 - 3?'")
        time.sleep(2)
        print("Write your answer below:")

        room3_answer = input("Enter your answer: ")

        if room3_answer == "56":
            print("Correct! You have won a key.")
            keys += 1
            time.sleep(2)
            print(f"You now have {keys} key(s).")
            room = 'room 4'
        else:
            print("Incorrect! You have died instantly.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(2)
            again = input("Do you want to play again? (yes/no): ")
            if again.lower() == "yes":
                keys = 0
                room1_quiz_answered = False
                coin_to_room_3 = False
                room = 'starting'
            else:
                print("Thx for playing! <3")
                game_running = False

    elif room == 'room 4':
        time.sleep(2)
        print("You enter the fourth room and find yourself in the largest room you have ever seen.")
        time.sleep(2)
        print("At the end of the room, you see a wall")
        time.sleep(2)
        print("There is a note on the wall that says: 'To get the key, you must arrange the letters in an order that forms a word. Otherwise you will die!")
        time.sleep(2)

        word = "programming"
        mixed = "".join(random.sample(word, len(word)))

        room4_answer = input(f"Arrange the letters: {mixed}     ")
        print("")

        if room4_answer.lower() == word:
            print("Correct! You have won a key.")
            keys += 1
            time.sleep(2)
            print(f"You now have {keys} key(s).")
            room = 'starting2'

        else:
            print("Incorrect! You have died instantly.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(2)
            again = input("Do you want to play again? (yes/no): ")
            if again.lower() == "yes":
                keys = 0
                room1_quiz_answered = False
                coin_to_room_3 = False
                room = 'starting'
            else:
                print("Thx for playing! <3")
                game_running = False

    elif room == 'starting2':
        print("You have returned to the starting room.")
        time.sleep(2)
        print("You see the smaller doors with 3 locks again.")
        time.sleep(2)
        print('You have exactly 3 keys now.')
        time.sleep(2)
        print('You enter the small doors')
        room = 'winning room'
     
    elif room == 'winning room':
        time.sleep(2)

        if keys == 3:

            print("You insert three keys into the keyholes and turn them...")
            time.sleep(2)
            print("The doors open and you step inside...")
            time.sleep(2)
            print("You walk in and see a strange, glowing portal in the middle of a small room...")
            time.sleep(2)
            print("Without a second thought (since youre already tired of it all (×_×)), you step into the portal and...")
            time.sleep(2)
            print("You wake up in bed in your own home, as if nothing had happened.")
            time.sleep(2)
            print("You look around and see that everything is normal, but you cant shake the feeling that something is off...")
            time.sleep(2)
            print("Well, its probably nothing.")
            time.sleep(2)
            print("You have won the game!")

            game_running = False

        else:
            print("You dont have enough keys to open the doors. You must go back and find more keys.")
            room = 'starting'

