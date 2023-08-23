def remove_common_words(string1, string2):
    words1 = string1.split()
    words2 = string2.split()   
    common_words = set(words1) & set(words2)   
    filtered_words1 = [word for word in words1 if word not in common_words]
    filtered_words2 = [word for word in words2 if word not in common_words]    
    new_string1 = " ".join(filtered_words1)
    new_string2 = " ".join(filtered_words2)
    return new_string1, new_string2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
new_string1, new_string2 = remove_common_words(string1, string2)
print("Modified first string:", new_string1)
print("Modified second string:", new_string2)
