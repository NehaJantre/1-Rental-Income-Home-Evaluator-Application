# Lists - Manipulation Exercise

# Using the `stock_tickers` list, update, add and remove elements according to the specified instructions.
# Print after each action, print the list in order to confirm your syntax was correct.


stock_tickers = ["AMZN", "CSCO", "FB", "GOOG", "INTC", "MSFT", "SQ", "TWTR", "WRK"]


# @TODO Update the ticker 'WRK' to 'WORK'
# Print stock_tickers to confirm your code
#stock_tickers.update("WRK", "WORK")
print(stock_tickers)


# @TODO Add the ticker 'ZM' to the end of the stock_tickers list
stock_tickers.append("ZM")
# @TODO Print stock_tickers to confirm your code
print(stock_tickers)


# @TODO Add the ticker 'AAPL' to the beginning of the stock_tickers list.
# @TODO Add the ticker 'DELL' so it appears between 'CSCO' and 'FB'.
# @TODO Print stock_tickers to confirm your code
stock_tickers.insert(0, "APPL")
stock_tickers.insert(3, "DELL")
print(stock_tickers)


# @TODO Remove the ticker 'INTC' from the stock_tickers list
# @TODO Print stock_tickers to confirm your code
del stock_tickers[6]
print(stock_tickers)



# @TODO Remove the ticker 'SQ' from the list using the pop() method
# @TODO Print stock_tickers to confirm your code
stock_tickers.pop(7)
print(stock_tickers)


# @TODO Slice a section of the list that includes the tickers 'CSCO', 'DELL', 'FB', and 'GOOG'.
# @TODO Set this equal to a variable called stock_tickers_slice.
# @TODO Print the new variable to confirm your actions.
stock_tickers_slice = stock_tickers[2:6]
print(stock_tickers_slice)
