from time import sleep as slp
import random

########################################################
# Health system

players_lives = 0  # property to track player's lives


# function to add x lives to players_lives
def add_lives(num_lives):
    global players_lives
    players_lives = players_lives + num_lives
    return


# function to subtract x lives to players_lives
def subtract_lives(num_lives):
    global players_lives
    players_lives = players_lives - num_lives
    return


# possible cool extra: find a boun that doubles player's lives
def double_lives_bonus():
    players_lives = players_lives * 2
    return


def check_if_game_over():
    if players_lives == 0:
        game_over()
    else:
        print_and_stop(f"You have {players_lives} lives left.")


def game_over():
    print("You are dead GAME OVER!!!!!!!!!!")
    quit()


############################################

###########################################
# Relic system

players_relics = []  # property to track player's lives


# function to add x lives to players_lives
def add_relic(relic_type):
    global players_relics
    players_relics.append(relic_type)
    return


# function to subtract x lives to players_lives
def remove_relic(relic_type):
    global players_relics
    players_relics.remove(relic_type)
    return


def what_relics_do_I_have():
    print(f"you have the following relics: {players_relics}")


##############################################
def level_one_path_choice():
    print("Level 1 - Path Option")

    print("Your options are:")
    print("A: Living room")
    pause(1)
    print("B: kitchen")
    pause(1)
    print("C: bedroom")
    pause(1)
    print("D: hallway")
    pause(1)
    print("E: optional room")

    path = input("type 'a', 'b', 'c', 'd', 'e'")

    match path:
        case "a":
            print("you gained a WHATEVER relic")
            add_relic("whatever")
        case "b":
            print("you gained 2 WHATEVER relics")
            add_relic("whatever")
            add_relic("whatever")
        case "c":
            print("sorry, no relics here!")
        case "d":
            print("you gained a DIFFERENT relic")
            add_relic("different")
        case "e":
            print("you gained a WHATEVER relic")
            add_relic("whatever")

    # tODO: pluralise sentence when necessary
    print(f"You have {len(players_relics)} relic(s).")
    print(players_relics)
    print_and_stop("")


############################################
def print_and_stop(message):
    print(message)
    input("press 'enter' to continue")


def print_and_pause(message, seconds):
    print(message)
    pause(seconds)

def print_new_line():
    print('\n')

def level_complete(level):
    if len(players_lives) > 1:
        print(f"You have successfully completed level {level} with {players_lives} lives left!")
    else:
        print(f"You have successfully completed level {level} with {players_lives} life left!")

##########################################


def choose_difficulty_level():
    difficulty_level = int(input("type:\n1 for easy\n2 for medium\n3 for hard"))

    match difficulty_level:
        case 1:
            add_lives(5)
        case 2:
            add_lives(4)
        case 3:
            add_lives(3)
        case _:
            # todo
            print("Your reponse was not valid............................")

    print(f"you are ready to start with {players_lives} lives")


def pause(seconds):
    slp(seconds)


################################
# challenge 1


def challenge_one():
    print_and_stop("######### CHALLENGE 1 ###########")
    print("Challenge one: what is the capital of France?")
    pause(1)
    print("1: London")
    pause(1)
    print("2: Paris")
    pause(1)
    print("3: Sydney")
    answer = int(input("type '1', '2' or '3'..."))

    match answer:
        case 1:  # WRONG ANSWER (B)
            print("oh, no you got it wrong!  You lose 1 life")
            subtract_lives(1)
        case 2:  # if RIGHT ANSWER
            print("right answer.  You don't lose any lives")
        case 3:  # WRONG ANSWER (B)
            print("oh, no you got it wrong!  You lose 1 life")
            subtract_lives(1)

    check_if_game_over()


################################
# challenge 2
def challenge_two():
    print_and_stop("######### CHALLENGE 2 ###########")

    num1 = random.randint(1, 20)
    num2 = random.randint(5, 30)

    answer = int(input(f"type the answer to: what is {num1} + {num2}?"))

    correct_answer = num1 + num2

    if answer != correct_answer:
        print_and_pause(
            f"oh, no you got it wrong!  The correct answer is: {correct_answer}.  You lose 1 life",
            2
        )
        subtract_lives(1)
    else:
        print_and_pause("You it right.  You keep your lives...", 2)

    check_if_game_over()


########################################################
# MAIN

# --> print_then_stop
# --> print_then_pause

print_and_stop("Welcome to LOST IN NIGHTMARES")

choose_difficulty_level()

# LEVEL 1
pause(2)

challenge_one()

pause(2)

level_one_path_choice()

pause(2)

print_new_line()

challenge_two()

level_complete(1)
# LEVEL 2


# can go go level
#     print_and_stop(f"You have {players_lives} lives left, enought to go to LEVEL 2")
