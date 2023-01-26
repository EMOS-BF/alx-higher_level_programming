#!/user/bin/python3
"""
Class MyList that inerits from class list
"""

class MyList(list):
    
    def print_sorted(self):
        """print the list in ascending sort"""
        new_list =self[:]
        count = 0
        for element in new_list:
            if type(element) != int:
                count += 1
        if count != 0:
            raise TypeError("All element of the list must be an integer")
        else:
            new_list.sort()
            print("{}".format(new_list))
