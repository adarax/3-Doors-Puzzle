import doors
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
switchedWins = 0

# Specify number of iterations
iterations = 10000

for i in range(iterations):
    progress = ((i + 1) / iterations) * 100
    if progress % 1 == 0:
        clear()
        print("Progress: " + str(round(progress, 2)) + "%")
    result = doors.game(random.randint(1, 3)) # Switch is always true
    
    if result:
        switchedWins += 1

switchedLosses = iterations - switchedWins

print("\nResults:\n")
print("Switched wins: " + str(switchedWins) + "\nSwitched losses: " + str(switchedLosses) + "\n")
print("Win rate when switiching: " + str((switchedWins / iterations) * 100) + "%\n")