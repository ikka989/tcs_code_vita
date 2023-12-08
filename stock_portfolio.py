def compute_profit_loss(stocks, prices, time):
    perceived_profit_loss=0
    veiled_profit_loss=0
    for i in range(len(stocks)):
        quantity, purchase_time,sell_time=stocks[i]
        if sell_time !=0 and purchase_time <= time <=sell_time:
           perceved_profit_loss+= quantity * (prices[i][sell_time-1] - prices[i][purchase_time-1])
        else:
            veiled_profit_loss+= quantity * (prices[i][sell_time-1] - prices[i][purchase_time-1])
    return perceived_profit_loss,veiled_profit_loss

num_stocks= int(input())
stocks_info =[]
for _ in range(num_stocks):
    stock = list(map(int, input().split()))
    stocks_info.append(stock)
    
    num_days = int(input())
    stock_prices =[]
    for _ in range(num_stocks):
        prices = list(map(int, input().split()))
        stock_prices.append(prices)
        
        
    time_instance = int(input())
    perceived_p1, veiled_p1= compute_profit_loss(stocks_info, stock_prices, time_instance)
    
    print(perceived_p1)
    print(veiled_p1)
            