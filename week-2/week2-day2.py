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

