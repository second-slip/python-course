# Activity(1):
# Create a list of 4 favourite films
# Use a for loop to show each film in the list
# Create a function called film_check() that checks if the
# 3rd film in the list is Ghostbusters.
# If it is, it should print “yey it’s ghostbusters”. If it isn’t, it
# should print “booo, we want ghostbusters”

films = ["Pokemon", "Jurassic Park", "Ghostbusters", "Super Mario"]

def film_check(films):
    i = 0
    for film in films:
        if (film == "Ghostbusters") and (i == 2):
            print("yey it's ghostbusters")
        else:
            print("booo, we want ghostbusters")
        i += 1

film_check(films)