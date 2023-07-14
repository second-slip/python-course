#############################################################################################
# Week One
# Functions challenges
#############################################################################################


# Activity(1):
# Here's an example of a function that includes a parameter.
# Parameters are responsible for functions being able to work on different data
# inputs. Edit the snippet below to include two or more parameters and a running
# order count updated when the function is called :

order_count = 1

def take_order(topping, size):
    global order_count
    print(f"Order No. {order_count}: {size} pizza with {topping}")
    order_count += 1

take_order("pineapple", "12 inch")
take_order("Pepperoni", "9 inch")


# Activity(2):
print("Activity 2:")
# Cash machine time. Let’s create one that :
# Takes an input of pin number and amount
# Prints dispensing cash if the pin number is correct and
# there’s enough money to withdraw
# Displays the new bank balance
# Be creative!

account_balance = 1000
print(f"initial account balance is: £{account_balance}");

def withdraw_from_account(amount, account, pin):
    global account_balance;

    if (is_pin_valid(pin) == False):
        return print("The PIN is incorrect.  Try again")

    if (is_funds_available(amount)) == False:
        return print("You don't have sufficient funds available to withdraw the requested amount.");

    print(f"depensing £{amount} from your account number: {account}.");

    update_balance(amount);

    print(f"Your new account balance is: £{account_balance}")

def is_pin_valid(pin):
    if (len(str(pin)) == 4):
        return True
    else:
        return False

def is_funds_available(amount):
    funds_available = get_customer_balance()

    if amount <= funds_available:
        return True
    else:
        return False

def get_customer_balance():
    #global account_balance;
    return account_balance;

def update_balance(amount):
    global account_balance;
    account_balance = account_balance - amount;

# ok
withdraw_from_account(100, 12345678, 1234);
# not enough funds
withdraw_from_account(2000, 12345678, 1234);
# incorrect PIN
withdraw_from_account(345, 12345678, 134);
    
