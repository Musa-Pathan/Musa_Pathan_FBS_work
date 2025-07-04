#5.WAP to calculate selling price of book based on cost price and discount. 
cost_price=float(input("enter the cost price of the book:"))
discount=float(input("enter the discount percentage:"))
discount_amount=(discount/100)*cost_price
selling_price=cost_price-discount_amount
print("selling price of the book is:",selling_price)