def max_profit(prices):

    # Best time to Buy and Sell Stock
    buy = 0
    sell =  1
    max_profit = 0
    n = len(prices)
    while sell < n:
        current_profit = prices[sell] - prices[buy]
        max_profit = max(current_profit , max_profit)
        if prices[buy] > prices[sell]:
            buy = sell
        sell += 1   
    return max_profit


print(max_profit([7,1,5,3,6,4]))
