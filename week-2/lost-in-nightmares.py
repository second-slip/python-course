from time import sleep as slp
import random

##############################################
# standard messages
WRONG_ANSWER = "\nOh, no: You got it wrong!  You lose 1 life..."
RIGHT_ANSWER = "\nYay!  You got it right.  You keep all your lives..."
INALID_RESPONSE_INT = "\nYour response is not valid.  Type an integer"
INALID_RESPONSE_YES_NO = (
    "\nYour repose is invalid.  You must type either 'yes' or 'no'..."
)

#region Miscellaneous functions

def capture_int_response():
    response = input("Hint: type your answer as an integer (e.g: 1 or 2 or 3) here: ")
    return int(response) if response.isdigit() else None

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

def game_achievement_score():
    if players_relics > 4:
        print_and_pause(f"\nYou found {players_relics} relics")
        print_and_stop("\nYou completed the game a high score!  Very well done")

    else:
        print_and_pause(f"\nYou found {players_relics} relics")
        print_and_stop(
            "You completed the game, but with a low score.  Try to improve your score next time."
        )



#endregion


# region health system

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


# function to update lives count to 0
def lose_all_lives():
    global players_lives
    players_lives = 0
    return


def check_if_game_over():
    if players_lives == 0:
        game_over()
    else:
        print_and_stop(
            f"\nYou have {players_lives} lives and {players_relics} relic(s).\n"
        )


def game_over():
    print("\nYou have no lives left.")
    print_and_stop("\nGAME OVER!!!!!!!!!!\n")
    quit()


# endregion


# region Relic system

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


# endregion


# region level decision points
#### LEVEL 1 ROOM CHOICE
def level_one_room_choice():
    print_and_pause("Where will you go now?.  You can choose ONE room...", 1)
    print_and_pause("1 for the Kithchen", 1)
    print_and_pause("2 for the Bedroom", 1)
    print_and_pause("3 for the Bathroom", 1)

    room = capture_int_response()

    match room:
        case 1:  # Kitchen
            print_and_pause(
                "\nYou entered the kitchen to look for something to eat. After all, you hadn't eaten all day, so a nice meal would be very useful to soothe your growling stomach. You opened the fridge only to hear your gas hobs spark to life behind you along with the cupboards creaking open. 'That's some storm..' you muttered before turning off the hobs and closing the cupboards.",
                5,
            )
            print_and_pause(
                "\nA click of the backdoor is heard as it unlocked without you even touching it, the handle was pulled down and the door swung wide open. On the other side was a lanky demon-like figure with inky black flesh and piercing white eyes. It began to crawl through the door with its freakishly long and blood-stained appendages - you screamed and ran out of the kitchen, slamming the door behind you. You knew staying inside of the house would get you killed, so without hesitation, you sprinted out of the front door into the storm.",
                4,
            )
            # no gains

        case 2:  # Bedroom
            print_and_pause(
                "\nYou decided to head upstairs to your room for some much needed rest. After such a tiring day, you thought maybe your mind was playing tricks on your again, but as you entered your room, you noticed something on your pillow. It looked like another relic! Understandably, you began to freak out a little, why were these things following you? How were they following you? You picked up the relic and examined it. This relic was different to the one you found earlier, it felt softer, its hum was delicate and gentle. You decided to stuff it into your pocket.",
                5,
            )
            print_and_pause(
                "\nUpon turning around to close your window, a demon-like figure was standing outside the glass. You screamed and backed up away from the window, grabbing the door handle to escape, absolutely terrified of the creature before you. It looked like a shadow - it was lanky and as black as the abyss, its white eyes and sharpened bloody teeth piercing through the darkness. It was crawling through the open window to get to you. You panicked and sprinted out of the bedroom, slamming the door behind you. You needed to run!",
                5,
            )
            print_and_pause("\nYou gained a relic")
            add_relic(1)

        case 3:  # Bathroom
            print_and_pause(
                "You decided to quickly check the bathroom for anything interesting. Honestly, there wasn't much, but you did find some medication in the cabinate behind your mirror.",
                5,
            )
            print_and_pause(
                "You stuffed it into your pocket and and closed the cabinate door. As it closed, you glanced into the mirror, only to see a dark demonic creature stretching its bloodied claws towards you. You grab your shower pole out of panic and smashed it over the demons head, stunning it long enough to process what was happening and run out of the house.",
                5,
            )
            print_and_pause("\nYou gained a life")
            add_lives(1)

        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            level_one_room_choice()

    check_if_game_over()


