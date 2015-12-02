# MONTY HALL PROBLEM
# Author: Will Moyle
# Last modified: 2nd December 2015

# This Python console program allows the user to automatically or manually
# play the so called Monty Hall problem ("https://en.wikipedia.org/wiki/Monty_Hall_problem")

# There are a set number of doors. Behind one is a prize. The player selects
# one door. Another door is then opened that does not contain the prize. The
# player can then choose to switch to the other unopened door or stick with their
# initial choice. Probability dictates that the player should always switch, this
# program verifies that.

from __future__ import division
import random as rdm


# START OF FUNCTION: problem
# Primary function for simulating the Monty Hall problem
# Parameters:
#     switch (boolean value stating whether the program should automatically sitch)
#     manual (boolean value for whether the input should be manual or automatic)
# Returns:
#     True if the user wins, else returns False
def problem(num_doors, switch, manual = False):

    doors = range(num_doors)
    for i, _ in enumerate(doors):
        doors[i] += 1

    win = rdm.choice(doors)
    choice = 0
    
    # choose a door to open
    if manual:
        choice = getChoice(doors)
    else:
        choice = rdm.choice(doors)
    
    # open one of the closed doors
    doors.remove(choice)
    opened = rdm.choice(doors)
    while opened == win:
        opened = rdm.choice(doors)
    doors.remove(opened)

    # choose whether or not to open the other door
    if manual:
        manual_switch = getSwitch(opened, choice, doors)
        if manual_switch:
            choice = rdm.choice(doors)
    elif switch:
        choice = rdm.choice(doors)

    if choice == win:
        return True
    return False
# END OF FUNCTION



# START OF FUNCTION: getChoice
# Allows the user to manually choose a door from the parameter 'doors'
def getChoice(doors):
    choice_str = raw_input('Choice ' + str(doors) + ': ')
    try:
        choice = int(choice_str)
    except ValueError:
        choice = 0
    while choice not in doors:
        choice_str = raw_input('Choice ' + str(doors) + ': ')
        try:
            choice = int(choice_str)
        except ValueError:
            choice = 0
    return choice
# END OF FUNCTION



# START OF FUNCTION: getSwitch
# Allows the user to manual choose whether or not to switch the doors
def getSwitch(opened, choice, closed):
    message = 'Opened door ' + str(opened)
    message += '. Keep with door ' + str(choice)
    message += ', or switch to door ' + str(closed) + '? (K/S) '
    manual_switch = raw_input(message)
    while manual_switch not in ['K', 'S', 'k', 's']:
        manual_switch = raw_input('Try again: ')
    if manual_switch in ['K', 'k']:
        return False
    return True
# END OF FUNCTION



# START OF FUNCTION: getIntInput
# Allows the user to manually choose an integer with a given message and min value
def getIntInput(min_val, message):
    choice_str = raw_input(message)
    try:
        choice = int(choice_str)
    except ValueError:
        choice = 0
    while choice < min_val:
        choice_str = raw_input('Try again: ')
        try:
            choice = int(choice_str)
        except ValueError:
            choice = 0
    return choice
# END OF FUNCTION



# START OF FUNCTION: getBoolean
# Allows the user to manually choose an boolean with a given message (using Y/N)
def getBoolean(message):
    input = raw_input(message)
    while input not in ['Y', 'y', 'N', 'n']:
        input = raw_input('Try again: ')
    if input in ['Y', 'y']:
        return True
    return False
# END OF FUNCTION


def main():
    
    num_doors = getIntInput(3, "How many doors are there? ")
    attempts = getIntInput(1, "How many rounds should be played? ")
    manual = getBoolean("Do you wish to play manually (Y/N)? ")
    switch = False
    if not manual:
        switch = getBoolean("Do you want the computer to automatically switch (Y/N)? ")
    wins = 0
    
    for _ in range(attempts):
        if problem(num_doors, switch, manual):
            wins += 1

    print 'Wins: ' + str(wins)
    print 'Attempts: ' + str(attempts)
    print 'Win rate: ' + str((100 * wins) / attempts) + '%'


main()