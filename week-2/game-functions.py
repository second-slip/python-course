from time import sleep as slp
import random

########################################################
def pause(seconds):
    slp(seconds)

def print_and_stop(message):
    print(message)
    input("press 'enter' to continue")

# prints message to the console and pauses for x seconds
def print_and_pause(message, seconds):
    print(message)
    pause(seconds)

# prints new line
def print_new_line():
    print('\n')

###########################################################

def capture_int_response():
    response = input("Hint: type your answer as an integer (e.g: 1 or 2 or 3) here: ")
    return int(response) if response.isdigit() else None
  

def challenge_four():
    print(f"What is {1} + {2}?");
    answer = capture_int_response()
    if (answer is None):
        print("Your response must be an integer number!\n")
        challenge_four()
    
    print("ok")

challenge_four()