#### LEVEL 2 PATH CHOICE
def level_two_path_choice():
    print_and_pause("Your only options were to go Dead Ahead, Left or Right", 1)
    print_and_pause("1 for Dead Ahead", 1)
    print_and_pause("2 for Left", 1)
    print_and_pause("3 for Right", 1)

    path = capture_int_response()

    match path:
        case 1:  # Dead ahead
            print_and_pause(
                "\nYou scuttled down the middle path, refusing to go any other direction. You thought it best to carry on in the direction you were already on.",
                5,
            )
            print_and_pause(
                "\nSurprisingly, the path was relatively easy to navigate with the torch, you felt like you were making a decent bit of distance from the demon. Along your journey, two relics were sat huddled together inside of a fallen birds nest, they looked two little owlets. You gently picked up the two relics and stuff them into your pocket and swiftly moved along. After a short while of paranoia-fuelled walking, you reached a main road that was illuminated with lamplight. You were alive, and somewhat safe.",
                5,
            )

        case 2:  # LEFT PATH
            print_and_pause(
                "\nYou decided to take the left path. The terrain was long and treacherous, it seemed to go on forever. On your journey, you find a singular relic encased in brambles that looked exactly like the one you previously stuffed into your pocket. You decided to stuff the relic into your pocket, too. Oh! What's this? You found a red vial with a mysterious fluid inside. You kept it to see what it would taste like.",
                5,
            )
            print_and_pause(
                "\nEventually, your light flickered out on your journey to safety, forcing you to stop and relight the flame. The flint refused spark to life, and the rustling started to get closer and closer, the demons raspy breathing sounded like it was just a heartbeat away. You panicked and dropped your torch, running until you reached the edge of the forest and straight into lamplight on a eerily silent road. You were alive. For now.",
                5,
            )
            print_and_pause("\nYou gained a relic")
            add_relic(1)  # +1 relic


        case 3:  # RIGHT PATH
            print_and_pause(
                "\nYou decided to scurry down the right path. It didn't take long for you to reach what seemed to be a graveyard covered in a thick layer of fog. You entered the graveyard, ever so cautious of what you'd find.",
                5,
            )
            print_and_pause(
                "\nYou explored around the yard of death until you found a peculiar open grave, the loose soil was still piled up next to it. As you wearily approached the grave, you saw that 'Harvey Staker' was engraved into the headstone. You began to panic, dropping your torch onto the ground out of shock and fear, causing the flame to go out. You turned to run, but it was too late - It was here... The demon had snuck up on you and dragged you down to the grave before you could scream. This was the end of Harvey Staker, may his soul rest in pieces.",
                5,
            )
            lose_all_lives()
            check_if_game_over()

        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            level_two_path_choice()

    check_if_game_over()


#### LEVEL 3 SCHOOL BOOK CHOICE
def level_three_book_choice():
    print_and_pause("Which book do you choose?.  You can choose ONE book...", 1)
    print_and_pause("1 for the Blue Book", 1)
    print_and_pause("2 for the Red Book", 1)
    print_and_pause("3 for the Green Book", 1)

    book = capture_int_response()

    match book:
        case 1:  # Blue book
            blue_book_maths_challenge()
            add_relic(2)  # +2 relic

        case 2:  # Red book
            red_book_history_challenge()
            add_relic(1)  # +1 relics

        case 3:  # Light 2
            green_book_biology_challenge()
            add_relic(1)  # +1 relics

        case _:
            print_and_pause(INALID_RESPONSE_INT, 1)
            level_three_book_choice()


# endregion


# region prining functions

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


