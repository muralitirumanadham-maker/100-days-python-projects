print(r'''
                  ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-"""'
''')
print("Welcome to Treasure Island\nYou're mission is to find the treasure")
choice=input("You're at a cross road.where do you want to go?\n  Type 'left' or 'right' ").lower()
if choice=="left":
    p=input("You have come to lake.There is an island in the middle of the lake.\n  Type 'wait' to wait for a boat. Type 'swim' to swim accross ").lower()
    if p=="wait":
        c=input("You arrive at the island unharmed. There is a how with 3 doors. \n One red,one yellow and one blue.Which colour do you choose:").lower()
        if c=="red":
            print("Game over!!!")
        elif c=="yellow":
            print("You win!!! you found the treasure")
        else:
            print("Game over!!!")
    else:
        print("you have been eaten by a shark!! Game over!!!")
else:
    print("You choosed the wrong direction! GAME OVER!!!")
