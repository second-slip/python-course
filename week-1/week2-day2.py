
print(len("hello"));

print("hello"[0]);

print("hello there".capitalize());

print("hello".upper());

print("hello".lower());

print("hello ".strip());

print("hello".find("e"));

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







# properties, lists, loops ...?

str = "All Around the World";

print(str[7].upper());

letters = [x for x in str]
print(letters);



# if ==
# elif ==
# else:

# == equal
# != not equal
# > greater than
# < less than
# =< less than or equal to
# => greater than or equal to

age = 20;
country = 'UK';

if (age > 17 and country == 'UK'):
    print("yes I can serve you");
else:
    print("you aren't old enough");




# age = int(input("enter your age:"));

# if (age <= 18):
#     print("price is £8");
# elif (age > 18) and (age < 60):
#     print("Adult 18+ price is £10.95");
# else:
#     print("senior price is £7.50");

def cash_withdraw(amount, account):
    print("Withdrawing {} from account {}".format(amount, account));

cash_withdraw(10, 7986008);

def print_order(size, type_of_drink):
    print(f"An order was placed for {size} {type_of_drink}");

print_order("grande", "flat white");


def add(num1, num2):
    return num1 + num2;

result = add(2,2);
print(result);

def substract(num1, num2):
    return num1 - num2;

result = substract(2,8);
print(result);

def multiply(num1, num2):
    return num1 * num2;

result = multiply(2,8);
print(result);

def divide(num1, num2):
    return num1 / num2;

result = multiply(2,8);
print(result);


def multiply_by_nine_fifths(celcius):
    return celcius * (9/5);

degreesC = multiply_by_nine_fifths(30);

print(degreesC);


# Example 5. Mini weather app , converting celsius to  fahrenheit:

def multiply_by_nine_fifths(celsius):
    return celsius * (9/5);

def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32;

print("The temperature is {}°F".format(get_fahrenheit(15)));


dict_list=["a" "chilli"],["b", "biio"];
print(dict_list[1],[1])