# pauses execution for x seconds
def pause(seconds):
    slp(seconds)


# endregion


#region Level 1 challenges

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

#endregion


#region Level 3 challenges

################################
def blue_book_maths_challenge():
    #
    num1 = random.randint(6, 12)
    num2 = random.randint(6, 12)
    correct_answer = num1 * num2

    print_and_pause("\nYou opened the blue book, your homework was a math problem:", 1)

    print_and_pause(f"\n'What is {num1} * {num2}?'", 1)

    attempts = 0

    while attempts < 2:
        answer = capture_int_response()
        # if answer is None:
        #     print("Your response must be an integer number!\n")
        #     blue_book_maths_challenge()

        if answer == correct_answer:
            print_and_pause(
                "\nTeacher: 'Very good. Here is your reward.'",
                1,
            )
            print_and_pause(
                "The teacher handed you a blue key to unlock the drawer the book was sitting on top of. You opened it to find another relic and an old spare classroom key! You stuffed the relic into your pocket and used the key on the door, allowing you to escape to the lobby.",
                5,
            )
            break

        else:
            if attempts == 0:
                print_and_pause(
                    "\nTeacher: 'WRONG. Try it again, PROPERLY this time, use the correct method to solve this equation.'",
                    1,
                )
                subtract_lives(1)
                check_if_game_over()
            if attempts == 1:
                print_and_pause(
                    "\nTeacher: 'FAILURE! You're inadequate for my class, you must be punished for your stupidity!"
                    "\nThe teacher used her ruler to hack off your hands, causing you to bleed to death. This was the end of Harvey Staker.",
                    1,
                )
                lose_all_lives()
                check_if_game_over()

        attempts += 1


#############################################
def red_book_history_challenge():
    print_and_pause("\nYou opened the red book, your homework is a history problem:", 1)

    print_and_pause(f"\n'Who was the German leader in the Second World War?'", 1)

    correctAnswers = ["hitler", "adolf hitler", "adolf"]
    attempts = 0

    while attempts < 2:
        answer = input("type your answer: ")
        answer.lower()

        if answer in correctAnswers:
            print_and_pause(
                "\nTeacher: 'Well done, small one. You have completed your history homework.'",
                5,
            )
            break
        else:
            if attempts == 0:
                print_and_pause(
                    "\nTeacher: 'WRONG. Try it again, I can tell you don't know your history. RESEARCH MORE.",
                    5,
                )
                subtract_lives(1)
                check_if_game_over()
            if attempts == 1:
                print_and_pause(
                    "\nTeacher: 'FAILURE! You're inadequate for my class, you must be punished for your stupidity!'\nThe teacher used her ruler to stab you in the eyes, causing you to bleed to death. This was the end of Harvey Staker.",
                    5,
                )
                lose_all_lives()
                check_if_game_over()

        attempts += 1


###################################
def green_book_biology_challenge():
    print_and_pause(
        "\nYou opened the green book, your homework is a biology problem:", 1
    )

    print_and_pause(f"\nWhat is the powerhouse of a cell?", 1)

    correctAnswers = [
        "mitochondria",
        "nitochondria",
        "jitochondria",
        "mutochondria",
        "mjtochondria",
        "mktochondria",
    ]

    attempts = 0

    while attempts < 2:
        answer = input("type your answer: ")
        answer.lower()

        if answer in correctAnswers:
            print_and_pause(
                "\nTeacher: 'Well done, my pupil. You have completed your history homework.'",
                5,
            )
            break
        else:
            if attempts == 0:
                print_and_pause(
                    "\nTeacher: 'WRONG. Try it again, I can tell you don't know your history. RESEARCH MORE.",
                    5,
                )
                subtract_lives(1)
                check_if_game_over()
            if attempts == 1:
                print_and_pause(
                    "\nTeacher: 'FAILURE! You're inadequate for my class, you must be punished for your stupidity!'\nThe teacher used her ruler to stab you in the eyes, causing you to bleed to death. This was the end of Harvey Staker.",
                    5,
                )
                lose_all_lives()
                check_if_game_over()

        attempts += 1

