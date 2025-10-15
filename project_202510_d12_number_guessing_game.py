## Day 12
## Project: Number Guessing Game

'''
https://appbrewery.github.io/python-day12-demo/

Instructions:
- Build a number higher lower guessing game

### PRE WORK ###
1. Set up libraries, global variables, defined constants, csv input/output variables, functions
2. Draw flowchart programming
3. Write psuedocode (by hand)
4. Make pseudocode into comments

### BRAINSTORM ###

(see flowchat on Goodnotes)

#### LEARNINGS ####


'''

######## Import libraries or own files ############
#import random #Import random Python library or self-created python files
#import random #import gavel_art.py python file
import math
import random

########## Declare Global Variables ##################
#List variables, for each of letters, numbers, symbols
num = 0 #answer, pulled from random function
difficulty = "" #string variable type, hold user input: 'easy' or 'hard'
attempts_remaining = 0 #int variable - to hold # of attempts remaining
guess = 0 #user guess

####### Defined Constants #############
#NA

#### CSV Input/Output Variables #######
#NA

############### Functions ##############

### VARIABLES HOLDING FUNCTIONS ########


####################

def main():
    print_intro()
    set_game_difficulty()
    play_game()

def print_intro():
    global num #Name global variables to define in local scope
    print("Welcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    #pull random number for game instance
    num = random.randint(1, 100) #Return random integer between named a(1) and b(100) 


def set_game_difficulty():
    global difficulty, attempts_remaining #Name global variables to define in local scope

    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    
    while difficulty != 'easy' or difficulty != 'hard':
        if difficulty == 'easy' or difficulty == 'hard': #if then to keep checking so that once difficulty DOES equal easy or hard, it will BREAK out of loop
           break
        else:
            print("You didn't select a difficulty. Try again.")
            difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

    if difficulty == "easy":
        attempts_remaining = 10
        print(attempts_remaining)
    elif difficulty == "hard":
        attempts_remaining = 5
        print(attempts_remaining)


def play_game():
    global attempts_remaining, guess #Name global variables to define in 
    
    while attempts_remaining > 0: #WHILE LOOP until no more attempts remaining
        print(f'You have {attempts_remaining} attempts remaining to guess the answer.')
        guess = int(input("Make a guess: ")) #Request USER INPUT for integer guess

        if guess == num: #WIN
            print("You win!")
            break #BREAK OUT OF WHILE LOOP that it's inside in
        elif guess < num: #LOSE, GUESS IS TOO LOW
            print("Guess is too low. Guess again.")
            attempts_remaining -= 1 #Decrement attempts remaining by 1
            #RESTART LOOP 
        elif guess > num: #LOSE, GUESS IS TOO HIGH
            print("Guess is too high. Guess again.")
            attempts_remaining -= 1 #Decrement attempts remaining by 1 
            #RESTART LOOP

    if attempts_remaining == 0: #As attempts_remaining has gone to 0 and user HAS NOT won
        print("You lose. No more attempts remaining.")

    #otherwise, arrived because have won. 

main()
