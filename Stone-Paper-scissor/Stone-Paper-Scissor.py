import random
computer = random.randint(1, 3)
user_input = input("choose one of the number:  1.ROCK  2.PAPER  3.SCISSOR\n")
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
       ROCK """)
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
     SCISSOR""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    PAPER""")
game_image = [rock, paper, scissor]
print(f"you chooses{game_image[int(user_input ) -1]}")
if int(user_input) == computer:
    print("DRAW...")
elif int(user_input) != computer:
    if int(user_input) == 1:
        if computer == 1:
            print("draw")
        if computer == 2:
            print("you loose")
        if computer == 3:
            print("you win")
    if int(user_input) == 2:
        if computer == 1:
            print("you win")
        if computer == 2:
            print("draw")
        if computer == 3:
            print("you loose")

    if int(user_input) == 3:
        if computer == 1:
            print("you loose")
        if computer == 2:
            print("you win")
        if computer == 3:
            print("draw")
print(f"computer chooses {game_image[computer -1]}")
