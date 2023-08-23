def delchar(s, c):
    if len(c) != 1:
        return s
    return s.replace(c, '')

s = input("Enter a string: ")
c = input("Enter a single character to delete: ")
result = delchar(s, c)
print("Modified string:", result)
