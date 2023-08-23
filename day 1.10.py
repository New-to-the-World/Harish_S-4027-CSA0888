def modify_string(S):
    frequency = [0] * 26   
    for char in S:
        frequency[ord(char) - ord('a')] += 1   
    modified_string = ""
    for char in S:
        circular_distance = frequency[ord(char) - ord('a')]
        new_char = chr(((ord(char) - ord('a') + circular_distance) % 26) + ord('a'))
        modified_string += new_char    
    return modified_string

input_string = input("Enter a string consisting of lowercase alphabets: ")
result = modify_string(input_string)
print("Modified String:", result)
