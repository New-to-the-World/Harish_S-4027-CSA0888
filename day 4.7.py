def countSortedVowelStrings(n):
    dp = [[0] * 5 for _ in range(n + 1)]
    for j in range(5):
        dp[1][j] = 1
    for i in range(2, n + 1):
        for j in range(5):
            dp[i][j] = sum(dp[i - 1][k] for k in range(j, 5))
    return sum(dp[n])

n = int(input("Enter the length of the string: "))
result = countSortedVowelStrings(n)
print("Number of lexicographically sorted vowel strings:", result)
