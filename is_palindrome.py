def is_palindrome(text):
    text = "".join(a.lower() for a in text if a.isalpha())
    return text == text[::-1]

print(is_palindrome(input()))
