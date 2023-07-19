from time import sleep as slp

def pause(seconds):
    slp(seconds)

#prints message to the console and stops until users presses enter
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


###############################

print_and_stop("hello")

print_new_line()

print_and_pause("i will pause for...", 5)

print_and_pause("i will pause for...", 2)

print_and_pause("i will pause for...", 2)

print_and_pause("i will pause for...", 2)





