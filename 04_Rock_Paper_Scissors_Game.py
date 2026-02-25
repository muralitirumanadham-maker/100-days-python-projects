import random

hands = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

while True:

    choice = int(input("\nType 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if choice > 2 or choice < 0:
        print("Invalid Choice ❌")

    else:
        computer = random.randint(0, 2)

        print("\nYou chose:")
        print(hands[choice])

        print("Computer chose:")
        print(hands[computer])

        # Result
        if choice == computer:
            print("Draw 🤝")

        elif (
            (choice == 0 and computer == 2) or
            (choice == 1 and computer == 0) or
            (choice == 2 and computer == 1)
        ):
            print("You Win 🎉")

        else:
            print("You Lose 😢")

    ch = input("\nPlay again? Type 'yes' : ").lower()

    if ch != "yes":
        print("Game Over 👋")
        break
