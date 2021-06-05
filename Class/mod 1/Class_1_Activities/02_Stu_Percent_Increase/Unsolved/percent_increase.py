# Percent Increase Activity

# Formulas
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# @TODO: Create float variable for original_price
original_price = 5.50

# @TODO: Create float variable for current_price
current_price = 14.50

# @TODO: Calculate difference between current_price and original_price
price_change = current_price - original_price

# @TODO: Calculate percent_increase
percent_increase = price_change/original_price * 100
#print (percent_increase)

# Print original_price
print(f"Apple's original stock price was ${original_price}")

# Print current_price
print(f"Apples current stock price is ${current_price}")
print(f"Apples stock percent increased {percent_increase:.2f}%")


# @TODO: Print percent_increase to 2 decimal places using f-string formatting
print(f"percent increase {percent_increase: .1f}%")
