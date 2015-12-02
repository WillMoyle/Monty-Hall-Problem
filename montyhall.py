# Monty Hall Problem

import random as rdm

def problem(switch, manual = False):

    doors = range(3)
    for i, _ in enumerate(doors):
        doors[i] += 1

    win = rdm.choice(doors)
    choice = 0
    
    if manual:
        choice = getChoice(doors)
    else:
        choice = rdm.choice(doors)

    opened = 0
    closed = 0
    doors.remove(choice)
    
    if choice == win:
        opened = rdm.choice(doors)
        doors.remove(opened)
        closed = doors[0]
    else:
        closed = win
        doors.remove(closed)
        opened = doors[0]

    if manual:
        manual_switch = getSwitch(opened, choice, closed)
        if manual_switch:
            choice = closed
    elif switch:
        choice = closed

    if choice == win:
        return True
    return False


def getChoice(doors):
    choice_str = raw_input('Choice (1 - ' + str(len(doors)) + '): ')
    try:
        choice = int(choice_str)
    except ValueError:
        choice = 0
    while choice not in doors:
        choice_str = raw_input('Choice (1 - ' + str(len(doors)) + '): ')
        try:
            choice = int(choice_str)
        except ValueError:
            choice = 0
    return choice

def getSwitch(opened, choice, closed):
    message = 'Opened door ' + str(opened)
    message += '. Keep with door ' + str(choice)
    message += ', or switch to door ' + str(closed) + '? (K/S)'
    manual_switch = raw_input(message)
    while manual_switch not in ['K', 'S', 'k', 's']:
        manual_switch = raw_input('Try again: ')
    if manual_switch in ['K', 'k']:
        return False
    return True


def main():
    attempts = 100000
    wins = 0
    
    for _ in range(attempts):
        if problem(True):
            wins += 1

    print 'Wins: ' + str(wins)
    print 'Attempts: ' + str(attempts)
    print 'Win rate: ' + str((100 * wins) / attempts) + '%'


    attempts = 100000
    wins = 0
    
    for _ in range(attempts):
        if problem(False):
            wins += 1

    print 'Wins: ' + str(wins)
    print 'Attempts: ' + str(attempts)
    print 'Win rate: ' + str((100 * wins) / attempts) + '%'

main()