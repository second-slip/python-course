#############################################################################################
# Week One
# What If challenges
#############################################################################################


# Challenge 1
print("Challenge 1:")

# Check how many letters are in the password, 
def how_many_letters(password):
    letters_in_string = len(password);

    if (letters_in_string < 8):
        print("the password is too short");  # if there are less than 8 print that the password is too short. 
    else:
        print(f"the password is: {password}"); # Otherwise print the password.


password = 'hellothere'; # create a variable called password
how_many_letters(password);
password = 'not8'; 
how_many_letters(password);




# Challenge 2
print("Challenge 2:");

#Check if the variable is divisible by 3 or 5. 
def divisible_by_3_or_5(number):
    if (number %3 == 0) or (number %5 == 0):
        #If it is print “This number is divisible by 3 or 5” to the console. 
        print("this number is divisable by 3 or 5");
    else:
        # Otherwise log “This number is not divisible by 3 or 5”.
        print("This number is not divisible by 3 or 5");

num = 3; #Create a variable called num.
divisible_by_3_or_5(num);
num = 5; 
divisible_by_3_or_5(num);
num = 2; 
divisible_by_3_or_5(num);


# Challenge 3
print("Challenge 3:");

def fizz_buzz_printer(num):
    if (num %3 ==0) and (num%7 == 0): # num needs to equal 21
        print("fizz buzz"); # if it’s divisible by both 3 and 7 print “fizz buzz”
    elif (num %3 == 0): # If num is divisible by 3 print “fizz”, 
        print("fizz");
    elif (num %7 == 0):  # if it’s divisible by 7 print “buzz”, i
        print("buzz");
    else:
        print(num); # otherwise print num

num = 3;
fizz_buzz_printer(num);
num = 7;
fizz_buzz_printer(num);
num = 21;
fizz_buzz_printer(num);
num = 1;
fizz_buzz_printer(num);



# Challenge 4:
print("Challenge 4:");

def last_letter_equals_first(word):
    last_letter = word[len(word)-1];
    fist_letter = word[0];
    # Create an if statement that checks if the last letter is the same as the first. 
    if (fist_letter == last_letter):
        print(True); # If it is return true
    else:
        print(False); # otherwise return false.

word = "hello"; # Create a variable called word that takes a string.
last_letter_equals_first(word);

word = "oxo"; # Create a variable called word that takes a string.
last_letter_equals_first(word);



# Challenge 5:
print("Challenge 5:");

def where_am_I(time, place_of_work, town_of_home):
    # Create an if statement that prints where someone is at times of the day. 
    if (0 <= time < 8):
        print(f"I'm at home in {town_of_home}."); 
        return;
    if (time == 8):
        print(f"I'm commuting from {town_of_home} to my work in {place_of_work}"); 
        return;
    if (9 <= time < 17):
        print(f"I'm at work in {place_of_work}");
        return;
    if (time == 17):
        print(f"I'm commuting from {place_of_work} to home in {town_of_home}");
        return;
    if (18 <= time <= 23):
        print(f"I'm at home in {town_of_home}.");
        return;
    else:
        print("It was not possible to find out the person's location.");
        return;

place_of_work ="Manchester"; # a variable called place_of_work
town_of_home = "London"; # and a variable called town_of_home.

time = 7;
where_am_I(time, place_of_work, town_of_home);
time = 8;
where_am_I(time, place_of_work, town_of_home);
time = 10;
where_am_I(time, place_of_work, town_of_home);
time = 17;
where_am_I(time, place_of_work, town_of_home);
time = 19;
where_am_I(time, place_of_work, town_of_home);


# Challenge 6:
print("Challenge 6:");

# Create an if statement that checks if the result of the sum is even. 
# If it is, return a success message.
def is_even(number1, number2):
    number = number1 + number2;
    if (number % 2) == 0:
        print("the number is even");
    else:
        print("the number is false");

num1 = 4; # Create two variables called num1 and num2.
num2 = 7;
is_even(num1, num2);

num1 = 4;
num2 = 4;
is_even(num1, num2);



# Challenge 7:
print("Challenge 7:")

# Check if the number is a palindrome (looks the same
# forward as it does backwards e.g. 1001 or 20202).
def is_palindrome(number):
    forward = str(number);
    backward = forward[::-1];
    if (forward == backward):
        return True;
    else: 
        return False;

num = 1001; # Create a variable called num.
print(is_palindrome(num));
num = 20202;
print(is_palindrome(num));
num = 1234;
print(is_palindrome(num));


# Challenge 8:
print("Challenge 8:");
# Take the string “jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi”.
# Find the index of a last vowel in the string.

str = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi";
vowels = ["a", "e", "i", "o", "u"];

indexes = [i for i, letter in enumerate(str) if letter in vowels];

if (len(indexes) > 0):
    print(f"{len(indexes)} matches: {indexes}. \nThe last vowel is at index: {indexes[-1]}.");
else:
    print("no matches found");
