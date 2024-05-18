prices = [1,2,4]


# if len(prices) == 2 and prices[0] < prices[1]:
#     return prices[1] - prices[0]
            

maxprofit = 0
for i in range(len(prices)):
    buy = prices[i]
    left = i + 1
    right = len(prices) -1

    while left < right:
        if buy > left:
            left += 1
            continue
        else:
            profit = prices[left] - prices[buy]
            if profit > maxprofit:
                maxprofit = profit
            else:
                left += 1


