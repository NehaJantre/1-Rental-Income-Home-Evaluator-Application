"""A Logical Processor."""

# 1. Create two new variables to hold user data:
# Populate this variable with our first user, who is based in the United States
# and is already registered on the platform.
location = "United States"
is_registered = True

# 2. Write a conditional statement. If user is based in the U.S. and
# already registered, advertise the new service. Otherwise, give them
# notice that the feature is coming soon.
if location == "United States" and is_registered:
    print("Now Available! Crypto Accepted!")
else:
    print("Crypto Payments - Coming Soon!")

# 3. Change the user location to Japan and print the results again.
# Does your conditional statement program work as expected?
location = "Japan"
is_registered = True

if location == "United States" and is_registered:
    print("Now Available! Crypto Accepted!")
else:
    print("Crypto Payments - Coming Soon!")
