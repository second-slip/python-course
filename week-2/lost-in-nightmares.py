from time import sleep as slp
import random


##############################################
# standard messages
WRONG_ANSWER = "Oh, no: You got it wrong!  You lose 1 life..."
RIGHT_ANSWER = "Yay!  You got it right.  You keep all your lives..."
INALID_RESPONSE_INT = "Your response is not valid.  Type an integer"
INALID_RESPONSE_YES_NO = (
    "Your repose is invalid.  You must type either 'yes' or 'no'..."
)

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

def lose_all_lives():
    global players_lives
    players_lives = 0
    return


# possible cool extra: find a boun that doubles player's lives
def double_lives_bonus():
    players_lives = players_lives * 2
    return


def check_if_game_over():
    if players_lives == 0:
        game_over()
    else:
        print_and_stop(
            f"\nYou have {players_lives} lives and {players_relics} relic(s).\n"
        )


def game_over():
    print("\nYou are lost all your lives.")
    print_and_stop("\nGAME OVER!!!!!!!!!!\n")
    quit()



###########################################
# Relic system

players_relics = 0  # property to track player's lives

# function to add x lives to players_lives
def add_relic(num_relics):
    global players_relics
    players_relics = players_relics + num_relics
    return

# function to subtract x lives to players_lives
def remove_relic(num_relics):
    global players_relics
    players_relics = players_relics - num_relics
    return


# def what_relics_do_I_have():
#     print(f"you have {players_relics} following relics")


##############################################
def level_one_room_choice(): # level 1, in house
    print_and_pause("Where will you go now?.  You can choose ONE room...", 1)

    print_and_pause("1 for the Hallway", 1)
    print_and_pause("2 for the Kitchen", 1)
    print_and_pause("3 for the Living room", 1)
    print_and_pause("4 for the Bedroom", 1)
    print_and_pause("5 for the Bathroom", 1)

    room = capture_int_response()

    match room:
        case 1:  # Hall
            print_and_pause("story...", 5)

            # plus relics (add x)
        case 2:  # Kitchen
            print_and_pause("story...", 5)

        case 3:  # Living room
            print_and_pause("story...", 5)

        case 4:  # Bedroom
            print_and_pause("story...", 5)

        case 5:  # Batchroom
            print_and_pause("story...", 5)

        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            level_one_room_choice()


    # tODO: pluralise sentence when necessary
    check_if_game_over()



#### LEVEL 2 PATH CHOICE
def level_two_path_choice(): #In Forest, choose path (3 options)
    print_and_pause("Which path do you coose to follow?.  You can choose ONE path...", 1)
    print_and_pause("1 for path 1", 1)
    print_and_pause("2 for path 2", 1)
    print_and_pause("3 for path 3", 1)

    path = capture_int_response()

    match path:
        case 1:  # Dark
            print_and_pause("story...", 5)
            lose_all_lives()
            check_if_game_over()
        case 2:  # Light 1
            print_and_pause("story...", 5)
            add_relic(1) # +1 relic
        case 3:  # Light 2
            print_and_pause("story...", 5)
            add_relic(2) # +2 relics
        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            level_two_path_choice()


def level_three_drawer_choice(): #In School, choose drawer (3 options)
    print_and_pause("Which path do you coose to follow?.  You can choose ONE drawer...", 1)

    print_and_pause("1 for drawer 1", 1)
    print_and_pause("2 for drawer 2", 1)
    print_and_pause("3 for drawer 3", 1)

    drawer = capture_int_response()

    match drawer:
        case 1:  # 
            print_and_pause("story...", 5)
            add_relic(1) # +1 relic
        case 2:  # Light 1
            print_and_pause("story...", 5)
            add_relic(2) # +2 relics
        case 3:  # Light 2
            print_and_pause("story...", 5)
            lose_all_lives()
            check_if_game_over()
        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            level_three_drawer_choice()


############################################
# prints message to the console and stops until users presses enter
def print_and_stop(message):
    print(message)
    input("press 'enter' to continue...")


# prints message to the console and pauses for x seconds
def print_and_pause(message, seconds):
    print(message)
    pause(seconds)


# prints new line
def print_new_line():
    print("\n")


def pause(seconds):
    slp(seconds)


#########################################


