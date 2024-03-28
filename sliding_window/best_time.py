def maxProfit(prices): 
    
    new_list = sorted(prices)
    if prices[0] == new_list[-1]:
        return 0
    
    left = 0
    right = 


prices = [7,1,5,3,6,4]

print(maxProfit(prices))