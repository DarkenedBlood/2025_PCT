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


# Main routine starts here
yes_no_list = ['yes', 'no']

want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

