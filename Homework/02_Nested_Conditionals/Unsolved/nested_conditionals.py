"""Nested Conditionals."""

# @TODO: Create variables with the initial ad price and company type
ad_price = 10
company_type = "Existing"

# @TODO: Convert the following decision logic into valid Python code.
# if the ad price is affordable (less than 20):
#     if the company is a startup:
#         print that the expected profit is 500
#     elif the company is existing:
#         print that the expected profit is 100
#     else:
#         print that the company type is not specified
# else:
#     print that the ad price is too expensive

if ad_price < 20:
    if company_type == "Startup":
        print(f"Existing profit is ${500}")
    elif company_type == "Existing":
        print(f"Existing profit is ${100}")
    else:
        print("the company type was not specified")
else:
    print("Advertising rates are just too expensive")
