# Use the following variables for present value calculations.
home_price = 100000  # Investment cost
expected_sale_price = 120000  # Future Value of the home
hurdle_rate = 0.10  # 0.10 = 10% # Annual Discount Rate; minimum return expected
holding_months = 12  # Number of months until sold (until Future Value)

# Using `expected_sale_price`, `hurdle_rate`, and `holding_months`,
# calculate the present value of the home. Save the result as a new
# variable named `present_value`.
# Use the **monthly** version of the present value formula. 
present_value = expected_sale_price / (1 + (hurdle_rate / 12)) ** holding_months
print(f"Present Value is ${present_value}")


# Put `present_value` into a conditional statement:
# If present value is greater than cost to buy (home_price), buy it:
if present_value > home_price:
    print("Take the plunge! It's worth more than it's selling for.")
# Otherwise, take a pass:
elif present_value < home_price:
    print("Don't buy this, as it's offered at a price higher than what it's worth.")
# Bonus Points! The edge case:
elif present_value == home_price:
    print(
        "Breakeven case! You can expect to earn exactly your hurdle rate on this deal."
    )
