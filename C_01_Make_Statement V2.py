# Functions go here
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


# Main Routine goes here
make_statement("Price Comparison Tool", "=", 3)
make_statement("Instructions", "-", 1)
