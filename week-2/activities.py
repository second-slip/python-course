# In class activities


# Activity 1

# create a variable called password
password = 'hellothere';
# Check how many letters are in the password, 
letters_in_string = len(password);

print(letters_in_string);

if (letters_in_string < 8):
    # if there are less than 8 print that the password is too short. 
    print("the password is too short");
else:
    # Otherwise print the password.
    print(f"the password is: {password}");


# Activity 2

#Create a variable called num.
number = 5;

#Check if the variable is divisible by 3 or 5. 
if (number %3 == 0) or (number %5 == 0): #if (number %3 == 0 or number %5 == 0):
    #If it is print “This number is divisible by 3 or 5” to the console. 
    print("this number is divisable by 3 or 5");
else:
    # Otherwise log “This number is not divisible by 3 or 5”.
    print("This number is not divisible by 3 or 5");

# Activity 3
# Create a variable called num.
num = 5;
# If num is divisible by 3 print “fizz”, 
if (num %3 == 0):
    print("fizz");
# if it’s divisible by 7 print “buzz”, i
elif (num %7 == 0):
    print("buzz");
# if it’s divisible by both 3 and 7 print “fizz buzz”. print num.
elif (num %3 ==0) and (num%7 == 0): # num needs to equal 21
    print("fizz buzz");
else:
    print(num);

# Activity 4:
# Create a variable called word that takes a string.
word = "hello";
last_letter = word[len(word)-1];
fist_letter = word[0];
# Create an if statement that checks if the last letter is the same as the first. 
if (fist_letter == last_letter):
    # If it is return true,
    print(True); 
else:
    # otherwise return false.
    print(False);


# Activity 5:
# Create a variable called time, 
time = 7; # should I use DateTime
# a variable called place_of_work
place_of_work ="Manchester";
# and a variable called town_of_home.
town_of_home = "London";

# def where_am_I(time, place_of_work, Town_of_home) 
#     print("Withdrawing") 

    

# Create an if statement that prints where someone is at times of the day. 
if (time  == 7):
    # If it is return true,
    print("I'm at home"); 

if (time  == 8) and (place_of_work ==  "Manchester"):
    # If it is return true,
    print("I'm at home"); 


else:
    # otherwise return false.
    print(False);
# E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at work.