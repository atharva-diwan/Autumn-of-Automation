no_of_days=int(input())
stock_prices=list(map(int, input().split()))        #stock prices input
max_profit=stock_prices[1]-stock_prices[0]          #max profit initialization
buy_date=1                                          #buy date initialization
for i in range(no_of_days):
  for j in range(i,no_of_days):
    if stock_prices[j]-stock_prices[i]>max_profit:
      max_profit=stock_prices[j]-stock_prices[i]
      buy_date=i+1
print(max_profit)
print(buy_date)

