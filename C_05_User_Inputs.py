def num_check(question, num_type, exit_code=None):
    """Checks users enter an integer / float that is more than zero"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero"
        change_to = int

    else:
        error = "Oops - please enter a number more than zero"
        change_to = float

    while True:
        response = input(question).lower()

        # check for exit code
        if response == exit_code:
            return response

        try:
            # change response to be an integer and make sure it is higher than Zero.
            response = change_to(response)

            if response > 0:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    # Checks that users enter the full word or the first letter of a word from a list of valid responses.

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter.
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. \n")


def get_inputs(input_type, how_many):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_item_names = []
    all_weights = []
    all_costs = []

    # expenses dictionary
    # expenses_dict = {
        # "Item Names": all_item_names,
        # "Weight": all_weights,
        # "Cost": all_costs
    # }

    # default amount to 1 for fixed expenses and
    # to avoid PEP 8 error for variable expenses
    amount = 1

    # loop to get expenses
    while True:

        # get item name and check it's not blank
        item_name = not_blank("Item Name: ")

        # check users enter at least one variable expense
        # NOTE: If you type the conditions without brackets,
        # All on one line and then add in enters
        # Pycharm will add in the brackets automatically.
        if (input_type == "variable" and item_name == "xxx") and len(all_item_names) == 0:
            print("Oops! - you have not entered anything. "
                  "You need at least 1 item.")
            continue

        elif item_name == "xxx":
            break

        # Get item amount <enter> defaults to number of
        # products being made
        weight = num_check(f"What is the weight of the item (g)? ", "float", "")

        if amount == "":
            amount = how_many

        cost = num_check("Price for the item? $", "float")

        all_item_names.append(item_name)
        all_weights.append(weight)
        all_costs.append(cost)

    return get_inputs


# Main Routine goes here

budget = num_check("What is your budget? $", "float")
item_amount = num_check("How many items? ", "float")

user_inputs = get_inputs("variable", item_amount)
