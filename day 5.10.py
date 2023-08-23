def reverseWords(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

input_string = input("Enter a string: ")
reversed_string = reverseWords(input_string)
print("Reversed words:", reversed_string)
