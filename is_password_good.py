# The password is considered strong if:

# Its length is at least 8 characters.  abcD13qwerY
# It contains at least one uppercase letter.
# It contains at least one lowercase letter.
# It contains at least one digit.
def is_password_valid(password):
    if (len(password) < 8):
        return False
    if not any (char.isupper() for char in password):
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any (char.islower() for char in password):
        return False
    return True

password = input("Enter a password: ")
print(is_password_valid(password))
