def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    '''Checks that users enter the full word or the first letter of a word from a list of valid responses.'''

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
print(f"you chose {want_instructions}")
