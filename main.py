print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

input1 = input("You're at a cross road. Where do you want to go? Type left or right\n")
if input1 == "right":
    print("You got hit by a car and died.")
    print("GAME OVER!!!")
elif input1 == "left":
    input2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if input2 == "swim":
        print("You got eaten by an alligator")
        print("GAME OVER!!!")
    elif input2 == "wait":
        input3 = input("You look around and find a boat. You use the boat to travel to the island There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if input3 == "red":
            print("You got bit by a king cobra and died")
            print("GAME OVER!!!")
        elif input3 == "blue":
            print("You got eaten by a bear")
            print("GAME OVER!!!")
        elif input3 == "yellow":
            print("You found the treasure!!!")
            print("YOU WON!!!")

