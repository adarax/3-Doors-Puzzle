import doors
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
switchedWins = 0
switchedLosses = 0

# Specify number of iterations
iterations = 100000

for i in range(iterations):
    progress = ((i + 1) / iterations) * 100
    
    if progress % 1 == 0:
        clear()
        print("Progress: " + str(round(progress, 2)) + "%")
    
    switchDoors = False
    result = doors.game(random.randint(1, 3), switchDoors)  # Parameters are (door number chosen, switch)
    
    if result[1]:
        switchedWins += 1
    else:
        switchedLosses += 1

print("\nResults:\n")
print("Switched wins: " + str(switchedWins) +
      "\nSwitched losses: " + str(switchedLosses) + "\n")
print("Win rate when " + ("" if result[0] else "not ") + "switiching doors: " +
      str((switchedWins / (switchedWins + switchedLosses)) * 100) + "%\n")