#endregion


#region Level 2 challenges

# Challenge 1 (riddle)
def riddle_challenge_one():
    print_and_pause("Here is a riddle to solve:", 1)
    print_and_pause(
        "\nTroll: 'Tidings to you, mortal one. In order to pass, partake in my class : What belongs to only you, but those around you use it, too?'",
        1,
    )

    correctAnswers = ["your name", "name", "my name"]
    attempts = 0

    while attempts < 2:
        answer = input("type your answer: ")
        answer.lower()

        if answer in correctAnswers:
            print_and_pause(
                "\nTroll: 'Well done, small one. You have passed the test. You may proceed, but be careful, you may not succeed.'",
                5,
            )
            break
        else:
            if attempts == 0:
                print_and_pause(
                    "\nSorry, little one. That is incorrect. One more chance or you'll never advance.",
                    5,
                )
                subtract_lives(1)
                check_if_game_over()
            if attempts == 1:
                print_and_pause(
                    "\nMy, my, little one... You have failed the test, you can no longer progress. \nThe shadow demon caught up to you, killing you where you stand from behind. This was the end for Harvey Staker.",
                    5,
                )
                lose_all_lives()
                check_if_game_over()

        attempts += 1


# Challenge 2 (riddle)
def riddle_challenge_two():
    print_and_pause("Here is a riddle to solve:", 1)
    print_and_pause(
        "\nGirl: 'Hey, Mister! Play a game with me! I tell you a widdle, and you figure out the answer, okay? Here we go! What room do ghosts hate going in?'",
        1,
    )

    correctAnswers = ["living room", "the living room"]
    attempts = 0

    while attempts < 2:
        x = input("type answer: ")
        x.lower()

        if x in correctAnswers:
            print_and_pause(
                "\nGirl: 'That's wight! Living wooms make us feel sad... Do you want to play again? No? Aw... Okay. Well, bye-bye, Mister! We can play again when you die! Don't take too long!'",
                5,
            )
            break
        else:
            if attempts == 0:
                print_and_pause(
                    "\nGirl: 'Nope! That's not wight, silly goose! I'll let you have one more try, otherwise you'll play with me forever! Hehe!'",
                    5,
                )
                subtract_lives(1)
                check_if_game_over()
            if attempts == 1:
                print_and_pause(
                    "\nGirl: 'Oh no... You got it wrong again. That means Daddy will make you play with me! Here he is!\nYou turned around to see the shadow demon looming over your now doomed person. It snapped your neck, killing you instantly. Looks like you're the girl's playmate for the rest of eternity.",
                    5,
                )
                lose_all_lives()
                check_if_game_over()

        attempts += 1

#endregion


# region Level one game play
### LEVEL 1 ############ HOUSE ###################
def level_one():
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
    print_and_pause(
        "\nWhatever that demon was, you had no interest in finding out and scampered out of the house without a second thought. You kept up the pace and made your way into the woodlands. It felt like you were running for hours and hours, but now you were lost in the darkness of the forest with no light except for what trickled in from the gaps of the trees.",
        4,
    )

    # level complete
    level_complete(1)


# endregion


