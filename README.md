# Folktale RPG

A text-based interactive adventure and puzzle RPG built in Python for the HackClub Folktale project.  
Created by **Patryk Powirski (Pepe-PL)**.

---

## 📖 Story & Overview

You awaken in an unfamiliar, pitch-black room with nothing but a torch. In front of you stands a massive door leading into a maze of mystery rooms; behind you is a door secured with three heavy locks.

To escape and find your way back home, you must navigate through several rooms, solve riddles, trivia, math challenges, and word anagrams to collect all 3 keys.

---

## 🗺️ Game Map

```
[Winning Room] <--- [Starting Room] ---> [Room 1: Quiz] ---> [Room 3: Math] ---> [Room 4: Anagram]
  (3 keys req.)                                |    ^
                                               |    |
                                               V    |
                                         [Room 2: Riddle (Coin)]
```

- **Starting Room**: The initial chamber. Choose to enter Room 1 or attempt opening the 3-lock exit door.
- **Room 1**: A grand hall featuring a trivia challenge for the 1st key, and doors leading to Room 2, Room 3, or back to Start.
- **Room 2**: A locked chest containing a special coin guarded by a riddle.
- **Room 3**: A dark corridor accessible only with the coin from Room 2; solve the math problem to obtain the 2nd key.
- **Room 4**: A massive hall containing a scrambled word challenge to win the 3rd key.
- **Winning Room**: Insert all 3 keys into the locks to open the glowing portal and win the game!

---

## 🚀 How to Run

### Requirements
- Python 3.9 or newer (uses standard library modules only: `time`, `random`).

### Run Command
Run the game directly from your terminal:
```bash
python3 game.py
```

---

## 🎮 How to Play

1. Read the narration and prompts carefully.
2. Enter the number corresponding to your chosen action or answer (e.g., `1`, `2`, `3`, `4`).
3. For text and riddle prompts, type your answer and press `Enter`.
4. Be careful: incorrect puzzle answers may lead to instant game over! You will be given the option to try again if you perish.

---

## 🧪 Testing

Automated tests can be run using Python's standard `unittest` framework:
```bash
python3 -m unittest -v
```
