#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "IV" : 4, "V": 5, "IX":9, "X":10, "L":50, "C":100, "D":500, "M":1000}
    roman_list = list(roman_string)
    somme = 0
    if not roman_string :
        return 0
    for elt in roman_list:
        if elt in roman_dict.keys():
            somme = somme + roman_dict[elt]
    return somme