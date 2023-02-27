#!/usr/bin/python3
def search_replace(my_list, serach, replace):
    return [element if element != search else replace for element in my_list]
