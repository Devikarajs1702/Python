def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "$@#"

    if len(password) >= 6:
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True

        if has_upper and has_lower and has_digit and has_special:
            print("Password is valid")
        else:
            print("Invalid password")
    else:
        print("Invalid password")

user_input = input("Enter the password: ")
validate_password(user_input)
