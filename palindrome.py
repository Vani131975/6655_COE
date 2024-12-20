print("Palindrome Checker")

def is_palindrome(string):
    string = string.lower() 
    return string == string[::-1]

text = input("Enter any word or phrase: ")
if is_palindrome(text):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
