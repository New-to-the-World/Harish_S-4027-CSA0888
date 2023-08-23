def isPalindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

phrase = input("Enter a phrase: ")
if isPalindrome(phrase):
    print("The given phrase is a valid palindrome.")
else:
    print("The given phrase is not a valid palindrome.")
