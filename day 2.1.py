def climb_stairs(n):
    if n <= 2:
        return n    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] 
    return dp[n]

n = int(input("Enter the number of steps: "))
ways = climb_stairs(n)
print("Distinct ways to climb to the top:", ways)
