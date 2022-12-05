#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    count = 0
    for element in my_string_list:
        if element == 'c' or element == 'C':
            my_string_list[count] = ""
        count += 1
    return "".join(my_string_list)
