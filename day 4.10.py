def isScramble(s1, s2, memo={}):
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    if s1 == s2:
        memo[(s1, s2)] = True
        return True
    if sorted(s1) != sorted(s2):
        memo[(s1, s2)] = False
        return False
    n = len(s1)
    for i in range(1, n):
        if (isScramble(s1[:i], s2[:i], memo) and isScramble(s1[i:], s2[i:], memo)) or \
           (isScramble(s1[:i], s2[-i:], memo) and isScramble(s1[i:], s2[:-i], memo)):
            memo[(s1, s2)] = True
            return True
    memo[(s1, s2)] = False
    return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if isScramble(s1, s2):
    print("s2 is a scrambled string of s1.")
else:
    print("s2 is not a scrambled string of s1.")
