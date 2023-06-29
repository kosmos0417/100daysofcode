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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You have to ways to go: right and left.")
a = input("Which do you prefer?")
if a == "Left":
    print("Hooray? You find some food")

    print("You've got two options: Swim or Wait?")
    a = input()

    if a == "Wait":
        print("That's the right choice!")
        print("Well done.")

        print("After some amount of time near of you appeares three mistical doors.")
        a = input("Which: REd, Blue or Yellow?")

        if a == "Yellow":
            print("You won this life. You enter thid door and suddenly relocate to your home.")
            print("Congrats")

        elif a == "Blue":
            print("Somehow you relocate to the centr of ocean and there's no way back.")
            print("After while time you finally sink.")
            print("Game over.")

        elif a == "Red":
            print("Game over")


    elif a == "Swim":
        print("The river's flow was too harsh and you can't survive")
        print("Game over.")


elif a == "Right":
    print("There is a tiger and you died...")
    print("Game over.(")



