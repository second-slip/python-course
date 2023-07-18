# Relic system

players_relics = []  # property to track player's lives

# function to add x lives to players_lives
def add_relic(relic_type):
    global players_relics
    players_relics.append(relic_type);
    return

# function to subtract x lives to players_lives
def remove_relic(relic_type):
    global players_relics
    players_relics.remove(relic_type);
    return

def what_relics_do_I_have():
    print(f"you have the following relics: {players_relics}")

##############################################
def level_one_path_choice():
    print("Level 1 - Path Option")
    
    print("Choose which room you want...")
    print("A: Living room") 
    print("B: kitchen")
    print("C: bedroom")
    print("D: hallway")
    print("E: optional room")

    path = (input())

    match path:
        case "a":
            print("you gained a WHATEVER relic")
            add_relic("whatever")
        case "b": #if RIGHT ANSWER
            print("you gained 2 WHATEVER relics")
            add_relic("whatever")
            add_relic("whatever")
        case "c": #WRONG ANSWER (B)
            print("sorry, no relics here!")
            add_relic("whatever")
        case "d": #WRONG ANSWER (B)
            print("you gained a DIFFERENT relic")
            add_relic("different")
        case "e": #WRONG ANSWER (B)
            print("you gained a WHATEVER relic")
            add_relic("whatever")

    # tODO: pluralise sentence when necessary
    print(f"You have {len(players_relics)} relic(s).")
    print(players_relics)

level_one_path_choice()

