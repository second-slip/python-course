#create a variable and assign string value
my_name = "Andrew";
# pass the variable to the print function to print the current value to the terminal
print(my_name);
# concatenate / join the current variable value and a string
print("hello " + my_name);
my_surname = "Cross";
# using F-Strings (a string formatting syntax) to concatenate string and string variables
print(f"my name is {my_name} {my_surname}");

# Activity 1
# Create a program that stores someone's name, age and favourite colour that
# prints these in a complete sentence

# create 3 variables for the name, age and colour
person_name = "Andrew";
person_age = 20;
person_colour = "yellow";

# Use the three variables to print a full sentance with the current variable values
print(f"My name is {person_name}.  I am {person_age} years old.  My favourite colour is {person_colour}.")


person_name = "Andrew";
person_age = 20;
person_colour = "yellow";
new_line_escape = '\n';

print(f"My name is {person_name}{new_line_escape}I am {person_age} years old.{new_line_escape}My favourite colour is {person_colour}.")


# Activity 2
# Create a program that stores someone's name, age and favourite colour that
day = "Today";
breakfast = "porridge";
lunch = "sandwich";
dinner = "burger";
print(f"{day} I ate {breakfast} for breakfast, {lunch} for lunch and {dinner} for dinner.");

day = "Tomorrow";
breakfast = "bacon";
lunch = "soup";
dinner = "pasta";
print(f"{day} I ate {breakfast} for breakfast, {lunch} for lunch and {dinner} for dinner.");

# Activity 3
# print(' ', ' ', '|');


def my_function(times, chars):
    for x in range(times):
        print(" " * chars + " | " + " " * chars + " | " + " " * chars);

def print_horizontal_line(x):
    print("- " * x);


# my_function(3, 3);
# print_horizontal_line(9);
# my_function(3, 3);
# print_horizontal_line(9);
# my_function(3, 3);


# Activity 4
space1 = "x";
space2 = "o";
space3 = " ";
space4 = "x";
space5 = "x";
space6 = " ";
space7 = "o";
space8 = " ";
space9 = " ";

# print(5 * '*' +  ' ' + 5 * '*');

space = " ";
vert = " | ";
dash = "- ";

def print_horizontal(spaces, dashes, verts):
    print(space * spaces + vert * verts + space * spaces + vert * verts + space * spaces)

def print_vertical(dashes):
    print(dash * dashes)

def print_horizontal2(spaces, dashes, verts):
    print(space * spaces + vert * verts + space * spaces + vert * verts + space * spaces)

print_horizontal(3,0,1);
print_horizontal(3,0,1);
print_horizontal(3,0,1);
print_vertical(9);
print_horizontal(3,0,1);
print_horizontal(3,0,1);
print_horizontal(3,0,1);
print_vertical(9);
print_horizontal(3,0,1);
print_horizontal(3,0,1);
print_horizontal(3,0,1);

def cell(one, two, three):
    print(f"{one} {two} {three}");


print(cell(space, space, space), vert, cell(space, space, space));





