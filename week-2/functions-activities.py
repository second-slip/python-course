# Activity(1):
# Here's an example of a function that includes a parameter.
# Parameters are responsible for functions being able to work on different data
# inputs. Edit the snippet below to include two or more parameters and a running
# order count updated when the function is called :

order_count = 1;
def take_order(topping, size):
    global order_count;
    print(f"Order No. {order_count}: {size} pizza with {topping}");
    order_count += 1;


take_order("pineapple", "12 inch");
take_order("pineapple", "12 inch");


# Activity(2):
# Cash machine time. Let’s create one that :
# Takes an input of pin number and amount
# Prints dispensing cash if the pin number is correct and
# there’s enough money to withdraw
# Displays the new bank balance
# Be creative!

