import re


def prompt_user_for_input_until_valid():
    """
    Ask for user input until a valid name is supplied.
    returns: valid input as a str.
    """
    valid_input = False
    VALIDATOR = re.compile("\w+")

    while not valid_input:
        user_input = input("")
        if user_input.lower() == "q":
            print("Goodbye!")
            exit(0)
        else:
            valid_input = re.fullmatch(VALIDATOR, user_input).group()
            if valid_input is None:
                print("Please enter a valid name consisting of only letters and whitespace characters")
                continue
    return valid_input
    

def greet_user(name: str):
    """
    Prints out a formatted greeting to the user.
    :param name as a str
    """
    print(f"\nHello \u001b[34m{name}!\u001b[0m\n")

def print_menu_options():
    print("Please enter a valid name. or Q to quit.")

def main():
    print_menu_options()
    while True:
        name = prompt_user_for_input_until_valid()
        greet_user(name)


if __name__ == "__main__":
    main()