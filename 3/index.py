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

print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")

def get_choice(option):
    choice = input().lower()

    if choice in valid_choices[option]:
        return valid_choices[option][choice]()
    
    print("You've chosen an invalid option. Please try again.")
    return get_choice(option)

def call_second_choice (): 
    print("You've come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")

    return get_choice("second_choice")


def call_third_choice():
    print("You find a boat and row to the island.")
    print("You've come to a house with 3 doors. One red, one yellow, and one blue. Which door do you choose?")

    return get_choice("third_choice")
    
valid_choices = {
    "first_choice": {
        "left": lambda: call_second_choice(),
        "right": lambda: print("The road ends and you fall off a cliff.")
    },
    "second_choice": {
        "swim": lambda: print("You've been eaten by a shark."),
        "wait": lambda: call_third_choice()
    },
    "third_choice": {
        "red": lambda: print("You've been burned by fire."),
        "blue": lambda: print("You've been eaten by a beast."),
        "yellow": lambda: print("You've found the treasure!")
    }
}


get_choice("first_choice")



    