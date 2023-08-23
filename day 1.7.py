def count_sorted_vowel_strings(n, vowel_index=0):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if n == 0:
        return 1
    count = 0
    for i in range(vowel_index, len(vowels)):
        count += count_sorted_vowel_strings(n - 1, i)   
    return count

n = int(input("Enter the value of n: "))
result = count_sorted_vowel_strings(n)
print(f"Number of sorted vowel strings of length {n}: {result}")
