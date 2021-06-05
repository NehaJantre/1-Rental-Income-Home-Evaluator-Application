"""Nested Conditionals."""

# Create variables with the initial ad price and company type
ad_price = 50
company_type = "Startup"

# Create a nested conditional logic statement to determine
# the company's expected profit given the following conditions:
# The code should first determine if the ad price is affordable or too expensive.
# Any ad price under $20 can be considered affordable,
# but anything else should be considered too expensive.
# If the ad price is under $20, then make a decision based on the company type.
# If the company is a "Startup", then print an expected profit of $500
# If the company is "Existing", then print an expected profit of $100
# Else, print that the company type was not specified.
if ad_price < 20:
    if company_type == "Startup":
        print(f"Expected profit is ${500}")
    elif company_type == "Existing":
        print(f"Expected profit is ${100}")
    else:
        print("Company type is not specified.")
else:
    print("Advertising rates are currently too expensive")
