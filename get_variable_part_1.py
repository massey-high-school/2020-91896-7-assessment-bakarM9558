# Item and Cost List


# Number Checking Function
def num_check(question):
    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        response = (input(question))

        if response.lower() == "xxx":
            return "xxx"

        else:
            try:
                if float(response) <=0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)

# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main Routine...

# Replace line below with component 3 in due course...
item_name = (input("What is item name? "))

# Set up empty item list
items = []

# Loop to ask users to enter an item
stop = ""
while stop != "xxx":

    amount = num_check("What is the budget? ")

    # Stop looping if exit code is typed and there are more
    # tan 2 items...
    if amount.lower() == "xxx" and len(items) > 1:
        break

    elif amount.lower() == "xxx" and len(items) <2:
        print("You need at least two items in the list.  "
              "Please add more items.")

    # If exit code is not entered, add item to list
    else:
        # Ask user for item (via not blank function)
        get_items = not_blank("Please enter the cost? ",
                                   "This can't be blank",
                                   "yes")
        amount = (amount) * num_check

        items.append("{} units {}".format(amount, get_items))

