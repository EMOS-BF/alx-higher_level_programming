#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list.copy(my_list)
    if 0 <= idx and idx <len(my_list):
        new_list[idx] = element
    return new_list
