# -*- coding: utf-8 -*-
"""Instructor Demo: Lists.

This script showcases basic operations of Python Lists.
"""
this_is_a_list = list([1, 2, 3])
this_is_a_list = [1, 2, 3]
this_is_a_list.append(4)
this_is_a_list.append(5)
this_is_a_list.insert(0, 25)
del this_is_a_list[0]
print(this_is_a_list)

l2 = [0, 3.3, "word", "True"]
print(l2[-1])




stock_tickers = ["amz", "csco", ]

#add to list
stock_tickers.append("ZM")
print(stock_tickers)

#add to the beginning of the list
stock_tickers.insert(0, "aapl")
print(stock_tickers)



