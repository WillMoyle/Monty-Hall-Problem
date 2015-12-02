# MONTY HALL PROBLEM
# Author: Will Moyle
# Last modified: 2nd December 2015

This Python console program allows the user to automatically or manually play the so called Monty Hall problem ("https://en.wikipedia.org/wiki/Monty_Hall_problem"). There are a set number of doors. Behind one is a prize. The player selects one door. The computer then randomly opens a given number of doors. The player can then choose to switch to the other unopened door or stick with their initial choice. Probability dictates that the player should always switch, this program verifies that.

The user can input the number of doors, the number of doors that the computer opens and the number of rounds that can be played. The user then decides if the game should be played automatically or manually. If the game is played automatically, the user is then asked whether the computer should always switch or always stick.

According to D. L. Ferguson (1975 in a letter to Selvin cited in (Selvin 1975b)), given an N-door problem, with the computer opening P wrong doors, the probability of winning if the user switches is:

(N - 1) / (N(N-p-1))

This formula is tested if the game is played automatically.