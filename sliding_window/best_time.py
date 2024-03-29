def maxProfit(prices): 
    maxP = 0
    buy = 0
    sell = 1
    
    while sell < len(prices):
        if prices[buy] < prices[sell]: # so if buy is 7 and sell is 1, it wont go into the loop
            profit = prices[sell] - prices[buy]
            maxP = max(profit, maxP)
        else:
            buy = sell
        sell += 1
    return maxP
        
prices = [7,3,5,1,6]

print(maxProfit(prices))