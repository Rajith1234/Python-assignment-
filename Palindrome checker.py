def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the cleaned string is the same as its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
