def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

def is_valid_password(password):
    parts = password.split(':')

    if len(parts) == 3:
        a, b, c = map(int, parts)
        if is_palindrome(a) and is_prime(b) and c % 2 == 0:
            return True

    return False


print(is_valid_password(input()))
