import re
def is_valid_number(s):
    pattern = r'^\s*[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?\s*$'
    return bool(re.match(pattern, s))

input_str = input("Enter a string: ")
if is_valid_number(input_str):
    print("Valid number")
else:
    print("Not a valid number")
