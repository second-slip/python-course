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


# Activity(1):
# Create a list of your
# favourite website (3 of them), and then
# add another two once you’ve created the list. Then remove
# the last website.

websites = ["Amazon", "Stack Overflow", "GitHub"]

more_websites = ["Pluralsight", "Python Docs"]

websites.extend(more_websites)

print(websites)

websites.pop()

print(websites)

# Activity(2):
# Research on the following methods: remove(), reverse(), sort(),
# count(), extend() (and many more). Create a program to
# demonstrate the uses of each method, some of these you may
# need more than one example. (Pay attention: not all methods
# would permanently updates/make changes to the lists
# themselves.)

# list
favourite_morrissey_songs = [
    "Suedehead",
    "The World Is Full of Crashing Bores",
    "The Youngest Was the Most Loved",
]

print(favourite_morrissey_songs)
# print an element by index
print(favourite_morrissey_songs[0])
# change one element by index
favourite_morrissey_songs[0] = "Spent the Day in Bed"
print(favourite_morrissey_songs)
# add an item with append
favourite_morrissey_songs.append("Istanbul")
print(favourite_morrissey_songs)

# pop default -1 / last element
favourite_morrissey_songs.pop()
print(favourite_morrissey_songs)

# pop access element by specific index
favourite_morrissey_songs.pop(1)
print(favourite_morrissey_songs)

# remove Removes the first item with the specified value
favourite_morrissey_songs.remove("The Youngest Was the Most Loved")
print(favourite_morrissey_songs)

# append method appends an element to the end of the list.
favourite_morrissey_songs.append("Istanbul")
favourite_morrissey_songs.append("Istanbul")
favourite_morrissey_songs.append("Istanbul")

# count() Returns the number of elements with the specified value
count = favourite_morrissey_songs.count("Istanbul")
print(count)

more_favourite_morrissey_songs = ["Forgive Someone", "Drag the River"]

# extend method adds the specified list elements (or any iterable) to the end of the current list.
favourite_morrissey_songs.extend(more_favourite_morrissey_songs)
print(favourite_morrissey_songs)

# insert dds an element at the specified position
favourite_morrissey_songs.insert(1, "That's How People Grow Up")
print(favourite_morrissey_songs)

# reverse()	Reverses the order of the list
favourite_morrissey_songs.reverse()
print(favourite_morrissey_songs)

# sort() method sorts the list ascending by default.
# can also make a function to decide the sorting criteria(s).
favourite_morrissey_songs.sort()
print(favourite_morrissey_songs)

# copy returns a copy of the list
copy = favourite_morrissey_songs.copy()
print(copy)

# index() returns the index of the first element with the specified value
index = favourite_morrissey_songs.index("Forgive Someone")
print(index)

# clear: removes all the elements
favourite_morrissey_songs.clear()
print(favourite_morrissey_songs)