def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping = {}
    used_characters = set()
    
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        else:
            if t[i] in used_characters:
                return False
            mapping[s[i]] = t[i]
            used_characters.add(t[i])
    
    return True

s=input()
t=input()
print(are_isomorphic(s,t))
