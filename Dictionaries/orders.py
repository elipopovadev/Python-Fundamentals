lines = input().split()
stocks = {}

while(lines != ['buy']):
    product = lines[0]
    price = float(lines[1])
    quantity = float(lines[2])
    if product not in stocks:
        stocks[product] = [price, quantity]
    elif product in stocks and stocks[product][0] != price:
        updated_price = price
        updated_quantity = stocks[product][1] + quantity
        stocks[product] = [updated_price, updated_quantity]
    else:
        stocks[product][1] += quantity
     
    lines = input().split()

for key, value in stocks.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
    

        
    