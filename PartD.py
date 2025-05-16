def is_lower_upper():
    user_input = input("Enter a character/s: ")
    if user_input != str:
        raise Exception("Incorrect data type. Enter a string.")
    if user_input.islower():
        print(f"Your input of {user_input} is lower case.")
    else:
        print(f"Your input of {user_input} is upper case.")

is_lower_upper()
