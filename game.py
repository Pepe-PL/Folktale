# Made by Patryk Powirski (Pepe-PL) 2026


#  The Game Plan :)
#
#      [Winning room] <- [starting room] -> [room 1] -> [room 3] -> [room 4]
#        [3 keys]                            [test]      [test]
#           |                                 |   ^     
#           V                                 |   |     
#     [Winning room]                          V   |
#                                           [room 2]           

import time
import random


def narration(*lines, delay=2):
    """Print lines of text sequentially with a pause between each line."""
    for line in lines:
        if isinstance(line, tuple):
            text, custom_delay = line
            print(text)
            time.sleep(custom_delay)
        else:
            print(line)
            time.sleep(delay)


# Game State Variables
room = 'starting'
keys = 0
coin_to_room_3 = False
room1_quiz_answered = False
game_running = True

while game_running:
    # ---------------------------------------------------------
    # Starting Room: Wake up in the dark and choose an initial path
    # ---------------------------------------------------------
    if room == 'starting':
        narration(
            "You have woken up in a strange place...",
            "You dont know where you are...",
            "You look around, but you cant see anything because its dark...",
            ("However, next to the bed youre in, you spot a light...", 3),
            "It turns out to be a torch...",
            "You pick it up and stand up.",
            ("In front of you is massive doors, and behind you, a smaller one with 3 locks.", 3),
        )
        print('If you want to enter the massive doors, enter "1". If you want to try to open the smaller doors, enter "2".')

        answer = input("1-2: ")

        if answer == "1":
            room = 'room 1'
        elif answer == "2":
            room = 'winning room'
        else:
            print("Invalid input. Please enter '1' or '2'.")

    # ---------------------------------------------------------
    # Room 1: Large hall with quiz machine and exits to rooms 2, 3, or back
    # ---------------------------------------------------------
    elif room == 'room 1':
        narration(
            "",
            "You enter the massive doors and find yourself in a large hall.",
            "There are two doors in front of you, one to the left and one to the right.",
            "Also in the room, you see a table with a small machine on it.",
            'On the machine there is a note that says: "Win a key by answering a question correctly. If you answer incorrectly, you will die instantly."',
        )
        print("")
        time.sleep(2)
        print('If you want to answer the question, enter "1". If you want to go through the left door, enter "2". If you want to go through the right door, enter "3". If you want to turn back and go back to the starting room, enter "4".')

        answer = input("1-4: ")

        if answer == "1":
            if room1_quiz_answered:
                narration(
                    "You have already answered the question in this room. You cannot answer it again.",
                    "You must choose another option.",
                )
                room = 'room 1'
            else:
                narration(
                    "You approach the machine and read the question on the screen.",
                    "The question is: 'What is the capital of Australia?'",
                )
                quiz_options = [
                    'If you want to answer "Canberra", enter "1".',
                    'If you want to answer "Sydney", enter "2".',
                    'If you want to answer "Melbourne", enter "3".',
                    'If you want to answer "Brisbane", enter "4".',
                ]
                for option in quiz_options:
                    print(option)

                room1_answer = input("Enter your answer: ")

                if room1_answer == "1":
                    print("")
                    print("Correct! You have won a key.")
                    room1_quiz_answered = True
                    keys += 1
                    time.sleep(2)
                    print(f"You now have {keys} key(s).\n")

                elif room1_answer in ("2", "3", "4"):
                    print("")
                    narration(
                        "Incorrect! You have died instantly.",
                        "Game Over.",
                    )
                    room1_quiz_answered = True
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

    # ---------------------------------------------------------
    # Room 2: Chest room with a riddle to obtain the coin
    # ---------------------------------------------------------
    elif room == 'room 2':
        narration(
            "You enter the doors and find yourself in a small room with a locked chest.",
            "There is a note on the chest that says: 'If you want to go and open the chest, you must answer a riddle.'\n",
            "The riddle is: 'What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?'",
        )
        print("Write your answer below:")

        room2_answer = input("Enter your answer: ")

        if room2_answer.lower() == "river":
            print("")
            narration(
                "Correct! The chest opens and you find a coin inside.",
                "You take the coin and leave the room.\n",
            )
            coin_to_room_3 = True
            room = 'room 1'
        else:
            narration(
                "Incorrect! You have died instantly.",
                "Game Over.",
            )
            again = input("Do you want to play again? (yes/no): ")

            if again.lower() == "yes":
                keys = 0
                room = 'starting'
                coin_to_room_3 = False
                room1_quiz_answered = False
            else:
                print("Thx for playing! <3")
                game_running = False

    # ---------------------------------------------------------
    # Room 3 Check: Gatekeeper requiring coin from room 2
    # ---------------------------------------------------------
    elif room == 'room 3_before':
        if coin_to_room_3:
            narration("You have a coin to enter this room. You can now enter the room.")
            room = 'room 3'
        else:
            print("You don't have a coin to enter this room. You must go back to the starting room and find a coin first.")
            room = 'room 1'

    # ---------------------------------------------------------
    # Room 3: Math puzzle room to win the 2nd key
    # ---------------------------------------------------------
    elif room == 'room 3':
        narration(
            "",
            "You enter the third room and find yourself in a dark corridor.",
            "There is a small table with a piece of paper on it that says 'To get the key, you must solve this math problem.'",
            "The math problem is: 'What is 7 * 8 + 6 / 2 - 3?'",
        )
        print("Write your answer below:")

        room3_answer = input("Enter your answer: ")

        if room3_answer == "56":
            print("Correct! You have won a key.")
            keys += 1
            time.sleep(2)
            print(f"You now have {keys} key(s).")
            room = 'room 4'
        else:
            narration(
                "Incorrect! You have died instantly.",
                "Game Over.",
            )
            again = input("Do you want to play again? (yes/no): ")
            if again.lower() == "yes":
                keys = 0
                room1_quiz_answered = False
                coin_to_room_3 = False
                room = 'starting'
            else:
                print("Thx for playing! <3")
                game_running = False

    # ---------------------------------------------------------
    # Room 4: Anagram / word scramble puzzle to win the 3rd key
    # ---------------------------------------------------------
    elif room == 'room 4':
        narration(
            "",
            "You enter the fourth room and find yourself in the largest room you have ever seen.",
            "At the end of the room, you see a wall",
            "There is a note on the wall that says: 'To get the key, you must arrange the letters in an order that forms a word. Otherwise you will die!",
        )

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
            narration(
                "Incorrect! You have died instantly.",
                "Game Over.",
            )
            again = input("Do you want to play again? (yes/no): ")
            if again.lower() == "yes":
                keys = 0
                room1_quiz_answered = False
                coin_to_room_3 = False
                room = 'starting'
            else:
                print("Thx for playing! <3")
                game_running = False

    # ---------------------------------------------------------
    # Starting Room 2: Return with all 3 keys
    # ---------------------------------------------------------
    elif room == 'starting2':
        narration(
            "You have returned to the starting room.",
            "You see the smaller doors with 3 locks again.",
            "You have exactly 3 keys now.",
            "You enter the small doors",
        )
        room = 'winning room'

    # ---------------------------------------------------------
    # Winning Room: Check for 3 keys and display victory ending
    # ---------------------------------------------------------
    elif room == 'winning room':
        time.sleep(2)

        if keys == 3:
            narration(
                "You insert three keys into the keyholes and turn them...",
                "The doors open and you step inside...",
                "You walk in and see a strange, glowing portal in the middle of a small room...",
                "Without a second thought (since youre already tired of it all (×_×)), you step into the portal and...",
                "You wake up in bed in your own home, as if nothing had happened.",
                "You look around and see that everything is normal, but you cant shake the feeling that something is off...",
                "Well, its probably nothing.",
                "You have won the game!",
            )
            game_running = False

        else:
            print("You dont have enough keys to open the doors. You must go back and find more keys.")
            room = 'starting'
