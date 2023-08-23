def longestSubstring(s, k):
    if len(s) == 0 or k > len(s):
        return 0
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for char, freq in char_freq.items():
        if freq < k:
            return max(longestSubstring(sub_s, k) for sub_s in s.split(char))
    return len(s)

s = input("Enter the string: ")
k = int(input("Enter the integer k: "))
result = longestSubstring(s, k)
print("Length of the longest substring:", result)