def level_complete(level):
    if players_lives > 1:
        print(
            f"You have successfully completed level {level} with {players_lives} lives left and {players_relics} relics!"
        )
    else:
        print(
            f"You have successfully completed level {level} with {players_lives} life left and {players_relics} relics!"
        )


##########################################

def choose_difficulty_level():
    print("\nChoose difficulty level:")
    print("1 for easy\n2 for medium\n3 for hard")

    difficulty_level = capture_int_response()

    match difficulty_level:
        case 1:
            add_lives(5)
        case 2:
            add_lives(4)
        case 3:
            add_lives(3)
        case _:
            # todo
            print(INALID_RESPONSE_INT)
            choose_difficulty_level()  # recursive function

    print_and_stop(f"\nYou are ready to start the game with {players_lives} lives.")


################################
# challenge 1: multiple choice quiz question
def challenge_four():
    print_and_pause("This is Challenge 1: a multiple choice quiz question:", 1)
    print_and_pause("What is the capital of France?", 1)
    print_and_pause("1: London", 1)
    print_and_pause("2: Paris", 1)
    print_and_pause("3: Sydney", 1)

    answer = capture_int_response()

    match answer:
        case 1:  # WRONG ANSWER (B)
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case 2:  # if RIGHT ANSWER
            print_and_pause(RIGHT_ANSWER, 1)
        case 3:  # WRONG ANSWER (B)
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            challenge_three()

    check_if_game_over()


#############################
# Challenge 3: multiple choice quiz question
def challenge_three():
    print_and_pause("This is Challenge 3: a multiple choice quiz question:", 1)
    print_and_pause("Which country has the biggest population?", 1)
    print_and_pause("1: Spain", 1)
    print_and_pause("2: Italy", 1)
    print_and_pause("3: Germany", 1)

    answer = capture_int_response()

    match answer:
        case 1:  # WRONG ANSWER
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case 2:  # WRONG ANSWER
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case 3:  # RIGHT ANSWER
            print_and_pause(RIGHT_ANSWER, 1)
        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            challenge_three()

    check_if_game_over()


################################
# challenge 5
def challenge_five():
    print_and_pause("######### CHALLENGE  ###########", 2)

    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

    print_and_pause(f"What is {num1} * {num2}?", 3)
    answer = capture_int_response()
    if answer is None:
        print("Your response must be an integer number!\n")
        challenge_five()

    correct_answer = num1 * num2

    if answer != correct_answer:
        print_and_pause(
            f"oh, no you got it wrong!  The correct answer is: {correct_answer}.  You lose 1 life",
            2,
        )
        subtract_lives(1)
    else:
        print_and_pause(RIGHT_ANSWER, 1)

    check_if_game_over()


################################
# challenge 2 maths
def challenge_two_():
    num1 = random.randint(1, 20)
    num2 = random.randint(5, 30)
    
    print_and_pause("######### CHALLENGE ###########", 2)

    print_and_pause(f"What is {num1} + {num2}?", 3)

    answer = capture_int_response()
    if answer is None:
        print("Your response must be an integer number!\n")
        challenge_two_()

    correct_answer = num1 + num2

    # todo
    # check if int

    if answer != correct_answer:
        print_and_pause(
            f"oh, no you got it wrong!  The correct answer is: {correct_answer}.  You lose 1 life",
            2,
        )
        subtract_lives(1)
    else:
        print_and_pause(RIGHT_ANSWER, 1)

    check_if_game_over()


def capture_int_response():
    response = input("Hint: type your answer as an integer (e.g: 1 or 2 or 3) here: ")
    return int(response) if response.isdigit() else None


###################################
# Challenge 1 (riddle)
def challenge_one():
    print_and_pause("This is Challenge 4: a riddle to solve:", 1)
    print_and_pause("What is x and y, but not z?", 1)
    print_and_pause("1: Option 1", 1)
    print_and_pause("2: Option 2", 1)
    print_and_pause("3: Option 3", 1)

    answer = capture_int_response()

    match answer:
        case 1:  # WRONG ANSWER
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case 2:  # WRONG ANSWER
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case 3:  # RIGHT ANSWER
            print_and_pause(RIGHT_ANSWER, 1)
        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            challenge_one()

    check_if_game_over()

