def lengthOfLastWord(s):
    s = s.rstrip()  
    if not s:
        return 0
    last_space = s.rfind(' ')
    if last_space == -1:
        return len(s)
    else:
        return len(s) - last_space - 1

s = input("Enter a string: ")
result = lengthOfLastWord(s)
print("Length of the last word:", result)
