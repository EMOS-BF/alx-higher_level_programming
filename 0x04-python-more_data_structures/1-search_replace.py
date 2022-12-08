#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpt = -1
    for elt in my_list:
        cpt = cpt + 1
        if elt == search:
            j = cpt
    my_list[j] = replace
    return my_list

