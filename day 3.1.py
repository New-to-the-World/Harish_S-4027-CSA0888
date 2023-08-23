def max_profit(prices):
    n = len(prices)    
    buy1 = [float('-inf')] * n
    sell1 = [0] * n
    buy2 = [float('-inf')] * n
    sell2 = [0] * n    
    for i in range(n):
        if i == 0:
            buy1[i] = -prices[i]
        else:
            buy1[i] = max(buy1[i-1], -prices[i])
            sell1[i] = max(sell1[i-1], buy1[i-1] + prices[i])
            buy2[i] = max(buy2[i-1], sell1[i-1] - prices[i])
            sell2[i] = max(sell2[i-1], buy2[i-1] + prices[i])   
    return sell2[n-1]

prices_str = input("Enter the stock prices throughout the day separated by spaces: ")
prices = [int(x) for x in prices_str.split()]
profit = max_profit(prices)
print("Maximum profit:", profit)
