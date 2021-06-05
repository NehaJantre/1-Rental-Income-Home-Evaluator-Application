# -*- coding: utf-8 -*-
"""Instructor Demo: Dictionaries

This script showcases basic operations of Python Dicts.
"""
states = {
    "hawaii": "best state",
    "washington": "home state",
    "colorado": "second favorite"
}
print(states)

states["oregon"] = "hippy state"
print(states)
del states["hawaii"]
print(states)

value = states.get("washington")
print(value)