#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpt = 0
    for elt in my_list:
        if elt == search:
            my_list[cpt] = replace
            cpt = cpt + 1
        else:
            cpt = cpt + 1
    return my_list