# region Level two game play
### LEVEL 2 ############ FOREST ###################
def level_two():

    # story
    print_and_pause(
        "\nYou ran for as far and as fast as you could, eventually coming to a halt in the centre of the forest. You looked around, the darkness hindered your ability to see. A tall stature loomed in front of you, or at least that's what you thought it was. You noticed there was a torch at the base of the statue. You take it. As you sparked the flame, your surroundings were illuminated, revealing that the statute was never a structure made of stone, it was a living troll!",
        4,
    )

    # story
    print_and_pause(
        "\nThe troll creaked and growled, its mighty voice bellowed through the forest.",
        4,
    )

    # challenge 1, a riddle
    riddle_challenge_one()

    # story
    print_and_pause(
        "\nThe troll stepped aside and returned to stone, allowing you easy passage through the forest with your new torch.",
        4,
    )

    # story
    print_and_pause(
        "\nAs you trekked through the murky woodland, the trees and foliage began to rustle - twigs and branches loudly snapped all around you. The demon was still following you. You picked up the pace, running to a set of three paths further ahead. Your only options were to go Dead Ahead, Left or Right. You've never been in these neck of the woods before, so you had no idea where these paths would lead. Which do you choose? The clock is ticking...",
        4,
    )

    # choose path in forest
    level_two_path_choice()

    # story
    print_and_pause(
        "\nThere was a school up ahead, you thought that maybe someone was still inside judging from the cars in the parking lot, but something was blocking you from reaching the gates; you pushed forward, only to be met with the soul of a dead child. Her eyes were hollow with some sort of black fluid pouring from them. You were, understandably, horrified. The little girl spoke with a soft and playful tone.",
        4,
    )

    # challenge 2, a riddle
    riddle_challenge_two()

    # story
    print_and_pause(
        "\nYou watched the little ghost girl fade away, you blinked a couple times before making your way to the school doors.",
        4,
    )

    # end level 2
    level_complete(2)


# endregion


# region Level three game play
### LEVEL 3 ############ SCHOOL ###################
def level_three():

    # story
    print_and_pause(
        "As you made your hasty ascent up the school steps, you peer into the windows of the school - there was nothing but thick gloom that consumed each room, not a single trace of human life. You thought it was odd to have cars parked outside if no-one was here, this was the only building around, too. You tried the front doors, and as you expected, they were locked up tight. You decided to look for another way in",
        4,
    )

    # story
    print_and_pause("Where will you go?", 3)

    # story (broken window)
    print_and_pause(
        "\nYou noticed a window that had been smashed open was surrounded by overgrown bushes and foliage, it lead straight into a classroom at the side of the school. You decided to stumble through the broken window, taking a small risk to your body as your tear your clothes and flesh on the broken glass which was still sticking out of the frame. Your body flopped onto the ground after a short fall, but you quickly get up and recover.\n",
        5,
    )

    # story
    print_and_pause(
        "\nYou allowed your eyes to adjust to the darkness, taking in your surroundings to make sure you didn't just waltz into a death trap - and would you look at that; you did. The classroom was heavily damaged. The walls were peeling and oozing with some sort of black fluid, just like the little ghost girl you encountered. You go to the classroom door to leave, but it was locked! As you turned back around, the ghost of a school teacher with a gasmask with hollowed eyes appeared behind you, causing you to scream.\n",
        5,
    )

    # choose book in schoolroom
    level_three_book_choice()

    # story
    print_and_pause(
        "\nJust before you left the classroom, you noticed a hefty looking book sitting on the teachers desk, you picked it up and flicked through the ancient pages. It was the solution to killing the shadow demon! The relics you've come across assist in destroying the beast, you just hoped you had enough. You exited the classroom and entered the lobby.\n",
        4,
    )

    # story
    print_and_pause(
        "\nYou decided to try entering through the cellar doors at the back of the school, breaking in the fragile rusty lock and swinging open the heavy iron doors. You made your descent to the depths of the school. It was pitch black inside, but the path up to the lobby was relatively straight forward. Before leaving through the main door, you spot a suspicious looking book. You flicked through it, realising this book had the answer to killing the shadow demon! You stuff the large, hard cover book into your pocket. You also found a box of bandages.\n",
        4,
    )

    print_and_pause(
        "\nYou finally made your way into the school's lobby with your pockets full of objects you've found on the way, you felt the presence of impending doom as you stood in the large, ruined room. This school was the complete opposite of what you originally thought, it was falling apart, and at any moment it felt as if it was going to come toppling down, and not a slither of human life. The shadow demon burst through the glass double doors of the lobby, you had a second to see what you could do against this monster.\n",
        4,
    )

    # end level 2
    level_complete(3)


# endregion


########################################################
# MAIN

print_and_stop("\nWelcome to LOST IN NIGHTMARES\n")

choose_difficulty_level()

level_one()

level_two()

level_three()

game_achievement_score()
