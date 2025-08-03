import pandas as pd
from datetime import date

# Functions go here
# Statement Generator (essentially a heading)
def make_statement(statement, decoration, lines=1):
    """Creates headings (3 lines) subheadings (2 lines) and emphasized text (1 line)"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

    return make_statement


# Checks For Yes and No.
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


# Display Instructions to the User
def instructions():
    make_statement("Instructions", "ℹ️", 1)

    print("""

Welcome to this Price Comparison Tool
Think about the following inputs you will need.

- The Item's Name 
- The Cost for The Item
- The Weight of The Item (g)
- And your current budget

The program will record the inputs and calculate the 
Weight in kg and the unit price per KG.

Once you have entered the exit code ('xxx'), 
the program will display a recommendation
and write the all of the data to a text file.

    """)


# Makes sure the user's answer is not blank.
def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. \n")


# Checks the user enters a VALID number.
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


# Main inputs
def get_inputs(input_type, how_many, item_limit=0):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_item_names = []
    all_weights = []
    all_kg_weights = []
    all_price_per_kg = []
    all_rounded_price_kg = []
    all_costs = []

    price_comparison_dict = {
        'Name': all_item_names,
        'Weight': all_weights,
        'Weight (KG)': all_kg_weights,
        'Price': all_costs,
        'Price per KG': all_price_per_kg,
        'Price per KG (2 dp)': all_rounded_price_kg,
    }

    # Item amount (dunno why it's here, but it makes things work)
    amount = item_amount

    # User's Budget
    print()
    budget = num_check("Budget: $", float)
    print()

    # loop to get expenses
    while item_limit < item_amount :

        # get item name and check it's not blank
        item_name = not_blank("Item Name: ")
        print()

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

        if amount == "":
            amount = how_many

        # User inputs weight, Calculates to KG
        weight = num_check(f"What is the weight of the item (g)? ", "float", "")
        print()
        kg_weight = weight / 1000

        # User inputs cost of item, Calculates the price per KG + Rounding
        cost = num_check("Price for the item? $", "float")
        print()
        price_kg = (cost / kg_weight)
        rounded_price_kg = f"{price_kg:.2f}"

        item_limit += 1

        all_item_names.append(item_name)
        all_weights.append(weight)
        all_costs.append(cost)
        all_kg_weights.append(kg_weight)
        all_price_per_kg.append(price_kg)
        all_rounded_price_kg.append(rounded_price_kg)

    # create dataframe / table from dictionary
    price_comparison_frame = pd.DataFrame(price_comparison_dict)

    # Recommendations
    recommendation_sorter = price_comparison_frame.sort_values(by='Price per KG (2 dp)')

    # print (price_comparison_frame)
    print("Budget: $",budget)
    print()
    print(price_comparison_frame.to_string(index=False))
    print()
    print("Recommendation: This is my recommendation list, from most recommended to the lowest:")
    print()
    print(recommendation_sorter)

    # Headings / Strings...
    main_heading_string = f"=== Price Comparison Tool (budget: ${budget} ===)"
    items_heading_string = "- Items, Weights and Costs -"
    item_name_string = f"Names of Items: {all_item_names}"
    weights_string = f"The weights of Items: {all_weights}"
    cost_string = f"The costs of Items: {all_costs}"
    calculation_heading_string = f"- Calculations -"
    weights_kg_string = f"Weight (KG): {all_kg_weights}"
    cost_kg_string = f"Price per KG: {all_price_per_kg}"
    rounded_string = f"(rounded): {all_rounded_price_kg}"

    # list of strings to be outputted / written to file
    to_write = [main_heading_string,
                "\n", items_heading_string, item_name_string,
                weights_string, cost_string,
                "\n", calculation_heading_string, weights_kg_string,
                cost_kg_string, "\n",
                rounded_string]

    # create file to hold data
    file_name = f"Price Comparison {all_item_names} {day}_{month}_{year}"
    write_to = "{}.txt".format(file_name)

    text_file = open(write_to, "w+")

    # write the item to file
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

    return get_inputs


# Main Routine goes here

# **** Get current date for heading and filename ****
today = date.today()

# get day, month & year in separate strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

make_statement("Price Comparison Tool!", "*", 3)
want_instructions = string_check("Would you like to see the instructions? ")

if want_instructions == "yes":
    instructions()
else:
    print()

item_amount = num_check("How many items? ", "integer")
user_inputs = get_inputs("variable", item_amount)