######################
# Challenge 2 (riddle)
def challenge_two():
    print_and_pause("This is Challenge 6: a riddle to solve:", 1)
    print_and_pause("What is x and y, but not z?", 1)
    print_and_pause("1: Option 1", 1)
    print_and_pause("2: Option 2", 1)
    print_and_pause("3: Option 3", 1)

    answer = capture_int_response()

    match answer:
        case 1:  # RIGHT ANSWER
            print_and_pause(RIGHT_ANSWER, 1)
        case 2:  # WRONG ANSWER
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case 3:  # WRONG ANSWER
            print_and_pause(WRONG_ANSWER, 1)
            subtract_lives(1)
        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            challenge_two()

    check_if_game_over()


def find_relic_level_one():
    print_and_pause("Do you want to take the relic?", 1)

    response = input("Hint: type either 'yes' or 'no' here: ")

    response = response.lower()

    match response:
        case "yes":
            print_and_pause(
                "\nYou picked up the relic from the dirt and brushed it off, it felt... strange. It hummed with an ominous energy, but that didn't bother you. You stuffed the relic into your pocket and climbed out on the vine that came down with you and made your way home through the rain to get a better look at it.\n",
                5,
            )
            add_relic(1)
        case "no":
            print_and_pause(
                "\nYou decided to leave the relic alone; you didn't want to disturb whatever secrets it may hold, and turned to climb out with the vine that tripped you originally. As you climbed out of the hole in a huff, you noticed a new foreign weight in your left pocket - your hand entered the pocket and were shocked to find the relic inside. You were certain that you left the relic behind, and yet, here it was in your hand. You tried to drop it back down the hole and brushed it off.\n",
                1,
            )
            subtract_lives(1)
        case _:
            print_and_pause(INALID_RESPONSE_YES_NO, 1)
            find_relic_level_one()

    check_if_game_over()


########################################################
# MAIN

print_and_stop("Welcome to LOST IN NIGHTMARES\n")

choose_difficulty_level()


### LEVEL 1 ############ FOREST ###################

# story start
print_and_pause(
    "\nYour name is Harvey Staker - an experienced hunter who fended for himself in the middle of nowhere. It was late, and you were tired from a hard day of poaching.\n",
    5,
)

print_and_pause(
    "On your usual route home, a heavy storm began to pick up, you thought it would be best to hurry so you wouldn't get soaked. As you scurried on back to your house, you tripped over an old, thick vine that laced the blackening soil beneath a decaying tree. You fell through the ground with a hefty thump, groaning in pain and shock as you hit the bottom. You sit up and shake your head, letting your vision realign itself for a moment.\n",
    5,
)

print_and_pause(
    "Once your vision returned, you noticed a dark looking object at the end of the room, it looked like an ancient relic.\n",
    5,
)

find_relic_level_one()

# story
print_and_pause(
    "\nAfter half an hour of walking, you finally reached your home. It was locked up tight, so you pulled out your keys and let yourself in. The lights flickered on, colouring the white walls with a yellow hue. You kicked off your muddy work boots and hung up your coat. Upon entering the living room, you spot the relic sitting on your shelf: 'that's odd', you thought, certain that you never placed it there. You began feeling an uneasy chill run up your spine.\n",
    3,
)

# choose which room in the house
level_one_room_choice()

# story
print_and_pause("more story", 4)

# challenge 1
challenge_one() #riddle

# story
print_and_pause("more story", 4)

# level complete
level_complete(1)


### LEVEL 2 ############ FOREST ###################

# story
print_and_pause("START LEVEL 2 story", 4)

# challenge 2
challenge_two()  # riddle

# story
print_and_pause("more story", 4)

# choose forest path
level_two_path_choice()

# story
print_and_pause("more story", 4)

# challenge 4 maybe a find relic
challenge_four()  # riddle ???

# story
print_and_pause("more story", 4)

# end level 2
level_complete(2)


### LEVEL 3 ############ SCHOOL ###################

# story
print_and_pause("start Level 3 story", 4)

# challenge
challenge_five()  # maths lose life if wrong

# story
print_and_pause("more story", 4)

# choose drawer in schoolroom
level_three_drawer_choice() # three chogain relics or die

# story
print_and_pause("more story", 4)

# challenge 6
challenge_five()  # maths

# story
print_and_pause("more story", 4)

# end level 2
level_complete(3)

# ----BOSS BATTLE----
