def is_palindrome(s):
    return s == s[::-1]

text = input("Enter string: ")
print("Palindrome" if is_palindrome(text) else "Not Palindrome")