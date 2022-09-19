import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game(): # For user input
    clear()
    doors = [1, 2, 3]
    prizeIndex = random.randint(0, 2)
    firstChoice = None

    while firstChoice not in doors:
        try:
            firstChoice = int(input("Pick a door: 1, 2, or 3\nChoice: "))
            if firstChoice not in doors:
                print("Please pick a valid door.")
            else:
                continue
        except ValueError:
            print("Invalid input. Try again.")

    openedDoor = None

    for i in doors:
        if i is not firstChoice and i is not doors[prizeIndex]:
            openedDoor = i
            doors.remove(i)
            break    

    doors.remove(firstChoice)
    remainingDoor = doors[0]

    choseSwitch = input("Door " + str(openedDoor) + " was opened.\nSwitch doors? (Y/N)\nChoice: ")

    switched = (choseSwitch == "Y" or choseSwitch == "y")
    won = False

    if switched:
        print("You chose to switch to door " + str(remainingDoor) + ".")
        if remainingDoor == prizeIndex + 1:
            won = True
            print("You got the prize!")
        else:
            print("You lost.")
    else:
        if firstChoice == prizeIndex + 1:
            won = True
            print("You got the prize!")
        else:
            print("You lost.")

    return [switched, won]

def game(choice, switch): # For automated testing
    doors = [1, 2, 3]
    prizeIndex = random.randint(0, 2)

    firstChoice = choice

    for i in doors:
        if i is not firstChoice and i is not doors[prizeIndex]:
            doors.remove(i)
            break    

    doors.remove(firstChoice)
    remainingDoor = doors[0]

    switched = switch
    won = False

    if switched:
        if remainingDoor == prizeIndex + 1:
            won = True
    else:
        if firstChoice == prizeIndex + 1:
            won = True

    return [switched, won]

# For user input
# game()
