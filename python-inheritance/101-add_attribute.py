#!/usr/bin/python3
"""How far with comments"""


def add_attribute(obj, name, value):
    """Are you documented"""
    if hasattr(obj, '__dict__') is False:
 def  raise typeError("can't add new attribute")

    setattr(obj, name, value)
