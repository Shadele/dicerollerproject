#diceroller.py has the base files for the dice roller

'''Current project goals 3/22/22:
1. Main menu
2. Select sides of dice
3. Select number of dice
4. Select modifier (+1, +2, etc)
5. Total
6. History of dice rolls? Maybe? Like the results of the last 10 rolls
7. Exit
'''
from random import randint

def menu_selection():
    print("1. Start rolling dice!\n2. See your roll history!\n3. Exit.")

def main_menu():
    while True:
        print("Welcome to the Dice Roller!\nPlease select a menu option.")
        menu_selection()
        menu_choice = input()
