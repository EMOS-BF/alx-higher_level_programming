#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_do_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            key_do_delete.append(key)
    for key in key_do_delete:
        del a_dictionary[key]
    return a_dictionary