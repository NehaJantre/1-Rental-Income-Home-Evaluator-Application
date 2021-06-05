"""Split Second Part 2."""
# This function should have the following 4 parameters: home_price, expected_sale_price, hurdle_rate, holding_months
# The function should contain the following code (the solutions from Part 1 of this activity):

def price_this_home(home_price, expected_sale_price, hurdle_rate, holding_months):
    present_value = expected_sale_price / (1 + (hurdle_rate / 12)) ** holding_months

    # Put `present_value` into a conditional statement:
    # If present value is greater than cost to buy (home_price), buy it:
    if present_value > home_price:
        print("Buy this one, junior analyst! It's worth more than it's selling for.")
    # Otherwise, take a pass:
    elif present_value < home_price:
        print("Don't buy this, as it's offered at a price higher than what it's worth.")
    # Bonus Points! The edge case:
    elif present_value == home_price:
        print(
            "Breakeven case! You can expect to earn exactly your hurdle rate on this deal."
        )

    # Have the function calculate and return the expected profit, or `net_present_value`, of the home being evaluated. 
    # This is defined as the `present_value` of the home, minus the `current home_price`.
    net_present_value = present_value - home_price
    return net_present_value


# Run the function
npv = price_this_home(
    home_price=100000, expected_sale_price=180000, hurdle_rate=0.10, holding_months=36
)

# Print the npv
print(f"The Expected Profit is: {npv}")
